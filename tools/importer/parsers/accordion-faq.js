/* global WebImporter */

/**
 * Parser for accordion-faq block
 *
 * Source: https://wknd-trendsetters.site
 * Base Block: accordion
 *
 * Block Structure:
 * - Row 1: Block name header
 * - Rows 2-N: [Question | Answer]
 *
 * Source HTML Pattern:
 * <div class="faq-accordion">
 *   <div class="accordion-item">
 *     <div class="accordion-trigger">Question text</div>
 *     <div class="accordion-content">Answer text</div>
 *   </div>
 * </div>
 *
 * Generated: 2026-01-08
 */
export default function parse(element, { document }) {
  // Extract all FAQ items
  // VALIDATED: Found accordion structure in captured HTML
  const faqItems = Array.from(element.querySelectorAll(
    '.accordion-item, .faq-item, details, [class*="accordion-item"]'
  ));

  // Build cells array - one row per FAQ item
  const cells = [];

  faqItems.forEach((item) => {
    // Extract question (trigger/summary)
    const question = item.querySelector(
      '.accordion-trigger, .faq-question, summary, [class*="trigger"], [class*="question"]'
    );

    // Extract answer (content/details body)
    const answer = item.querySelector(
      '.accordion-content, .faq-answer, [class*="content"]:not([class*="trigger"]), [class*="answer"]'
    );

    if (question) {
      const questionText = question.textContent.trim();
      const answerText = answer ? answer.textContent.trim() : '';

      cells.push([questionText, answerText]);
    }
  });

  // Create block using WebImporter utility
  const block = WebImporter.Blocks.createBlock(document, { name: 'Accordion-FAQ', cells });

  // Replace original element with structured block table
  element.replaceWith(block);
}
