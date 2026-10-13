#!/usr/bin/env python3
"""Build master templates.json index + gallery.html from raw scrape data."""
import json, glob, os, re

LIB = '/home/hatch/workspace/mcit-ai-library'
RAW = os.path.join(LIB, 'raw')
PREV = os.path.join(LIB, 'previews')

def slug(s):
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s.lower())).strip('-')

def main():
    templates = []
    categories = {}
    for jf in sorted(glob.glob(os.path.join(RAW, '*.json'))):
        d = json.load(open(jf))
        cat = d['category']
        cslug = slug(cat)
        categories[cslug] = {'name': cat, 'slug': cslug, 'count': 0, 'templates': []}
        for t in d['templates']:
            tslug = t['url'].rstrip('/').rsplit('/', 1)[-1]
            tslug = '-'.join(tslug.split('-')[:-1]) if tslug.split('-')[-1].isdigit() else tslug
            tdir = os.path.join(PREV, cslug, slug(tslug))
            slides = sorted(glob.glob(os.path.join(tdir, 'slide-*.jpg')))
            rec = {
                'id': f'{cslug}/{slug(tslug)}',
                'title': t.get('title', tslug),
                'category': cat,
                'category_slug': cslug,
                'source_url': t['url'],
                'slides': [os.path.relpath(s, LIB) for s in slides],
                'slide_count': len(slides),
                'downloaded': len(slides) > 0,
            }
            templates.append(rec)
            categories[cslug]['templates'].append(rec['id'])
            categories[cslug]['count'] += 1

    index = {
        'generated': __import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),
        'total_templates': len(templates),
        'total_categories': len(categories),
        'downloaded_templates': sum(1 for t in templates if t['downloaded']),
        'total_slides': sum(t['slide_count'] for t in templates),
        'categories': categories,
        'templates': templates,
    }
    with open(os.path.join(LIB, 'templates.json'), 'w') as f:
        json.dump(index, f, indent=1)
    print(f"templates.json: {len(templates)} templates, {len(categories)} categories, "
          f"{index['downloaded_templates']} downloaded, {index['total_slides']} slides")

    # gallery.html
    cards = []
    for t in templates:
        thumb = t['slides'][0] if t['slides'] else ''
        img = f'<img src="{thumb}" loading="lazy" alt="">' if thumb else '<div class="noimg">no preview yet</div>'
        cards.append(f'''<a class="card" href="{t["source_url"]}" target="_blank">
  <div class="thumb">{img}</div>
  <div class="meta"><span class="cat">{t["category"]}</span>
  <span class="title">{t["title"]}</span>
  <span class="n">{t["slide_count"]} slides</span></div></a>''')
    html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>MCIT AI Library — Template Gallery</title>
<style>
body{{font-family:system-ui,sans-serif;background:#0a0a0a;color:#e5e5e5;margin:0;padding:24px}}
h1{{font-size:20px;margin:0 0 4px}}p.sub{{color:#888;margin:0 0 20px;font-size:13px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}}
.card{{background:#141414;border:1px solid #262626;border-radius:8px;overflow:hidden;text-decoration:none;color:inherit}}
.card:hover{{border-color:#525252}}
.thumb{{aspect-ratio:16/9;background:#1a1a1a;display:flex;align-items:center;justify-content:center}}
.thumb img{{width:100%;height:100%;object-fit:cover}}
.noimg{{color:#555;font-size:12px}}
.meta{{padding:10px 12px;display:flex;flex-direction:column;gap:2px}}
.cat{{font-size:11px;color:#888;text-transform:uppercase;letter-spacing:.5px}}
.title{{font-size:13px;font-weight:600}}
.n{{font-size:11px;color:#666}}
</style></head><body>
<h1>MCIT AI Library</h1>
<p class="sub">{len(templates)} technology templates across {len(categories)} categories</p>
<div class="grid">
{''.join(cards)}
</div></body></html>'''
    with open(os.path.join(LIB, 'gallery.html'), 'w') as f:
        f.write(html)
    print(f"gallery.html: {len(cards)} cards")

if __name__ == '__main__':
    main()
