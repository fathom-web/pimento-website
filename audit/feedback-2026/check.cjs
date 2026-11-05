const { chromium } = require('C:/Users/SKIKK/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('node:fs');
(async () => {
  const browser = await chromium.launch({ headless: true, channel: 'msedge' });
  const page = await browser.newPage({ reducedMotion: 'reduce' });
  const issues = [];
  const checks = [];
  for (const width of [320, 360, 390, 760, 768, 1024, 1440]) {
    await page.setViewportSize({ width, height: 1000 });
    for (const route of ['', 'contact/', 'waar-te-koop/', 'over-ons/']) {
      await page.goto('http://127.0.0.1:4173/' + route);
      await page.evaluate(() => document.fonts.ready);
      const state = await page.evaluate(() => {
        const rect = el => el.getBoundingClientRect();
        const word = document.querySelector('.contact-title-word');
        const brand = rect(document.querySelector('.brand img'));
        const tagline = rect(document.querySelector('.brand-tagline'));
        return {
          overflow: document.documentElement.scrollWidth > innerWidth,
          logoBlend: getComputedStyle(document.querySelector('.brand img')).mixBlendMode,
          taglineGap: tagline.top - brand.bottom,
          taglineCenterOffset: Math.abs(tagline.x + tagline.width / 2 - (brand.x + brand.width * .36)),
          wordFits: !word || rect(word).right <= innerWidth - 19,
          wordLines: word ? word.getClientRects().length : 0,
          socials: [...document.querySelectorAll('.site-footer a')].map(a => a.href),
          oldName: document.body.innerText.includes('Real-Est Dranken'),
          stylesheets: [...document.querySelectorAll('link[rel="stylesheet"]')].map(l => l.href),
        };
      });
      checks.push({ width, route, ...state });
      if (state.overflow || !state.wordFits || state.wordLines > 1 || state.logoBlend !== 'normal' || state.taglineGap < 5 || state.taglineCenterOffset > 1 || state.oldName || new Set(state.stylesheets).size !== state.stylesheets.length) issues.push({ width, route, state });
      if ([320, 390, 1440].includes(width) && ['', 'contact/'].includes(route)) {
        await page.screenshot({ path: `audit/feedback-2026/${route ? 'contact' : 'home'}-${width}.png` });
      }
    }
  }
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('http://127.0.0.1:4173/');
  await page.getByRole('button', { name: 'Menu', exact: true }).click();
  await page.locator('#mobile-nav').getByRole('link', { name: 'Horeca & contact' }).click();
  if (!page.url().endsWith('/contact/')) issues.push('Mobile contact navigation failed');
  for (const asset of ['short', 'long']) {
    const response = await page.request.get(`http://127.0.0.1:4173/assets/pimento-presentation-${asset}-june-2026.pdf`);
    if (response.status() !== 200 || !response.headers()['content-type'].includes('pdf')) issues.push(`Missing ${asset} presentation`);
  }
  fs.writeFileSync('audit/feedback-2026/results.json', JSON.stringify({ issues, checks }, null, 2));
  console.log(JSON.stringify({ pagesChecked: checks.length, issues }));
  await browser.close();
  if (issues.length) process.exitCode = 1;
})().catch(error => { console.error(error); process.exitCode = 1; });
