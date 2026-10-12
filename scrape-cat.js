/* Scrape all tech templates for one category.
   Usage: node scrape-cat.js "Presentations"
   Saves raw/<slug>.json */
const puppeteer = require('/home/hatch/workspace/skills/screen-record/scripts/node_modules/puppeteer-core');
const fs = require('fs');

const OUT = '/home/hatch/workspace/mcit-ai-library/raw';
const URL = 'https://www.visme.co/templates/industry/technology/';
const slug = s => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

(async () => {
  const catName = process.argv[2];
  if (!catName) { console.error('need category name'); process.exit(1); }
  fs.mkdirSync(OUT, { recursive: true });

  const browser = await puppeteer.launch({
    executablePath: '/opt/meta-chromium/chrome',
    headless: 'new',
    args: ['--no-sandbox', '--disable-dev-shm-usage', '--window-size=1400,900',
           '--proxy-server=127.0.0.1:8888', '--ignore-certificate-errors'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1400, height: 900 });
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36');

  await page.goto(URL, { waitUntil: 'networkidle2', timeout: 60000 });
  await new Promise(r => setTimeout(r, 4000));

  // Click the category filter button
  const clicked = await page.evaluate((name) => {
    const els = document.querySelectorAll('button');
    for (const el of els) {
      if ((el.innerText || '').trim().toLowerCase() === name.toLowerCase()) {
        el.click();
        return true;
      }
    }
    return false;
  }, catName);
  if (!clicked) { console.error('button not found:', catName); await browser.close(); process.exit(1); }
  console.log('clicked', catName);
  await new Promise(r => setTimeout(r, 4000));

  // Click "Load more" until exhausted (max 30 clicks)
  for (let i = 0; i < 30; i++) {
    // scroll to bottom to reveal the button
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
    await new Promise(r => setTimeout(r, 2000));
    const more = await page.evaluate(() => {
      const els = [...document.querySelectorAll('button, a, [role="button"]')];
      const btn = els.find(e => /load more/i.test((e.innerText || '').trim()) && e.offsetParent !== null);
      if (btn) { btn.scrollIntoView({ block: 'center' }); btn.click(); return (btn.innerText || '').trim(); }
      return false;
    });
    if (!more) { console.log('no more button after', i, 'clicks'); break; }
    console.log('load more click', i + 1, '-', more);
    await new Promise(r => setTimeout(r, 3500));
  }

  // Extract templates
  const templates = await page.evaluate(() => {
    const out = [];
    const seen = new Set();
    document.querySelectorAll('a[href*="/templates/"]').forEach(a => {
      const href = a.href;
      // template detail URLs end with -<id>/
      const m = href.match(/\/templates\/[a-z-]+\/[a-z0-9-]+-\d+\/?$/);
      if (!m || seen.has(href)) return;
      seen.add(href);
      const img = a.querySelector('img');
      const title = (a.getAttribute('title') || img && img.alt || a.innerText || '').trim();
      out.push({
        name: title,
        url: href,
        thumbnail: img ? (img.src || img.dataset.src || '') : '',
      });
    });
    return out;
  });

  const file = `${OUT}/${slug(catName)}.json`;
  fs.writeFileSync(file, JSON.stringify({ category: catName, count: templates.length, templates }, null, 1));
  console.log(`saved ${templates.length} templates to ${file}`);
  await browser.close();
})().catch(e => { console.error('FAIL:', e.message); process.exit(1); });
