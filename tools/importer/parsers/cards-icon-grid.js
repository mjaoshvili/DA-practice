/* global WebImporter */

/**
 * Parser for cards-icon-grid block
 *
 * Source: https://wknd-trendsetters.site
 * Base Block: cards
 *
 * Block Structure:
 * - Row 1: Block name header
 * - Rows 2-N: [Text content per card]
 *
 * Source HTML Pattern:
 * <div class="w-layout-grid desktop-4-column">
 *   <div class="icon-card-item">
 *     <div class="icon">...</div>
 *     <p>Description text</p>
 *   </div>
 *   ...
 * </div>
 *
 * Generated: 2026-01-08
 */
export default function parse(element, { document }) {
  // Extract all card items
  // VALIDATED: Found grid items in .w-layout-grid.desktop-4-column
  const cardItems = Array.from(element.querySelectorAll(':scope > div, .icon-card-item, [class*="card-item"]'));

  // Build cells array - one row per card
  const cells = [];

  cardItems.forEach((item) => {
    // Get text content from each card
    const paragraph = item.querySelector('p, .paragraph, [class*="text"]');
    if (paragraph) {
      cells.push([paragraph.textContent.trim()]);
    }
  });

  // Create block using WebImporter utility
  const block = WebImporter.Blocks.createBlock(document, { name: 'Cards-Icon-Grid', cells });

  // Replace original element with structured block table
  element.replaceWith(block);
}
