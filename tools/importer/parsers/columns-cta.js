/* global WebImporter */

/**
 * Parser for columns-cta block
 *
 * Source: https://wknd-trendsetters.site
 * Base Block: columns
 *
 * Block Structure:
 * - Row 1: Block name header
 * - Row 2: [Heading + Paragraph | Buttons]
 *
 * Source HTML Pattern:
 * <div class="flex-horizontal">
 *   <div>
 *     <h2>Heading</h2>
 *     <p>Description</p>
 *   </div>
 *   <div>
 *     <a class="button">Sign up</a>
 *     <a class="button">Connect</a>
 *   </div>
 * </div>
 *
 * Generated: 2026-01-08
 */
export default function parse(element, { document }) {
  // Extract heading and paragraph
  // VALIDATED: Found h2.h2-heading and p in captured HTML
  const heading = element.querySelector('h2, .h2-heading, [class*="heading"]');
  const paragraph = element.querySelector('p, .subheading, [class*="description"]');

  // Extract CTA buttons
  // VALIDATED: Found a.button elements in captured HTML
  const buttons = Array.from(element.querySelectorAll('a.button, a.w-button, .button-group a'));

  // Build cells array - text on left, buttons on right
  const cells = [];

  const leftColumn = [];
  if (heading) leftColumn.push(heading);
  if (paragraph) leftColumn.push(paragraph);

  const rightColumn = [...buttons];

  cells.push([leftColumn, rightColumn]);

  // Create block using WebImporter utility
  const block = WebImporter.Blocks.createBlock(document, { name: 'Columns-CTA', cells });

  // Replace original element with structured block table
  element.replaceWith(block);
}
