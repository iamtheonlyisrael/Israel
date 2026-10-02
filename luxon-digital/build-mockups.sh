#!/usr/bin/env bash
# Assembles the Home page blocks into mockups/home.html. All other pages: python3 build-pages.py
# Usage: ./build-mockups.sh
set -euo pipefail
cd "$(dirname "$0")"

page() { # page <output> <title> <block files...>
  local out="$1" title="$2"; shift 2
  {
    printf '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    printf '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    printf '<title>%s</title>\n' "$title"
    printf '<style>html{scroll-behavior:smooth}body{margin:0;background:#FFFFFF}</style>\n</head>\n<body>\n'
    for f in "$@"; do printf '\n<!-- ===== %s ===== -->\n' "$f"; cat "$f"; done
    printf '\n</body>\n</html>\n'
  } > "$out"
  echo "built $out"
}

page mockups/home.html "Luxon Digital | AI Automation for Limo & Transportation Companies" \
  shared/header.html home/01-hero.html home/02-missed-call.html home/03-how-it-works.html \
  home/04-features.html home/05-who-its-for.html home/06-guardrails.html home/07-founder-story.html \
  shared/cta-band.html shared/footer.html
