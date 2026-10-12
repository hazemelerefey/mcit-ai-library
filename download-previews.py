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
    import re
    return re.sub(r'-+', '-', ''.join(c if c.isalnum() else '-' for c in s.lower()).strip('-'))

def download(url, dest):
    """Download with retries. Returns True on success."""
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
            with urllib.request.urlopen(req, timeout=45) as r, open(dest, 'wb') as f:
                while True:
                    chunk = r.read(65536)
                    if not chunk:
                        break
                    f.write(chunk)
            if os.path.getsize(dest) > 5000:
                return True
        except Exception:
            if attempt == 2:
                if os.path.exists(dest):
                    os.remove(dest)
                return False
            time.sleep(2)
    return False

def process():
    new = 0
    for jf in sorted(glob.glob(os.path.join(RAW, '*.json'))):
        d = json.load(open(jf))
        cat = slug(d['category'])
        for t in d['templates']:
            thumb = t.get('thumbnail', '')
            if not thumb:
                continue
            # template folder from URL slug
            tslug = t['url'].rstrip('/').rsplit('/', 1)[-1]
            tslug = '-'.join(tslug.split('-')[:-1]) if tslug.split('-')[-1].isdigit() else tslug
            tdir = os.path.join(PREV, cat, slug(tslug))
            os.makedirs(tdir, exist_ok=True)
            # base name: i_Name-full_1.jpg -> try _1.._30
            import re
            m = re.match(r'^(.*_full_)(\d+)(\.\w+)$', thumb.rsplit('/', 1)[-1])
            if not m:
                # single image fallback
                fname = thumb.rsplit('/', 1)[-1].split('?')[0]
                dest = os.path.join(tdir, fname)
                if not (os.path.exists(dest) and os.path.getsize(dest) > 5000):
                    if download(thumb, dest):
                        new += 1
                continue
            prefix, _, ext = m.group(1), m.group(2), m.group(3)
            base_url = thumb.rsplit('/', 1)[0] + '/'
            for n in range(1, 31):
                fname = f'{prefix}{n}{ext}'
                dest = os.path.join(tdir, f'slide-{n}{ext}')
                if os.path.exists(dest) and os.path.getsize(dest) > 5000:
                    continue
                if download(base_url + fname, dest):
                    new += 1
                else:
                    break  # first 404 = no more slides
        print(f'{d["category"]}: done')
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
