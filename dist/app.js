document.documentElement.classList.add('js');
const menuButton=document.querySelector('.menu-button');
const mobileNav=document.querySelector('.mobile-nav');
function closeMenu(){menuButton?.setAttribute('aria-expanded','false');mobileNav?.classList.remove('open');}
menuButton?.addEventListener('click',()=>{const open=menuButton.getAttribute('aria-expanded')!=='true';menuButton.setAttribute('aria-expanded',String(open));mobileNav.classList.toggle('open',open)});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menuButton?.getAttribute('aria-expanded')==='true'){closeMenu();menuButton.focus()}});
mobileNav?.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu()});
if(!matchMedia('(prefers-reduced-motion: reduce)').matches&&'IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.remove('pending');observer.unobserve(entry.target)}}),{threshold:.08});document.querySelectorAll('.reveal').forEach(el=>{el.classList.add('pending');observer.observe(el)})}
const search=document.querySelector('#recipe-search');
const filterButtons=[...document.querySelectorAll('[data-filter]')];
const recipeCards=[...document.querySelectorAll('#recipe-grid .recipe-card')];
const normalise=value=>value.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
let category='Alles';
function filterRecipes(updateURL=true){
  const query=normalise(search?.value.trim()||'');let count=0;
  recipeCards.forEach(card=>{const matches=(category==='Alles'||card.dataset.categories.split('|').includes(category))&&normalise(card.dataset.search).includes(query);card.hidden=!matches;if(matches)count++});
  filterButtons.forEach(button=>{const active=button.dataset.filter===category;button.classList.toggle('active',active);button.setAttribute('aria-pressed',String(active))});
  document.querySelector('#result-count').textContent=`${count} ${count===1?'recept of mixidee':'recepten & mixideeën'}`;
  document.querySelector('#no-results').hidden=count!==0;
  if(updateURL){const url=new URL(location.href);category==='Alles'?url.searchParams.delete('categorie'):url.searchParams.set('categorie',category);search.value.trim()?url.searchParams.set('zoek',search.value.trim()):url.searchParams.delete('zoek');history.replaceState(null,'',url)}
}
if(search){
  const params=new URLSearchParams(location.search);const initial=params.get('categorie');
  if(filterButtons.some(button=>button.dataset.filter===initial))category=initial;
  search.value=params.get('zoek')||'';filterRecipes(false);
  search.addEventListener('input',()=>filterRecipes());
  filterButtons.forEach(button=>button.addEventListener('click',()=>{category=button.dataset.filter;filterRecipes()}));
  document.querySelector('#reset-filters').addEventListener('click',()=>{category='Alles';search.value='';filterRecipes();search.focus()});
}
document.querySelector('.print-recipe')?.addEventListener('click',()=>window.print());
document.querySelector('#contact-form')?.addEventListener('submit',event=>{
  event.preventDefault();const form=event.currentTarget;if(!form.reportValidity())return;
  const values=new FormData(form);
  const subject=`Pimento — ${values.get('subject')}`;
  const body=`Naam: ${values.get('name')}\nE-mail: ${values.get('email')}\nBedrijf: ${values.get('business')||'—'}\n\n${values.get('message')}`;
  const link=`mailto:info@real-est-dranken.nl?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  const fallback=form.querySelector('.mail-fallback');fallback.href=link;fallback.hidden=false;
  const status=form.querySelector('.form-status');status.textContent='Je e-mailconcept is klaar. Verstuur het vanuit je e-mailprogramma. Opent er niets? Mail dan rechtstreeks naar info@real-est-dranken.nl; je tekst blijft hier staan.';status.hidden=false;
  location.href=link;
});
