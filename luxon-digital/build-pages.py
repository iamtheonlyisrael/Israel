#!/usr/bin/env python3
"""Builds the paste-ready page blocks and full-page mockups.

  pages/src/<page>.html   page content (uses kit classes and {{i:name}} / {{i:name:size}} icons)
  kit/kit.css, kit/reveal.js  shared styles + scroll reveal, inlined into every block
  -> pages/<page>.html    ONE self-contained block: paste into a GHL Custom Code element
  -> mockups/<page>.html  header + page block + CTA band + footer, to preview in a browser

Run:  python3 build-pages.py
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)

ICONS = {
  'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
  'msg': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="M8 9h8M8 13h5"/>',
  'star': '<path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/>',
  'board': '<rect x="3" y="3" width="7" height="18" rx="1.5"/><rect x="14" y="3" width="7" height="11" rx="1.5"/>',
  'car': '<path d="M5 17h14M3 13l2-6h14l2 6v4H3z"/><circle cx="7.5" cy="17" r="1.5"/><circle cx="16.5" cy="17" r="1.5"/>',
  'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
  'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
  'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
  'users': '<circle cx="9" cy="8" r="3.5"/><circle cx="17" cy="9" r="2.5"/><path d="M2 20c0-3.5 3-5.5 7-5.5s7 2 7 5.5M16 14.5c3 0 6 1.5 6 4.5"/>',
  'check': '<path d="M5 12l5 5L20 7"/>',
  'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
  'cal': '<rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/>',
  'moon': '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>',
  'plane': '<path d="M2 16l20-6-3-3-6 2-6-5-2 1 4 6-5 2-2-2-2 1z"/>',
  'brief': '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/>',
  'trend': '<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
  'bulb': '<path d="M9 18h6M10 22h4"/><path d="M12 2a7 7 0 0 0-4 12.7V16h8v-1.3A7 7 0 0 0 12 2z"/>',
  'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
  'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
  'search': '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
  'lock': '<rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
  'file': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
  'repeat': '<path d="M17 2l4 4-4 4"/><path d="M3 11V9a3 3 0 0 1 3-3h15M7 22l-4-4 4-4"/><path d="M21 13v2a3 3 0 0 1-3 3H3"/>',
  'alert': '<path d="M12 9v4M12 17h.01"/><path d="M10.3 3.9L1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/>',
  'bolt': '<path d="M13 2L3 14h9l-1 8 10-12h-9z"/>',
  'video': '<rect x="2" y="6" width="14" height="12" rx="2"/><path d="M16 10l6-3v10l-6-3"/>',
  'tool': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
  'play': None,
}

def icon(m):
    name = m.group(1); size = m.group(2) or '22'
    if name == 'play':
        return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
    if name == 'starf':
        return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="#D4AF37" aria-hidden="true">{ICONS["star"]}</svg>'
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')

kit = open(P('kit', 'kit.css')).read()
reveal = open(P('kit', 'reveal.js')).read()
shared = lambda f: open(P('shared', f)).read()

TITLES = {
  'about': 'About Us', 'luxon-limo-ai': 'Luxon Limo AI', 'ai-receptionist': 'AI Receptionist',
  'lead-follow-up': 'Automated Lead Follow-Up', 'review-automation': 'Review Automation',
  'lead-management': 'Lead Management', 'demo': 'Demo', 'pricing': 'Pricing', 'faq': 'FAQ',
  'contact': 'Contact / Book a Demo', 'privacy-policy': 'Privacy Policy', 'terms-and-conditions': 'Terms & Conditions',
}
NO_CTA = {'contact', 'privacy-policy', 'terms-and-conditions'}

os.makedirs(P('mockups'), exist_ok=True)
for fn in sorted(os.listdir(P('pages', 'src'))):
    if not fn.endswith('.html'):
        continue
    page = fn[:-5]
    body = open(P('pages', 'src', fn)).read()
    body = re.sub(r'\{\{i:([a-z]+)(?::(\d+))?\}\}', icon, body)
    assert '{{' not in body, f'unreplaced placeholder in {fn}'
    block = (f'<!-- Luxon Digital | {TITLES.get(page, page)} page | paste this whole block into ONE Custom Code element -->\n'
             f'<div class="lxk">\n<style>\n{kit}</style>\n{body.strip()}\n<script>\n{reveal}</script>\n</div>\n')
    open(P('pages', fn), 'w').write(block)
    parts = [shared('header.html'), block] + ([] if page in NO_CTA else [shared('cta-band.html')]) + [shared('footer.html')]
    html = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f'<title>{TITLES.get(page, page)} | Luxon Digital</title>\n'
            '<style>html{scroll-behavior:smooth}body{margin:0;background:#FFFFFF}</style>\n</head>\n<body>\n'
            + '\n'.join(parts) + '\n</body>\n</html>\n')
    open(P('mockups', fn), 'w').write(html)
    print('built', page)
