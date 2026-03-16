/* global WebImporter */

/**
 * Parser for tabs-showcase block
 *
 * Source: https://wknd-trendsetters.site
 * Base Block: tabs
 *
 * Block Structure:
 * - Row 1: Block name header
 * - Rows 2-N: [Tab Label | Heading + Image]
 *
 * Source HTML Pattern:
 * <div class="tabs-menu">
 *   <a class="tab-link">Tab Label</a>
 * </div>
 * <div class="tabs-content">
 *   <div class="tab-pane">
 *     <h2>Heading</h2>
 *     <img src="..." alt="...">
 *   </div>
 * </div>
 *
 * Generated: 2026-01-08
 */
export default function parse(element, { document }) {
  // Extract tab labels
  // VALIDATED: Found .tabs-menu and .tab-link in captured HTML
  const tabLinks = Array.from(element.querySelectorAll('.tabs-menu a, .tab-link, [class*="tab-link"]'));

  // Extract tab content panels
  const tabPanes = Array.from(element.querySelectorAll('.tabs-content > div, .tab-pane, [class*="tab-pane"]'));

  // Build cells array - one row per tab
  const cells = [];

  tabLinks.forEach((tab, index) => {
    const label = tab.textContent.trim();
    const pane = tabPanes[index];

    if (pane) {
      // Extract heading from tab pane
      const heading = pane.querySelector('h2, .h2-heading, [class*="heading"]');

      // Extract image from tab pane
      const image = pane.querySelector('img');

      // Build content column
      const contentColumn = [];
      if (heading) contentColumn.push(heading);
      if (image) contentColumn.push(image);

      cells.push([label, contentColumn]);
    } else {
      cells.push([label, '']);
    }
  });

  // Create block using WebImporter utility
  const block = WebImporter.Blocks.createBlock(document, { name: 'Tabs-Showcase', cells });

  // Replace original element with structured block table
  element.replaceWith(block);
}
