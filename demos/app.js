'use strict';

// Read the cards so the random recommendation always matches the visible collection.
const cards = Array.from(document.querySelectorAll('[data-game]'));
const dialog = document.querySelector('#pick-dialog');
const randomButton = document.querySelector('#random-game');
let previousPick = -1;

function pickGame() {
  const choices = cards.map((card, index) => ({ card, index }))
    .filter(({ index }) => cards.length === 1 || index !== previousPick);
  const { card, index } = choices[Math.floor(Math.random() * choices.length)];
  previousPick = index;
  document.querySelector('#pick-title').textContent = card.querySelector('h3').firstChild.textContent;
  document.querySelector('#pick-description').textContent = card.querySelector('.game-description').textContent;
  document.querySelector('#pick-link').href = card.querySelector('.play-link').href;
}

if (cards.length && typeof dialog.showModal === 'function') {
  randomButton.hidden = false;
  randomButton.addEventListener('click', () => {
    pickGame();
    dialog.showModal();
  });
  document.querySelector('#pick-again').addEventListener('click', pickGame);
  document.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', (event) => {
    if (event.target !== dialog) return;
    const bounds = dialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right ||
        event.clientY < bounds.top || event.clientY > bounds.bottom) dialog.close();
  });
}
