# Pimento Nederland

Volledig herbouwde, statische merkwebsite. Geen framework-runtime, externe scripts, tracking of ingebouwde webshop. Alle pagina’s worden als HTML gegenereerd en blijven zonder JavaScript leesbaar.

## Lokaal bekijken

Open PowerShell in deze map en voer `./Start-Pimento.ps1` uit. Open vervolgens http://127.0.0.1:4173/.

Met `./Start-Pimento.ps1 -Rebuild` wordt eerst opnieuw gebouwd. Een andere poort kan met `-Port 4174`.

## Bewerken

- `build.py`: gedeelde paginaopbouw, overige pagina’s en recepttemplates; Python 3, alleen standaardbibliotheek.
- `templates/home.html`: bron voor de homepage, navigatie en gedeelde basis metadata.
- `content/recipes.json`: 95 unieke recepten en mixideeën, categorieën, oorspronkelijke tekst en bronlinks.
- `dist/styles.css`: basis design system en homepage.
- `dist/pages.css`: aanvullende pagina- en responsive stijlen.
- `dist/app.js`: mobiel menu, receptfilters, printknop en e-mailconcept.
- `dist/assets/`: originele merkassets, geoptimaliseerde WebP’s, lokale fonts en downloads.

`python build.py` bouwt 118 statische routes. `python audit/validate.py` controleert alle HTML-pagina’s, lokale links, assets, beeldafmetingen, altteksten en metadata.

## Werking en grenzen

De bestelknoppen openen de bestaande Real-Est Dranken-shop. Er is geen betaal- of winkelwagenfunctie toegevoegd. De bestaande shop verwijst zelf van HTTPS naar HTTP door; dit is ongewijzigd gelaten en staat in de audit.

Het contactformulier valideert lokaal en opent een `mailto:`-concept. Het verstuurt niet op de achtergrond en bewaart geen persoonsgegevens. De tekst blijft staan wanneer er geen mailprogramma is ingesteld. Voor server-side verzenden is later een echte maildienst nodig.

Receptnamen, makers, hoeveelheden en originele instructies zijn behouden. Vijf uitgelichte recepten kregen daarnaast Nederlandse ingrediënten en stappen. De overige originele teksten zijn Engels, Frans of Nederlands. Oude categorie-URL’s en de Italian Mule-URL blijven lokaal werken. Juridische teksten zijn ongewijzigd overgenomen; tegenstrijdige brongegevens staan in `audit/AUDIT.md`.

## Assets

Het logo, de fles, bestaande fotografie en PDF’s komen van pimentodrink.nl. Op 5 oktober 2026 is door de opdrachtgever aangeleverd materiaal toegevoegd: productfotografie met ingrediënten en bloemen, de barfoto, de Spicy Mocktail-afbeelding, de cocktailkaart, de roll-up, de advertentie en de Dry January-poster. De nieuwe foto's zijn als geoptimaliseerde WebP's verwerkt; drukwerk blijft als originele PDF beschikbaar. De eerder gebruikte AI-sfeerfoto (`aperitif.webp`) blijft als ongebruikt bestand bewaard. Geen assets of vormgeving van benchmarkmerken zijn gekopieerd.

Het contactadres is overal `info@real-est-dranken.nl`, inclusief het e-mailconcept en de disclaimer. De oorspronkelijke auditbronnen blijven bewaard; de build vervangt het oude adres in de gepubliceerde disclaimer.

De lokaal gebruikte Google Fonts zijn Barlow Condensed (800) en DM Sans (400). De interface gebruikt systeemfallbacks tijdens het laden.

## Publiceren

De inhoud van `dist/` kan door een statische webserver worden geserveerd, met directory-indexen en `404.html` als foutpagina. Deze oplevering draait lokaal; er zijn geen DNS- of productieaanpassingen gedaan. Stel bij een daadwerkelijke lancering de definitieve domeinmetadata, cacheheaders en 404-routering in. Downloads worden uitsluitend geladen wanneer de bezoeker ze opent.

Elke push naar de `main`-branch publiceert de website via GitHub Pages. De workflow bouwt de site opnieuw en past de interne links aan voor `/pimento-website/`.

## Feedback verwerkt op 5 november 2026

De homepage heeft een lichte grijsgroene achtergrond en een witte header. Het originele logo gebruikt geen kleurmengmodus meer; de slogan staat met extra tussenruimte onder het ruitvormige beeldmerk. De contacttitel schaalt op mobiel zodat “kennismaken” één woord blijft.

De zichtbare bedrijfsnaam is Uniqdrinks. De bestaande webshop-URL en het e-mailadres blijven behouden totdat vervangende adressen zijn aangeleverd. Facebook en LinkedIn gebruiken de opgegeven Nederlandse profielen. De homepage linkt naar de aangeleverde YouTube-commercial. Bij Horeca & contact staan de korte en lange Engelstalige producentpresentaties van juni 2026 als PDF-download. De lage-resolutie-artworks zijn niet als websitebeelden gebruikt.

Controle: alle 119 HTML-bestanden via `audit/validate.py`; 28 browserweergaven op 320, 360, 390, 760, 768, 1024 en 1440 pixels via `audit/feedback-2026/check.cjs`, inclusief mobiele contactnavigatie en beide PDF-downloads. Screenshots en resultaten staan in `audit/feedback-2026/`. Font-URL’s zijn relatief aan de stylesheet zodat ze ook onder het GitHub Pages-projectpad laden.
