import json

# Master collection of ALL discovered URLs
all_urls = set()

# ============================================
# PASS 1: From services.html (first crawl)
# ============================================
services_links = [
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply.html",
  "https://www.thermofisher.com/us/en/home/applications-techniques.html",
  "https://www.thermofisher.com/us/en/home/bioprocessing.html",
  "https://www.thermofisher.com/us/en/home/biotech.html",
  "https://www.thermofisher.com/us/en/home/brands/applied-biosystems.html",
  "https://www.thermofisher.com/us/en/home/brands/fisher-scientific.html",
  "https://www.thermofisher.com/us/en/home/brands/gibco.html",
  "https://www.thermofisher.com/us/en/home/brands/invitrogen.html",
  "https://www.thermofisher.com/us/en/home/brands/ion-torrent.html",
  "https://www.thermofisher.com/us/en/home/brands/patheon.html",
  "https://www.thermofisher.com/us/en/home/brands/ppd.html",
  "https://www.thermofisher.com/us/en/home/brands/thermo-scientific.html",
  "https://www.thermofisher.com/us/en/home/chemicals.html",
  "https://www.thermofisher.com/us/en/home/clinical/cell-gene-therapy.html",
  "https://www.thermofisher.com/us/en/home/clinical/clinical-genomics.html",
  "https://www.thermofisher.com/us/en/home/communities-social/socialhub.html",
  "https://www.thermofisher.com/us/en/home/digital-solutions.html",
  "https://www.thermofisher.com/us/en/home/digital-solutions/ecommerce/b2b.html",
  "https://www.thermofisher.com/us/en/home/digital-solutions/lab-informatics.html",
  "https://www.thermofisher.com/us/en/home/electron-microscopy.html",
  "https://www.thermofisher.com/us/en/home/events.html",
  "https://www.thermofisher.com/us/en/home/global/online-pricing-policy.html",
  "https://www.thermofisher.com/us/en/home/global/policies-notices.html",
  "https://www.thermofisher.com/us/en/home/global/privacy-policy.html",
  "https://www.thermofisher.com/us/en/home/global/terms-and-conditions.html",
  "https://www.thermofisher.com/us/en/home/global/trademark-information.html",
  "https://www.thermofisher.com/us/en/home/industrial.html",
  "https://www.thermofisher.com/us/en/home/industrial/animal-health.html",
  "https://www.thermofisher.com/us/en/home/industrial/battery.html",
  "https://www.thermofisher.com/us/en/home/industrial/cement-coal-minerals.html",
  "https://www.thermofisher.com/us/en/home/industrial/chromatography.html",
  "https://www.thermofisher.com/us/en/home/industrial/environmental.html",
  "https://www.thermofisher.com/us/en/home/industrial/food-beverage.html",
  "https://www.thermofisher.com/us/en/home/industrial/forensics.html",
  "https://www.thermofisher.com/us/en/home/industrial/manufacturing-processing.html",
  "https://www.thermofisher.com/us/en/home/industrial/mass-spectrometry.html",
  "https://www.thermofisher.com/us/en/home/industrial/microbiology.html",
  "https://www.thermofisher.com/us/en/home/industrial/pharma-biopharma.html",
  "https://www.thermofisher.com/us/en/home/industrial/pharma-biopharma/drug-discovery-development.html",
  "https://www.thermofisher.com/us/en/home/industrial/radiation-detection-measurement.html",
  "https://www.thermofisher.com/us/en/home/industrial/safety-security-threat-detection.html",
  "https://www.thermofisher.com/us/en/home/industrial/solutions-cdmos.html",
  "https://www.thermofisher.com/us/en/home/industrial/spectroscopy-elemental-isotope-analysis.html",
  "https://www.thermofisher.com/us/en/home/industrial/spectroscopy-elemental-isotope-analysis/geosciences.html",
  "https://www.thermofisher.com/us/en/home/industrial/spectroscopy-elemental-isotope-analysis/materials-science-research.html",
  "https://www.thermofisher.com/us/en/home/industrial/spectroscopy-elemental-isotope-analysis/materials-science-research/polymer-analysis.html",
  "https://www.thermofisher.com/us/en/home/lab-solutions/solutions-diagnostics-labs.html",
  "https://www.thermofisher.com/us/en/home/life-science/agricultural-biotechnology/agrigenomics.html",
  "https://www.thermofisher.com/us/en/home/life-science/antibodies.html",
  "https://www.thermofisher.com/us/en/home/life-science/bioproduction.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/cell-culture-plastics.html",
  "https://www.thermofisher.com/us/en/home/life-science/cloning/gene-synthesis/geneart-gene-synthesis.html",
  "https://www.thermofisher.com/us/en/home/life-science/dna-rna-purification-analysis.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-plasticware-supplies.html",
  "https://www.thermofisher.com/us/en/home/life-science/oligonucleotides-primers-probes-genes.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/real-time-pcr/real-time-pcr-assays.html",
  "https://www.thermofisher.com/us/en/home/o/b/no-interest-financing-offer.html",
  "https://www.thermofisher.com/us/en/home/order.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/aspire-member-program.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/promotions.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/crdmo.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/custom-services.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/financial-leasing-services.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/instrument-qualification-services.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/training-services.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/unity-lab-services.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/supply-center.html",
  "https://www.thermofisher.com/us/en/home/semiconductors.html",
  "https://www.thermofisher.com/us/en/home/support.html",
  "https://www.thermofisher.com/us/en/home/support/documents-certificates.html",
  "https://www.thermofisher.com/us/en/home/support/how-to-place-orders.html",
  "https://www.thermofisher.com/us/en/home/support/how-to-register-for-account.html",
  "https://www.thermofisher.com/us/en/home/sustainable-design.html",
  "https://www.thermofisher.com/us/en/home/technical-resources/contact-us.html",
  "https://www.thermofisher.com/us/en/home/technical-resources/instrument-support.html",
  "https://www.thermofisher.com/us/en/home/technical-resources/learning-centers.html",
  "https://www.thermofisher.com/us/en/home/technical-resources/technical-reference-library.html",
]
all_urls.update(services_links)

