/* global WebImporter */

/**
 * Parser for cards-article block
 *
 * Source: https://wknd-trendsetters.site
 * Base Block: cards
 *
 * Block Structure:
 * - Row 1: Block name header
 * - Rows 2-N: [Image | Tag + Heading + Description + Link]
 *
 * Source HTML Pattern:
 * <a class="card-link">
 *   <div class="card-image"><img src="..." alt="..."></div>
 *   <div class="card-body">
 *     <div class="tag">Category</div>
 *     <div class="read-time">3 min read</div>
 *     <h3>Heading</h3>
 *     <p>Description</p>
 *   </div>
 * </a>
 *
 * Generated: 2026-01-08
 */
export default function parse(element, { document }) {
  // Extract all article cards
  // VALIDATED: Found .card-link elements in captured HTML
  const cards = Array.from(element.querySelectorAll('.card-link, a[class*="card"]'));

  // Build cells array - one row per card with image and content
  const cells = [];

  cards.forEach((card) => {
    // Extract image
    const image = card.querySelector('img');

    // Extract tag/category
    const tag = card.querySelector('.tag, .eyebrow, [class*="tag"]');

    // Extract read time
    const readTime = card.querySelector('.read-time, [class*="read-time"], .paragraph-sm');

    // Extract heading
    const heading = card.querySelector('h3, .h3-heading, [class*="heading"]');

    // Extract description
    const description = card.querySelector('p:not(.paragraph-sm), .description, .card-body > p');

    // Build content column
    const contentColumn = [];
    if (tag) contentColumn.push(tag.textContent.trim());
    if (readTime) contentColumn.push(readTime.textContent.trim());
    if (heading) contentColumn.push(heading);
    if (description) contentColumn.push(description);

    // Get link href
    const href = card.getAttribute('href') || '#';
    const link = document.createElement('a');
    link.href = href;
    link.textContent = 'Read';
    contentColumn.push(link);

    // Add row with image and content
    if (image) {
      cells.push([image, contentColumn]);
    } else {
      cells.push([contentColumn]);
    }
  });

  // Create block using WebImporter utility
  const block = WebImporter.Blocks.createBlock(document, { name: 'Cards-Article', cells });

  // Replace original element with structured block table
  element.replaceWith(block);
}
