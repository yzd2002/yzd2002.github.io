'use strict';

const page = document.documentElement;
page.classList.add('interactive');

const atlasButtons = Array.from(document.querySelectorAll('[data-plate]'));
for (const button of atlasButtons) {
  button.addEventListener('click', () => {
    const chosen = button.dataset.plate;
    for (const item of atlasButtons) {
      item.setAttribute('aria-pressed', String(item === button));
    }
    for (const slide of document.querySelectorAll('[data-slide]')) {
      slide.hidden = slide.dataset.slide !== chosen;
    }
    if (chosen !== '2') document.querySelector('.film video')?.pause();
  });
}

for (const button of document.querySelectorAll('[data-change]')) {
  button.addEventListener('click', () => {
    const study = button.closest('.study');
    const alternate = study.dataset.state === 'initial';
    study.dataset.state = alternate ? 'alternate' : 'initial';
    study.querySelector('[data-changing] strong').textContent = alternate ? study.dataset.alternate : study.dataset.initial;
    study.querySelector('.readout b').textContent = alternate ? study.dataset.claimB : study.dataset.claimA;
    button.textContent = alternate ? study.dataset.restore : study.dataset.toggle;
  });
}

function showLinkedFilm() {
  if (location.hash === '#robot-demo') atlasButtons[2]?.click();
}
showLinkedFilm();
window.addEventListener('hashchange', showLinkedFilm);
document.querySelector('a.cover.footage')?.addEventListener('click', () => atlasButtons[2]?.click());

for (const button of document.querySelectorAll('.copy-citation')) {
  button.hidden = false;
  button.addEventListener('click', async () => {
    const citation = button.closest('details');
    const text = citation.querySelector('pre');
    const feedback = citation.querySelector('.feedback');
    try {
      await navigator.clipboard.writeText(text.textContent);
      feedback.textContent = page.lang === 'en' ? 'Copied.' : '已复制。';
    } catch {
      const selection = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents(text);
      selection.removeAllRanges();
      selection.addRange(range);
      feedback.textContent = page.lang === 'en' ? 'Text selected. Use your copy command.' : '已选中引用文本，可直接复制。';
    }
  });
}

const filters = document.querySelector('.filters');
if (filters) {
  const search = document.getElementById('search');
  const buttons = Array.from(filters.querySelectorAll('[data-filter]'));
  const records = Array.from(document.querySelectorAll('.paper'));
  const normalize = text => text.toLocaleLowerCase().replace(/[‐‑–—]/g, '-').trim();
  const entries = records.map(node => ({ node, text: normalize(node.textContent) }));
  const initial = new URLSearchParams(location.search);
  let category = buttons.some(button => button.dataset.filter === initial.get('type')) ? initial.get('type') : 'all';
  search.value = initial.get('q') || '';
  const print = document.getElementById('print-index');
  print.hidden = false;
  print.addEventListener('click', () => window.print());
  function update() {
    const terms = normalize(search.value).split(/\s+/).filter(Boolean);
    let count = 0;
    for (const { node, text } of entries) {
      const match = (category === 'all' || node.dataset.cat === category) && terms.every(term => text.includes(term));
      node.hidden = !match;
      if (match) count++;
    }
    for (const button of buttons) {
      button.setAttribute('aria-pressed', String(button.dataset.filter === category));
    }
    document.getElementById('matches').textContent = page.lang === 'en'
      ? count + (count === 1 ? ' record' : ' records') : '共 ' + count + ' 项成果';
    document.getElementById('empty').hidden = count > 0;
    const url = new URL(location.href);
    if (category === 'all') url.searchParams.delete('type');
    else url.searchParams.set('type', category);
    if (search.value.trim()) url.searchParams.set('q', search.value.trim());
    else url.searchParams.delete('q');
    if (location.href !== url.href) history.replaceState(null, '', url);
    const languageLink = document.querySelector('.lang');
    const translation = new URL(languageLink.href);
    translation.search = url.search;
    translation.hash = url.hash;
    languageLink.href = translation.href;
  }
  for (const button of buttons) {
    button.addEventListener('click', () => { category = button.dataset.filter; update(); });
  }
  search.addEventListener('input', update);
  window.addEventListener('hashchange', () => {
    const target = document.getElementById(location.hash.slice(1));
    if (target && target.classList.contains('paper') && target.hidden) {
      search.value = '';
      category = 'all';
      update();
      target.scrollIntoView();
    }
  });
  filters.hidden = false;
  update();
}
