from pathlib import Path
from lxml import html
import json
from PIL import Image, ImageOps, ImageDraw

pages=[]
for p in Path('audit').glob('page-*.html'):
    doc=html.fromstring(p.read_bytes())
    content=doc.xpath('//div[@class="border"]')
    if not content: continue
    node=content[0]
    title=doc.xpath('//div[@class="left"]/h1')[0].text_content()
    record={'id':int(p.stem.split('-')[1]),'title':title,'html':html.tostring(node,encoding='unicode'),'text':node.text_content().strip(),'links':[{'text':a.text_content(),'url':a.get('href')} for a in node.xpath('.//a[@href]')]}
    pages.append(record)
Path('audit/content.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
Path('audit/content.txt').write_text('\n\n'.join('PAGE '+str(p['id'])+' '+p['title']+'\n'+p['text'] for p in pages),encoding='utf-8')
files=[]
for f in Path('dist/assets').iterdir():
    try:
        im=Image.open(f); im.thumbnail((220,190)); files.append((f,im.copy().convert('RGBA')))
    except Exception: pass
sheet=Image.new('RGB',(880,240*((len(files)+3)//4)), '#ddd7c8')
d=ImageDraw.Draw(sheet)
for i,(f,im) in enumerate(files):
    x=(i%4)*220;y=(i//4)*240
    sheet.paste(im,(x+(220-im.width)//2,y),im)
    d.text((x+5,y+194),f.name[:28],fill='black')
sheet.save('audit/contact-sheet.jpg')
print([(p['id'],p['title'],len(p['text'])) for p in pages])
