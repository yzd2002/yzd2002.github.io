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
    document.getElementById('plate-number').textContent = 'FIG. 0' + (Number(chosen) + 1) + ' / 03';
  });
}

const filters = document.querySelector('.filters');
if (filters) {
  const search = document.getElementById('search');
  const buttons = Array.from(filters.querySelectorAll('[data-filter]'));
  const records = Array.from(document.querySelectorAll('.paper'));
  const normalize = text => text.toLocaleLowerCase().replace(/[‐‑–—]/g, '-').trim();
  const entries = records.map(node => ({ node, text: normalize(node.textContent) }));
  let category = 'all';
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
