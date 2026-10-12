#!/bin/bash
# Scrape all Visme tech categories sequentially
cd /home/hatch/workspace/mcit-ai-library
CATS=("Resumes" "Biographies" "Presentations" "Infographics" "Reports" "Ebooks" "Proposals" "Charts & Graphs" "Whiteboards" "Videos" "Newsletters" "Brochures" "Performance Reviews" "Project Charters" "Posters" "Flyers" "Printable Forms" "Form Builder" "Documents" "Social Media Graphics" "Graphs" "Timelines" "Flowcharts" "Banners" "Charts" "Bar Graphs" "Line Graphs" "Video Tutorials" "Flyers (Small)")
for c in "${CATS[@]}"; do
  slug=$(echo "$c" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]\+/-/g; s/^-//; s/-$//')
  if [ -f "raw/${slug}.json" ]; then
    cnt=$(python3 -c "import json; print(json.load(open('raw/${slug}.json'))['count'])" 2>/dev/null)
    echo "SKIP $c ($cnt already)"
    continue
  fi
  echo "=== $c ==="
  timeout 600 node scrape-cat.js "$c" 2>&1 | tail -2
  sleep 3
done
echo "ALL DONE"
# Summary
python3 -c "
import json, glob
total = 0
for f in sorted(glob.glob('raw/*.json')):
    d = json.load(open(f))
    print(f\"{d['category']}: {d['count']}\")
    total += d['count']
print('TOTAL:', total)
"
