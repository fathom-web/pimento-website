# Pimento — audit, contentinventaris en ontwerp

Auditdatum: 28 september 2026. Primaire bron: https://www.pimentodrink.nl/.

## Bronnen en dekking

Alle 21 openbare WordPress-pagina’s zijn via de publieke pagina-index gevonden en als volledige HTML opgeslagen (`page-*.html`). De REST-contentvelden waren grotendeels leeg doordat content in themavelden staat. Daarom is de zichtbare content uit de HTML gehaald, niet alleen de API-inhoud. `pages.json`, `media.json`, `content.json` en `content.txt` bewaren de inventaris en originele tekst.

De 25 mediabestanden uit de openbare media-index zijn gedownload, plus het originele themalogo. Ze omvatten de groene fles uit 2021, eerdere flesfotografie, Italian Mule-beelden, merkadvertenties, mocktailafbeeldingen en PDF-presentaties/cocktailkaarten. `contact-sheet.jpg` toont de beschikbare rasterbeelden. Bron-URL’s en originele afmetingen staan in `media.json`.

Pagina’s: home, over ons, producten, recepten, cocktails, gin, rum, wodka, tequila, diverse cocktails, shooters, mocktails, 0.0 Pimento Mix, Italian Mule, gerechten, agenda, waar te koop, contact, sitemap, voorwaarden en disclaimer.

## Bevindingen

- De oorspronkelijke menustructuur heeft drie niveaus; bezoekers moeten eerst de juiste drankcategorie vinden voordat ze recepten zien.
- De productbelofte is onderscheidend: gember, tonic en chilipeper; alcoholvrij; puur en als mixer.
- Veel pagina’s herhalen dezelfde fles, maar missen hiërarchie, duidelijke vervolgstappen en mobiele leesbaarheid.
- De navigatie verwijst naar een oudere Vana Tallinn-webshop. De verkooppuntenpagina verwijst specifieker naar https://shop.real-est-dranken.nl/32-pimento. Die laatste URL is behouden. Tijdens controle antwoordde de shop na een doorverwijzing naar HTTP met de titel “Pimento Spicy Ginger - Real Est Dranken Webshop”. De beveiliging van die externe shop valt buiten deze herbouw.
- De homepage/footer noemen KvK 32172008 en btw NL822424757B01; de contactpagina noemt KvK 72096837 en btw NL001706078883. Deze tegenstrijdige nummers zijn niet als bevestigde bedrijfsgegevens in de nieuwe contactsectie gepubliceerd. Originele juridische teksten blijven ongewijzigd beschikbaar; laat die voor een productielancering door de eigenaar nalopen.
- De contactpagina noemt Ronhaarstraat 48, 3815 MC Amersfoort, 06-11916408 en info@real-est-dranken.nl. Die gegevens zijn gebruikt. Het oudere info@pimentodrink.nl is in bronmateriaal bewaard.
- De agenda bevat geen datums bij Leeuwarden/Goes en een verwijzing naar een afgelopen Horecava. Er worden daarom geen verzonnen toekomstige evenementen getoond; de nieuwe pagina verwijst naar contact voor actuele planning.
- De verkooppuntenkaart stond als “under construction” vermeld. De oorspronkelijke link is behouden, zonder actuele voorraad of volledige dekking te beloven.
- De bron zegt enerzijds dat particulieren via de shop kunnen bestellen, anderzijds dat een KvK-nummer nodig is. De nieuwe site laat actuele bestelvoorwaarden bij de bestaande shop en belooft geen specifieke besteltoegang.
- Een alcoholvrij welkomsdrankje noemt prosecco/cava zonder expliciet “alcoholvrij”. De nieuwe recepttekst specificeert alcoholvrije mousserende wijn.
- De source bevat soms onduidelijke hoeveelheden of bereidingsinstructies (bijvoorbeeld 125 cl Pimento voor 125 g meel bij gambas). Die originele recepten zijn behouden zonder zelf hoeveelheden te verzinnen. Bij drankrecepten staat dat bruisende Pimento na het shaken wordt toegevoegd.
- De oudere boodschap gericht op minderjarigen is niet hergebruikt; de nieuwe site richt zich op volwassenen.

