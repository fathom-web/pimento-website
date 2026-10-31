# Lokale kwaliteitscontrole

Getest op 28 september 2026, via de lokale site op http://127.0.0.1:4173/.

## Automatisch

- Bouw: 118 statische routes plus `404.html`.
- 119 HTML-bestanden gecontroleerd op interne links, lokale assets, één H1, titel, beschrijving, beeldafmetingen en altteksten.
- 95 recepten/mixideeën; geen lege recepten.
- Geen ontbrekende interne pagina’s of assetbestanden gevonden.
- JavaScript syntaxcheck met `node --check dist/app.js`: geslaagd.
- De eerste-weergavebestanden zijn samen circa 310 KiB, ongecomprimeerd op schijf. Dit is een bestandsgroottemeting, geen Lighthouse- of Core Web Vitals-score. Grote PDF’s laden uitsluitend op verzoek; fotografie onder de vouw is lazy-loaded.

## Browser

- Hoofdschermen home, product, recepten, verkooppunten, contact en Italian Mule gecontroleerd op 320, 390, 820 en 1440 pixels viewportbreedte.
- Na correctie geen horizontale overflow op deze 24 combinaties; zie `responsive-checks.json` voor client- en scrollbreedtes.
- Originele fles, logo en lokale WebP’s laden zonder gebroken beelden.
- Mobiel menu opent en navigatie naar recepten werkt.
- Alcoholvrij-filter geeft 13 resultaten; Gin geeft 10.
- Zoeken op `Italian Mule` geeft één resultaat en opent de juiste detailpagina.
- Niet-bestaande zoekterm geeft nul resultaten en een duidelijke lege toestand; reset herstelt de collectie.
- Italian Mule toont de juiste originele hoeveelheden: 5 cl gin, 12,5 cl Pimento, limoen, ijs en garnituur.
- Leeg contactformulier wordt tegengehouden door ingebouwde validatie voor naam, e-mail en bericht. Geen bericht is verzonden.
- Browserconsole: geen fouten of waarschuwingen in de gecontroleerde flows.
- Visuele desktop- en mobile screenshots opgeslagen in deze map.

## Wat niet is beweerd of gewijzigd

Geen verzending via een mailserver: het formulier stelt alleen een e-mailconcept samen. Geen bestelling geplaatst. Geen voorraad van leveranciers geverifieerd. Geen productie-/DNS-wijzigingen. Geen gegarandeerde performance-score of volledige WCAG-certificering; focusstijlen, semantiek, reduced-motion en responsieve leesbaarheid zijn wel in de implementatie meegenomen.
