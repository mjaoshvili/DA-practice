/* global WebImporter */

/**
 * Parser for columns-media block
 *
 * Source: https://wknd-trendsetters.site
 * Base Block: columns
 *
 * Block Structure:
 * - Row 1: Block name header
 * - Row 2: [Image 1 | Image 2]
 *
 * Source HTML Pattern:
 * <div class="w-layout-grid grid-layout desktop-2-column">
 *   <div><img src="..." alt="..."></div>
 *   <div><img src="..." alt="..."></div>
 * </div>
 *
 * Generated: 2026-01-08
 */
export default function parse(element, { document }) {
  // Extract images from the grid layout
  // VALIDATED: Found in captured HTML with .w-layout-grid.desktop-2-column
  const images = Array.from(element.querySelectorAll('img'));

  // Build cells array - two images side by side
  const cells = [];

  if (images.length >= 2) {
    cells.push([images[0], images[1]]);
  } else if (images.length === 1) {
    cells.push([images[0]]);
  }

  // Create block using WebImporter utility
  const block = WebImporter.Blocks.createBlock(document, { name: 'Columns-Media', cells });

  // Replace original element with structured block table
  element.replaceWith(block);
}
