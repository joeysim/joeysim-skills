#!/bin/sh
# Render each card in cards/ to its 1200x630 og.png in pages/. Run from the repo root: sh cards/render.sh
set -e
chrome="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"
for card in cards/*.html; do
  name=$(basename "$card" .html)
  if [ "$name" = index ]; then out=pages/og.png; else out="pages/$name/og.png"; fi
  "$chrome" --headless --hide-scrollbars --force-device-scale-factor=1 --window-size=1200,630 \
    --screenshot="$PWD/$out" "file://$PWD/$card" 2>/dev/null
  echo "$out"
done