# From promotions.html
promotions_extra = [
  "https://www.thermofisher.com/us/en/home/global/forms/life-science/tetra-core-trial-kit.html",
  "https://www.thermofisher.com/us/en/home/o/a/benchtop-instruments.html",
  "https://www.thermofisher.com/us/en/home/o/a/cepa-promo.html",
  "https://www.thermofisher.com/us/en/home/o/a/cultured-solutions.html",
  "https://www.thermofisher.com/us/en/home/o/a/geneart-services-promo.html",
  "https://www.thermofisher.com/us/en/home/o/b/antibody-development-promo.html",
  "https://www.thermofisher.com/us/en/home/o/b/cells-to-ct-promo.html",
  "https://www.thermofisher.com/us/en/home/o/b/gene-expression-promo.html",
  "https://www.thermofisher.com/us/en/home/o/b/heartofeverylab.html",
  "https://www.thermofisher.com/us/en/home/o/b/plasticware-bundle.html",
  "https://www.thermofisher.com/us/en/home/o/c/more-savings-more-discover.html",
  "https://www.thermofisher.com/us/en/home/o/c/neuronal-research-products-promo.html",
  "https://www.thermofisher.com/us/en/home/o/c/protein-biology-essentials-promo.html",
  "https://www.thermofisher.com/us/en/home/o/c/protein-purification-promo.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/promotions/jump-start-biotech-new-lab-program.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/promotions/novex-product-promotions.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/promotions/sciencesavings.html",
]
all_urls.update(promotions_extra)