## Receptmigratie

95 unieke recepten en mixideeën. Recepten die in meerdere categorieën voorkomen zijn samengevoegd en houden meerdere categorieën. Tellingen overlappen: Alcoholvrij 13, Gin 10, Rum 14, Wodka 12, Tequila 12, Overige cocktails 24, Shooters 10, Gerechten 5.

De Italian Mule-detailpagina en 0.0 Mix-pagina bevatten varianten/herhalingen van recepten op de categoriepagina’s; hun routes blijven bruikbaar. Vijf recepten kregen Nederlandse ingrediënten en stappen naast bewaarde originele bronregels: Nojito, Italian Mule, Pimento Storm, Hot Mule en The Trident. Namen, auteursvermeldingen en overige originele tekst staan in `content/recipes.json`.

## Nieuwe informatiearchitectuur

1. Home: merkbelofte, smaak, sfeermoment, drie geselecteerde recepten, horeca.
2. Ontdek Pimento: product, smaakprofiel, puur/mocktail/cocktail, koken.
3. Recepten: één doorzoekbare collectie, acht filters, afzonderlijke detailpagina’s en printweergave.
4. Waar te koop: externe shop, oorspronkelijke leveranciers en kaart.
5. Horeca & contact: persoonlijk contact, e-mailconcept, zakelijke downloads.

Over ons, evenementen, voorwaarden, disclaimer en sitemap staan in de footer. Oude categorie- en productroutes blijven bestaan. Alle recepten zijn statisch toegankelijk zonder JavaScript.

## Design system

Visuele these: een warme, uitgesproken aperitiefwereld rond de originele groene fles — volwassen, helder en toegankelijk.

- Geel `#f4cf43`: productpodium en herkenningskleur.
- Rood `#b52c21`: kick, nadruk en horeca-sectie.
- Inkt `#24271f`: tekst, knoppen en één donkere sfeersectie.
- Papier `#faf9f3`: rustige leesvlakken; `#eceee5` voor ondersteunende secties.
- Barlow Condensed 800: krachtige compacte displaytypografie.
- DM Sans: leesbare lopende tekst. Lokale fonts; geen runtime-fontverzoeken.
- Rechthoekige knoppen, fijne scheidingslijnen, ruime witruimte. Geen standaard dashboardkaarten, carrousels of decoratieve emoji’s.
- Korte entree van de fles, zachte reveal, hovertransities en fotobeweging. Reduced-motion wordt gerespecteerd. Geen scroll-hijacking.
- 44px of grotere primaire touch-controls, zichtbare focus, skiplink, semantische elementen en gelabelde velden.

## Benchmark

Officiële pagina’s van Heineken, Bacardí, Fever-Tree en Schweppes zijn gelezen. Referenties: https://www.heineken.com/nl/nl/home/, https://www.bacardi.com/, https://fever-tree.com/en-gb en https://www.schweppes.com/.

Abstracte lessen: laat het product en de merkwereld domineren, geef recepten een duidelijke rol, scheid consumenten- en professionele taken en maak commerciële vervolgstappen makkelijk te vinden. Er zijn geen slogans, kleurpaletten, layouts, typografische systemen of assets van deze merken overgenomen.

## Beeldprovenance

Originele logo/fles/recept-/barbeelden: pimentodrink.nl. Geoptimaliseerde WebP-kopieën veranderen de compositie niet. `aperitif.webp` is een nieuwe AI-gegenereerde redactionele sfeerfoto: ginger mocktail, limoen, munt, gember en chili in warm middaglicht. Deze is als serveersuggestie toegepast; het is geen documentaire productfoto of exacte receptfoto.

## Testresultaten

Zie `validation.json` voor de automatische controle van alle lokale links, assets en pagina’s, en `QA.md` voor browsercontroles. Geen verzonnen Lighthouse-score of live voorraadinformatie.
