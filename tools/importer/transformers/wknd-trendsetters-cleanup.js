/* global WebImporter */

/**
 * Transformer for WKND Trendsetters website cleanup
 * Purpose: Remove navigation, footer, and non-content elements
 * Applies to: wknd-trendsetters.site (all pages)
 * Generated: 2026-01-08
 *
 * SELECTORS EXTRACTED FROM:
 * - Captured DOM during migration workflow (cleaned.html)
 */

const TransformHook = {
  beforeTransform: 'beforeTransform',
  afterTransform: 'afterTransform'
};

export default function transform(hookName, element, payload) {
  if (hookName === TransformHook.beforeTransform) {
    // Remove navigation elements
    // EXTRACTED: Found <div class="nav secondary-nav"> in captured HTML
    WebImporter.DOMUtils.remove(element, [
      '.nav.secondary-nav',
      '.nav-container',
      '.w-nav',
      '.w-nav-menu'
    ]);

    // Remove footer elements
    // EXTRACTED: Found footer section in captured HTML
    WebImporter.DOMUtils.remove(element, [
      'footer',
      '.footer',
      '.footer-section'
    ]);

    // Remove dropdown menus
    // EXTRACTED: Found .w-dropdown elements in navigation
    WebImporter.DOMUtils.remove(element, [
      '.w-dropdown',
      '.w-dropdown-list',
      '.mega-nav-dropdown-list-wrapper'
    ]);
  }

  if (hookName === TransformHook.afterTransform) {
    // Clean up remaining unwanted elements
    WebImporter.DOMUtils.remove(element, [
      'noscript',
      'link',
      'source'
    ]);

    // Remove tracking attributes
    const allElements = element.querySelectorAll('*');
    allElements.forEach(el => {
      el.removeAttribute('data-w-id');
      el.removeAttribute('data-wf-domain');
    });
  }
}