# From supply-center.html (redirected to PCR page)
supply_extra = [
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/life-science-tools.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/molecular-diagnostics-commercial-suppy.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/molecular-diagnostics-commercial-suppy/real-time-pcr/plastics-prototyping-services.html",
  "https://www.thermofisher.com/us/en/home/brands/invitrogen/molecular-biology-technologies.html",
  "https://www.thermofisher.com/us/en/home/brands/invitrogen/molecular-biology-technologies/pcr-literature-resource-library.html",
  "https://www.thermofisher.com/us/en/home/brands/thermo-scientific/molecular-biology/thermo-scientific-pcr.html",
  "https://www.thermofisher.com/us/en/home/global/forms/life-science/request-pcr-instrument-plastics-services-guide/thank-you.html",
  "https://www.thermofisher.com/us/en/home/global/forms/mol-bio-handbook-download-request-form.html",
  "https://www.thermofisher.com/us/en/home/life-science.html",
  "https://www.thermofisher.com/us/en/home/life-science/dna-rna-purification-analysis/nucleic-acid-gel-electrophoresis.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/lab-centrifuges/mini-microcentrifuges.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-plasticware-supplies/pipettes-pipette-tips.html",
  "https://www.thermofisher.com/us/en/home/life-science/oligonucleotides-primers-probes-genes/custom-dna-oligos.html",
  "https://www.thermofisher.com/us/en/home/life-science/oligonucleotides-primers-probes-genes/custom-dna-oligos/oligo-design-tools/oligoperfect.html",
  "https://www.thermofisher.com/us/en/home/life-science/oligonucleotides-primers-probes-genes/nucleotides.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/5-steps-pcr.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/digital-pcr.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/isothermal-nucleic-acid-amplification.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/pcr-enzymes-master-mixes.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/pcr-enzymes-master-mixes/platinum-high-fidelity-pcr-enzyme.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/pcr-enzymes-master-mixes/platinum-hot-start-pcr-enzyme.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/pcr-learning-center.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/pcr-plastics.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/pcr-plastics/applied-biosystems-microamp-8-tube-strips-attached-caps.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/pcr-plastics/microamp-triflex-3x32-plates-adhesive-film.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/pcr-plastics/plastics-selection-guide.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/real-time-pcr.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/reverse-transcription.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/reverse-transcription/superscript-cellsdirect.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/reverse-transcription/superscript-iv-reverse-transcriptase.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/reverse-transcription/superscript-iv-vilo-master-mix.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/rt-lamp-master-mix-isothermal-amplification.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/thermal-cyclers-realtime-instruments/thermal-cyclers.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/thermal-cyclers-realtime-instruments/thermal-cyclers/proflex-pcr-system.html",
  "https://www.thermofisher.com/us/en/home/life-science/pcr/thermal-cyclers-realtime-instruments/thermal-cyclers/simpliamp-thermal-cycler.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/promotions/life-science/everyday-essentials/pcr.html",
  "https://www.thermofisher.com/us/en/home/technical-resources/technical-reference-library/pcr-cdna-synthesis-support-center.html",
]
all_urls.update(supply_extra)

# From aspire-member-program.html (redirected to cell-culture.html)
aspire_extra = [
  "https://www.thermofisher.com/us/en/home/global/forms/opt-in-sms-text-updates.html",
  "https://www.thermofisher.com/us/en/home/life-science/bioproduction/single-use-bioprocessing.html",
  "https://www.thermofisher.com/us/en/home/life-science/bioproduction/single-use-bioprocessing/adherent-cell-culture-solutions.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-analysis.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-analysis/cell-analysis-instruments/automated-cell-counters.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-analysis/cellular-imaging/evos-cell-imaging-systems.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/cell-counting-viability-cryopreservation.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/cell-culture-learning-center.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/cell-culture-plastics/cell-culture-dishes-multidishes.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/cell-culture-plastics/cell-culture-flasks.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/cell-culture-plastics/cell-culture-plates.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/cell-culture-plastics/chamber-slides-coverglass.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/cell-culture-plastics/chamber-slides-coverglass/chamber-slides.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/instruments-cell-culture-room.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/mammalian-cell-culture.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/mammalian-cell-culture/cancer-cell-culture.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/mammalian-cell-culture/cell-culture-media.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/mammalian-cell-culture/fbs.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/mammalian-cell-culture/reagents.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/mammalian-cell-culture/recombinant-proteins.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/mammalian-cell-culture/recombinant-proteins/growth-factors.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/microbiological-culture.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/neuronal-cell-culture.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/organoids-spheroids-3d-cell-culture.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/organoids-spheroids-3d-cell-culture/extracellular-matrices-ecm.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/primary-cell-culture.html",
  "https://www.thermofisher.com/us/en/home/life-science/cell-culture/transfection.html",
  "https://www.thermofisher.com/us/en/home/life-science/genome-editing.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/biological-safety-cabinets.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/co2-incubators.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/cold-storage/cryopreservation-systems-accessories.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/cold-storage/ult-freezers.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/lab-centrifuges/benchtop-centrifuges.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/lab-centrifuges/benchtop-centrifuges/models.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/liquid-handling.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/ph-electrochemistry/ph-measurement-testing.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/water-baths-circulators-chillers/water-baths.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/water-purification-systems.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-equipment/water-purification-systems/models.html",
  "https://www.thermofisher.com/us/en/home/life-science/lab-plasticware-supplies/filtration.html",
  "https://www.thermofisher.com/us/en/home/life-science/protein-biology/protein-expression.html",
  "https://www.thermofisher.com/us/en/home/life-science/sample-storage-management/sample-storage-tubes.html",
  "https://www.thermofisher.com/us/en/home/life-science/stem-cell-research/stem-cell-culture.html",
  "https://www.thermofisher.com/us/en/home/references/gibco-cell-culture-basics.html",
  "https://www.thermofisher.com/us/en/home/references/gibco-cell-culture-basics/introduction-to-cell-culture.html",
  "https://www.thermofisher.com/us/en/home/references/protocols.html",
  "https://www.thermofisher.com/us/en/home/technical-resources/cell-lines.html",
  "https://www.thermofisher.com/us/en/home/technical-resources/technical-reference-library/cell-culture-support-center.html",
  "https://www.thermofisher.com/us/en/home/technical-resources/technical-reference-library/cell-culture-transfection-support-centers.html",
]
all_urls.update(aspire_extra)

