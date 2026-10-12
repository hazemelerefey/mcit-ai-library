#!/usr/bin/env python3
"""Download Visme template preview images into the library.
   Idempotent: skips files that already exist.
   Usage: python3 download-previews.py [watch]
   With 'watch', loops forever processing new raw/*.json files.
"""
import json, os, sys, time, glob, urllib.request

LIB = '/home/hatch/workspace/mcit-ai-library'
RAW = os.path.join(LIB, 'raw')
PREV = os.path.join(LIB, 'previews')

def slug(s):
    return ''.join(c if c.isalnum() else '-' for c in s.lower()).strip('-').replace('--', '-')

def process():
    new = 0
    for jf in sorted(glob.glob(os.path.join(RAW, '*.json'))):
        d = json.load(open(jf))
        cat = slug(d['category'])
        cdir = os.path.join(PREV, cat)
        os.makedirs(cdir, exist_ok=True)
        for t in d['templates']:
            thumb = t.get('thumbnail', '')
            if not thumb:
                continue
            # derive filename from URL
            fname = thumb.rsplit('/', 1)[-1].split('?')[0]
            if not fname.endswith(('.jpg', '.jpeg', '.png')):
                fname += '.jpg'
            dest = os.path.join(cdir, fname)
            if os.path.exists(dest) and os.path.getsize(dest) > 1000:
                continue
            try:
                req = urllib.request.Request(thumb, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=30) as r, open(dest, 'wb') as f:
                    f.write(r.read())
                new += 1
            except Exception as e:
                print(f'  skip {fname}: {type(e).__name__}')
        print(f'{d["category"]}: done ({len(d["templates"])} templates)')
    return new

if __name__ == '__main__':
    watch = len(sys.argv) > 1 and sys.argv[1] == 'watch'
    while True:
        n = process()
        total = sum(1 for _ in glob.glob(os.path.join(PREV, '*', '*.*')))
        print(f'pass complete: {n} new, {total} total previews')
        if not watch:
            break
        time.sleep(120)
