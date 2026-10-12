import { useEffect } from 'react';
import './ClickPush.css';

// A small "push()" tag that floats up from whatever button was clicked, like
// a frame going onto the call stack. Elements can name their own call with
// data-push: the section dots use it to read push(experience) and so on.
//
// One listener on the document rather than a wrapper on every button, so it
// covers buttons anywhere on the site without touching them.

const SELECTOR = '[data-push], button, .action-button';
const LIFETIME_MS = 900;

const ClickPush = () => {
  useEffect(() => {
    const onClick = (event: MouseEvent) => {
      const target = (event.target as Element | null)?.closest?.<HTMLElement>(SELECTOR);
      if (!target) return;

      // Keyboard activation reports no pointer position (detail is 0), so
      // start from the top of the element instead.
      let x = event.clientX;
      let y = event.clientY;
      if (event.detail === 0) {
        const rect = target.getBoundingClientRect();
        x = rect.left + rect.width / 2;
        y = rect.top;
      }

      const tag = document.createElement('span');
      tag.className = 'click-push';
      tag.setAttribute('aria-hidden', 'true');
      tag.textContent = target.dataset.push ? `push(${target.dataset.push})` : 'push()';
      tag.style.left = `${x}px`;
      tag.style.top = `${y}px`;
      document.body.appendChild(tag);
      window.setTimeout(() => tag.remove(), LIFETIME_MS);
    };

    // Capture phase: some buttons (the music player's mini control) stop
    // propagation, and would otherwise never reach a bubbling listener.
    document.addEventListener('click', onClick, true);
    return () => document.removeEventListener('click', onClick, true);
  }, []);

  return null;
};

export default ClickPush;