# From global section pages
global_extra = [
  "https://www.thermofisher.com/us/en/home/technical-resources/declarations-conformity.html",
  "https://www.thermofisher.com/us/en/home/technical-resources/knowledgebase-faqs.html",
  "https://www.thermofisher.com/us/en/home/global/privacy-policy/cookie-policy.html",
  "https://www.thermofisher.com/us/en/home/global/privacy-policy/privacy-notice-for-us.html",
  "https://www.thermofisher.com/us/en/home/global/customer-privacy-notice.html",
  "https://www.thermofisher.com/us/en/home/global/policies-notices/accessibility.html",
  "https://www.thermofisher.com/us/en/home/global/policies-notices/copyright.html",
  "https://www.thermofisher.com/us/en/home/global/policies-notices/equal-opportunity.html",
  "https://www.thermofisher.com/us/en/home/global/policies-notices/linked-sites.html",
  "https://www.thermofisher.com/us/en/home/global/policies-notices/policies-on-trademarks.html",
  "https://www.thermofisher.com/us/en/home/global/policies-notices/pricing.html",
  "https://www.thermofisher.com/us/en/home/global/policies-notices/product-returns.html",
  "https://www.thermofisher.com/us/en/home/global/policies-notices/promotions.html",
  "https://www.thermofisher.com/us/en/home/global/policies-notices/terms-and-conditions-of-sale.html",
]
all_urls.update(global_extra)

# From about-us OEM page
aboutus_extra = [
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/agricultural-biotech-commercial-supply.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/animal-health-commercial-supply.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/food-environmental-testing-commercial-supply.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/forensic-human-identification-commercial-supply.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/life-science-tools.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/molecular-diagnostics-commercial-suppy.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/newborn-screening-commercial-supply.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/reproductive-health-commercial-supply.html",
]
all_urls.update(aboutus_extra)

# Starting URLs
starting_urls = [
  "https://www.thermofisher.com/us/en/home/products-and-services/services.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/promotions.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/supply-center.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/aspire-member-program.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/new-products.html",
  "https://www.thermofisher.com/us/en/home/global/terms-and-conditions.html",
  "https://www.thermofisher.com/us/en/home/global/privacy-policy.html",
  "https://www.thermofisher.com/us/en/home/global/policies-notices.html",
  "https://www.thermofisher.com/us/en/home/global/trademark-information.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply.html",
  "https://www.thermofisher.com/us/en/home/order.html",
  "https://www.thermofisher.com/us/en/home/events.html",
  "https://www.thermofisher.com/us/en/home/biotech.html",
  "https://www.thermofisher.com/us/en/home/bioprocessing.html",
  "https://www.thermofisher.com/us/en/home/chemicals.html",
  "https://www.thermofisher.com/us/en/home/sustainable-design.html",
  "https://www.thermofisher.com/us/en/home/applications-techniques.html",
  "https://www.thermofisher.com/us/en/home/communities-social/socialhub.html",
  "https://www.thermofisher.com/us/en/home/lab-solutions/solutions-diagnostics-labs.html",
  "https://www.thermofisher.com/us/en/home/o/c/neuronal-research-products-promo.html",
  "https://www.thermofisher.com/us/en/home/o/c/more-savings-more-discover.html",
  "https://www.thermofisher.com/us/en/home/o/b/gene-expression-promo.html",
]
all_urls.update(starting_urls)

