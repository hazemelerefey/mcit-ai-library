/* Scrape Visme technology templates per type filter.
   Usage: node scrape-visme.js [typeIndex]
   Saves to /home/hatch/workspace/mcit-ai-library/raw/<type>.json */
const puppeteer = require('/home/hatch/workspace/skills/screen-record/scripts/node_modules/puppeteer-core');
const fs = require('fs');
const path = require('path');

const OUT = '/home/hatch/workspace/mcit-ai-library/raw';
const URL = 'https://www.visme.co/templates/industry/technology/';

(async () => {
  const typeIdx = process.argv[2] ? parseInt(process.argv[2]) : null;
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

  console.log('loading', URL);
  await page.goto(URL, { waitUntil: 'networkidle2', timeout: 60000 });
  await new Promise(r => setTimeout(r, 4000));

  // Find type filter buttons
  const types = await page.evaluate(() => {
    const out = [];
    // look for buttons/links containing type names near the template grid
    const els = document.querySelectorAll('button, a, [role="button"]');
    const seen = new Set();
    const keywords = ['presentation', 'infographic', 'report', 'whiteboard', 'chart', 'graph', 'form', 'survey', 'document', 'social', 'video', 'ebook', 'proposal', 'flyer', 'poster', 'banner', 'brochure', 'newsletter', 'menu', 'resume', 'wireframe', 'mind map', 'flowchart', 'timeline', 'diagram'];
    els.forEach(el => {
      const t = (el.innerText || '').trim();
      if (t.length > 2 && t.length < 40 && !seen.has(t.toLowerCase())) {
        const low = t.toLowerCase();
        if (keywords.some(k => low.includes(k))) {
          seen.add(t.toLowerCase());
          out.push({ text: t, tag: el.tagName });
        }
      }
    });
    return out;
  });
  console.log('filter candidates:', JSON.stringify(types, null, 1));

  await browser.close();
})().catch(e => { console.error('FAIL:', e.message); process.exit(1); });
