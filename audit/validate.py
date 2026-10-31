"""Check all generated pages, internal routes and local assets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
root=Path(__file__).resolve().parents[1]
dist=root/'dist'
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.refs=[];self.h1=0;self.imgs=[];self.ids=set();self.desc=False;self.title=False
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='h1':self.h1+=1
        if tag=='title':self.title=True
        if tag=='meta' and a.get('name')=='description':self.desc=True
        if 'id' in a:self.ids.add(a['id'])
        if tag=='img':self.imgs.append(a)
        for attr in ['href','src']:
            if a.get(attr):self.refs.append(a[attr])
errors=[];count=0
for f in dist.rglob('*.html'):
    p=Page();p.feed(f.read_text(encoding='utf-8'));count+=1
    if p.h1!=1:errors.append(f'{f.relative_to(dist)}: {p.h1} H1 elements')
    if not p.title or not p.desc:errors.append(f'{f.relative_to(dist)}: missing metadata')
    for im in p.imgs:
        if 'alt' not in im:errors.append(f'{f.name}: image without alt')
        if 'width' not in im or 'height' not in im:errors.append(f'{f.name}: image without dimensions')
    for ref in p.refs:
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        if not u.path:
            if u.fragment and u.fragment not in p.ids:errors.append(f'{f}: missing anchor {ref}')
            continue
        target=dist/unquote(u.path).lstrip('/') if u.path.startswith('/') else f.parent/unquote(u.path)
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(f'{f.relative_to(dist)}: missing {ref}')
recipes=json.loads((root/'content/recipes.json').read_text(encoding='utf-8'))
for r in recipes:
    if not r.get('lines') and not r.get('ingredients'):errors.append('Empty recipe '+r['name'])
report={'pages_checked':count,'recipes':len(recipes),'errors':errors,'critical_assets_bytes':sum((dist/p).stat().st_size for p in ['index.html','styles.css','pages.css','accessibility.css','app.js','assets/display.ttf','assets/body.ttf','assets/logo.png','assets/bottle.webp'])}
(root/'audit/validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2));raise SystemExit(bool(errors))