# From second pass discoveries
second_pass = [
  "https://www.thermofisher.com/us/en/home/products-and-services/eprocurement/eprocurement-solutions-contact-form.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/services-central.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/promotions/invitrogen-vivofectamine-delivery-solutions.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/promotions/industrial/automated-workflow-solutions-gc-gc-ms.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/custom-services/assay-development-services.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/custom-services/molecular-biology-services.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/custom-services/molecular-biology-services/protein-production.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/custom-services/screening-and-profiling-services.html",
  "https://www.thermofisher.com/us/en/home/products-and-services/services/instrument-qualification-services/compliance-and-validation/analytical-validation-consulting-services-laboratory-assays.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/immunodiagnostics-commercial-suppy.html",
  "https://www.thermofisher.com/us/en/home/about-us/partnering-licensing/oem-commercial-supply/therapeutics-commercial-suppy.html",
  "https://www.thermofisher.com/us/en/home/c/b/lab-clearance-sale.html",
  "https://www.thermofisher.com/us/en/home/o/a/centrifuges-online-offers.html",
  "https://www.thermofisher.com/us/en/home/brands.html",
  "https://www.thermofisher.com/us/en/home/brands/unity-lab-services.html",
  "https://www.thermofisher.com/us/en/home/brands/onelambda.html",
  "https://www.thermofisher.com/us/en/home/brands/olink-proteomics-protein-biomarker-analysis.html",
  "https://www.thermofisher.com/us/en/home/brands/expanded-filtration-separation.html",
  "https://www.thermofisher.com/us/en/home/product-selection-guides-and-tools.html",
  "https://www.thermofisher.com/us/en/home/support/how-to-apply-promo-quote-codes.html",
  "https://www.thermofisher.com/us/en/home/support/how-to-check-order-status-track-shipments.html",
  "https://www.thermofisher.com/us/en/home/support/how-to-create-recurring-orders.html",
  "https://www.thermofisher.com/us/en/home/support/how-to-use-account-dashboard.html",
  "https://www.thermofisher.com/us/en/home/digital-solutions/ardia-platform.html",
  # global/forms discovered
  "https://www.thermofisher.com/us/en/home/global/forms/evos-imaging-system-quote-demo.html",
  "https://www.thermofisher.com/us/en/home/global/forms/imaging-protocols-handbook.html",
  "https://www.thermofisher.com/us/en/home/global/forms/lab-solutions/bulk-fine-chemicals.html",
  "https://www.thermofisher.com/us/en/home/global/forms/how-can-our-scientists-help-you.html",
  "https://www.thermofisher.com/us/en/home/global/forms/life-science/molecular-solutions.html",
  "https://www.thermofisher.com/us/en/home/global/forms/molecular-solutions/technologies-in-clinical-laboratories.html",
  "https://www.thermofisher.com/us/en/home/global/forms/top-6-sample-form.html",
  "https://www.thermofisher.com/us/en/home/global/forms/antibody-based-tools-neurodegenerative-disease-research.html",
  "https://www.thermofisher.com/us/en/home/global/forms/gibco-neurobiology-protocol-handbook-request.html",
  "https://www.thermofisher.com/us/en/home/global/forms/life-science/respiratory-testing-solutions.html",
  "https://www.thermofisher.com/us/en/home/global/forms/life-science/covid19-testing-solutions-webinars.html",
  "https://www.thermofisher.com/us/en/home/global/forms/life-science/pharmacogenomics-solutions-information-request.html",
  "https://www.thermofisher.com/us/en/home/global/forms/bioprocessing/cgmp-chemicals/supply-resiliency-volatility-webinar.html",
  "https://www.thermofisher.com/us/en/home/global/forms/bioprocessing/cgmp-chemicals/raw-material-planning-webinar.html",
  "https://www.thermofisher.com/us/en/home/global/forms/patient-tumoroids-scalable-3d-screening-webinar.html",
  "https://www.thermofisher.com/us/en/home/global/forms/high-content-imaging-system-quote.html",
  "https://www.thermofisher.com/us/en/home/global/forms/cell-painting-application-note.html",
  "https://www.thermofisher.com/us/en/home/global/forms/biotech-maintaining-quality-compliance-webinar.html",
  "https://www.thermofisher.com/us/en/home/global/forms/webinar-registration-cdmos-maximize-productivity-sensitivity.html",
  "https://www.thermofisher.com/us/en/home/global/forms/life-science/lab-equipment.html",
  "https://www.thermofisher.com/us/en/home/global/forms/industrial/dioxin-analysis-triple-quad-gc-ms-compliance-eu-regulations.html",
  "https://www.thermofisher.com/us/en/home/global/forms/industrial/volatile-relationship-purge-trap-gc-ms.html",
  # events discovered
  "https://www.thermofisher.com/us/en/home/events/ai-image-data-analysis-life-sciences.html",
  "https://www.thermofisher.com/us/en/home/events/integrated-cryoem-data-management-with-cryoflow2.html",
  "https://www.thermofisher.com/us/en/home/events/slas-2026.html",
  "https://www.thermofisher.com/us/en/home/events/webinar-catalysis.html",
  "https://www.thermofisher.com/us/en/home/events/uscap.html",
  "https://www.thermofisher.com/us/en/home/events/hypulse-demo-webinar.html",
  "https://www.thermofisher.com/us/en/home/events/overcoming-challenges-advance-therapies-virtual-event.html",
]
all_urls.update(second_pass)

