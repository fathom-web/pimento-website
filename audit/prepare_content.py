from pathlib import Path
from lxml import html
from PIL import Image
import json,re,unicodedata

root=Path(__file__).resolve().parents[1]
pages=json.loads((root/'audit/content.json').read_text(encoding='utf-8'))
byid={p['id']:p for p in pages}
categories={45:'Alcoholvrij',49:'Gin',51:'Rum',53:'Wodka',55:'Tequila',59:'Overige cocktails',43:'Shooters',47:'Gerechten'}
def slug(s):
    return re.sub(r'[^a-z0-9]+','-',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()).strip('-')
def lines(node):
    raw=html.tostring(node,encoding='unicode')
    raw=re.sub(r'<br\s*/?>','\n',raw)
    raw=re.sub(r'</(?:p|li|ul|div)>','\n',raw)
    return [re.sub(r'\s+',' ',x).strip(' –\xa0') for x in html.fromstring('<div>'+raw+'</div>').text_content().splitlines() if x.strip(' –\xa0')]
recipes=[]
for pageid,cat in categories.items():
    node=html.fromstring(byid[pageid]['html'])
    current=None
    for el in node:
        text=el.text_content().strip()
        strong=el.xpath('.//strong')
        name=strong[0].text_content().strip(' :\xa0\n\u2028') if strong else ''
        if text=='Pimento Caipirinha': name=text
        if name and name not in ['Pimento','Enkele tip;','–','Marinade','Mélangez la farine et le Pimento.']:
            current={'name':name,'slug':slug(name),'categories':[cat],'lines':[],'source':next(p['link'] for p in json.loads((root/'audit/pages.json').read_text(encoding='utf-8-sig')) if p['id']==pageid)}
            recipes.append(current)
            ls=lines(el)
            if ls and ls[0].strip(' :')==name:ls=ls[1:]
            elif ls and ls[0].startswith(name):ls[0]=ls[0][len(name):].strip(' ,;:')
            current['lines'].extend(x for x in ls if x)
        elif current and el.tag not in ['h1','h2']:
            current['lines'].extend(lines(el))
# Deduplicate recipes which occur in more than one spirit category.
unique={}
for r in recipes:
    if r['slug'] in unique:
        unique[r['slug']]['categories']+=r['categories']
    else:unique[r['slug']]=r
recipes=list(unique.values())
# Original mixing ideas are deliberately retained; clarify that sparkling wine must be alcohol-free.
for r in recipes:
    if r['name']=='Alcoholvrij welkoms drankje':
        r['lines']=['Gebruik expliciet alcoholvrije mousserende wijn.','Meng 50% alcoholvrije mousserende wijn met 50% Pimento.']
    if r['name']=='Spicy smoothie':r['lines']=['Voeg Pimento naar eigen smaak toe aan je smoothie.']
    if r['name']=='Spicy Bowl':r['lines']=['Maak een alcoholvrije vruchtenbowl en voeg naar eigen smaak Pimento toe.']
    if r['name']=='Pimento Nojito / Spicy Virgin Mocktail':
        r['name']='Pimento Nojito';r['slug']='pimento-nojito'
        r['ingredients']=['Een paar schijfjes limoen','Verse muntblaadjes','Crushed ijs','Pimento om aan te vullen']
        r['steps']=['Kneus de limoen en munt voorzichtig met een muddler in een groot glas.','Voeg een flinke schep crushed ijs toe.','Vul aan met ijskoude Pimento en roer zachtjes.']
    if r['name']=='Italian Mule':
        r['ingredients']=['5 cl Roby Marton Gin','12,5 cl Pimento Spicy Ginger','Limoensap naar smaak','IJsblokjes of crushed ijs','Munt, een schijfje limoen en gember']
        r['steps']=['Vul een mulebeker of groot glas met ijs.','Voeg gin en limoensap toe.','Schenk de Pimento erbij en roer voorzichtig. Garneer met munt, limoen en gember.']
    if r['name']=='Pimento Storm':
        r['ingredients']=['6 cl donkere Jamaicaanse rum','1,5 cl vers limoensap','Pimento om aan te vullen','Gebroken ijs','Een partje limoen']
        r['steps']=['Shake de rum en het limoensap met ijs.','Zeef in een laag glas gevuld met gebroken ijs.','Vul aan met Pimento en garneer met een partje limoen.']
    if r['name']=='Hot Mule':
        r['ingredients']=['4 cl wodka','6 cl Pimento','2 cl vers limoensap','IJsblokjes']
        r['steps']=['Vul een laag glas met ijsblokjes.','Voeg wodka en limoensap toe.','Schenk de Pimento erbij en roer zachtjes.']
    if r['name']=='The Trident':
        r['ingredients']=['5 cl Poseidon Gin','12,5 cl Pimento Spicy Ginger','IJsblokjes','Een schijfje citroen']
        r['steps']=['Vul een tumbler met ijs.','Voeg gin en Pimento toe.','Roer voorzichtig en garneer met citroen.']
(root/'content').mkdir(exist_ok=True)
(root/'content/recipes.json').write_text(json.dumps(recipes,ensure_ascii=False,indent=2),encoding='utf-8')
assets=root/'dist/assets'
for source,target,size in [('DEF-PIMENTO-scaled.png','bottle.webp',(750,1700)),('91266241_2329581037339298_2581447500070125568_n.jpg','bar.webp',(900,650)),('20664908_1848047835209634_2074029553837587838_n.jpg','italian-mule.webp',(960,750)),('13445370_364158197041973_7975422145089464604_n.jpg','bartender.webp',(960,639))]:
    im=Image.open(assets/source);im.thumbnail(size);im.save(assets/target,'WEBP',quality=88)
im=Image.open(r'C:\Users\SKIKK\.codex\generated_images\01a0e931-0ae2-7971-9eb4-280badd5e59b\exec-5f798de0-a648-49f7-aa3f-8a35bbe3354c.png')
im.save(assets/'aperitif.webp','WEBP',quality=87)
print(f'{len(recipes)} unique recipes; '+', '.join(f'{cat}: {sum(cat in r["categories"] for r in recipes)}' for cat in categories.values()))
print([r['name'] for r in recipes])
