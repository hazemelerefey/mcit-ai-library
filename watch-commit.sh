#!/bin/bash
# Watch raw/ for new scrape outputs and commit each one in real time.
cd /home/hatch/workspace/mcit-ai-library
while true; do
  # stage any new/changed files
  git add -A 2>/dev/null
  if ! git diff --cached --quiet; then
    n=$(git diff --cached --name-only | wc -l)
    # build message from changed category files
    cats=$(git diff --cached --name-only | grep -o "raw/[a-z-]*\.json" | sed 's|raw/||; s|\.json||' | tr '\n' ' ')
    total=$(python3 -c "
import json, glob
t = sum(json.load(open(f))['count'] for f in glob.glob('raw/*.json'))
print(t)" 2>/dev/null)
    git commit -qm "templates: ${cats}(total ${total})" 2>/dev/null
    git push -q origin master 2>/dev/null
    echo "[$(date +%H:%M:%S)] committed+pushed: ${cats} total=${total}"
  fi
  sleep 30
done