# Now categorize everything
products_and_services = sorted([u for u in all_urls if '/products-and-services/' in u])
global_urls = sorted([u for u in all_urls if '/global/' in u])
about_us = sorted([u for u in all_urls if '/about-us/' in u])
promo_o = sorted([u for u in all_urls if '/home/o/' in u])
c_b = sorted([u for u in all_urls if '/home/c/' in u])

# All other URLs grouped by first path segment after /home/
other = {}
for u in sorted(all_urls):
    if '/products-and-services/' in u: continue
    if '/global/' in u: continue
    if '/about-us/' in u: continue
    if '/home/o/' in u: continue
    if '/home/c/' in u: continue
    # Extract first segment after /home/
    path = u.split('/us/en/home/')[1] if '/us/en/home/' in u else ''
    seg = path.split('/')[0].replace('.html', '')
    if seg not in other:
        other[seg] = []
    other[seg].append(u)

print("=" * 80)
print("1. ALL URLs under /products-and-services/")
print("=" * 80)
for u in products_and_services:
    print(u)
print(f"\nTotal: {len(products_and_services)} URLs\n")

print("=" * 80)
print("2. ALL URLs under /global/")
print("=" * 80)
for u in global_urls:
    print(u)
print(f"\nTotal: {len(global_urls)} URLs\n")

print("=" * 80)
print("3. ALL URLs under /about-us/")
print("=" * 80)
for u in about_us:
    print(u)
print(f"\nTotal: {len(about_us)} URLs\n")

print("=" * 80)
print("4. ALL URLs under /o/ (promo offers)")
print("=" * 80)
for u in promo_o:
    print(u)
print(f"\nTotal: {len(promo_o)} URLs\n")

print("=" * 80)
print("5. ALL URLs under /c/ (clearance/other)")
print("=" * 80)
for u in c_b:
    print(u)
print(f"\nTotal: {len(c_b)} URLs\n")

print("=" * 80)
print("6. ALL other discovered URLs grouped by first path segment")
print("=" * 80)
for seg in sorted(other.keys()):
    print(f"\n--- /{seg}/ ---")
    for u in sorted(other[seg]):
        print(u)
    print(f"  ({len(other[seg])} URLs)")

print(f"\n{'=' * 80}")
print(f"GRAND TOTAL: {len(all_urls)} unique URLs discovered")
print(f"{'=' * 80}")
