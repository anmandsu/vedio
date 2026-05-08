# Project Lessons

## 2026-05-08 | dongjiao-guochao-xiqu | Overall Styling Direction

- User said: The project is a Guochao xiqu styling experience store in Dongjiao Memory. The design must be based on traditional Chinese opera headwear, especially fengguan and shuai helmet. It should feel modern and fashionable, but not drift into gothic, cyberpunk, armor fantasy, or generic hanfu/new-Chinese styling.
- System changed: Moved from broad "opera-inspired fashion" toward a stricter two-anchor system: fengguan line and shuai-helmet / wudan-lingzi line. Used user-provided traditional xiqu images as img2img/reference anchors, then modernized the clothing around the preserved hair/headwear silhouette.
- Result: V5C storefront and later V7/V8/V10 character sheets became the accepted direction. Strongest accepted signal was `renders/concepts_v5c/v5c_04_young_storefront_16x9.png`, followed by full-body three-view design sheets.
- Lesson: For this client, first preserve the readable xiqu silhouette, then modernize the clothing. The headwear/hair shape is the identity anchor; clothing is the innovation layer.
- Scope: project
- Evidence count: 1 project with repeated feedback loops
- Promote? no

## 2026-05-08 | dongjiao-guochao-xiqu | Accepted Visual Language

- User said: "v5c_04_young_storefront_16x9.png" is close and much better. Makeup can be simpler, keep the hairstyle feeling. Later: all designs are okay, background can be more fashionable; then keep background and batch 50 similar designs.
- System changed: Reduced heavy theatrical makeup; kept black forehead opera hair patches, bead flowers, pearl tassels, red pom-poms, curved lingzi arcs, and fengguan/shuai-kui silhouettes. Shifted clothing into youth-oriented boutique Guochao with pankou, cloud collar/shoulder, embroidery, gauze, tassels, wide-leg pants, culottes, short jacket, and clean boots/sneakers.
- Result: V8 50-sheet batch established the reusable design system: 25 skirt variants and 25 pants variants, all as 16:9 full-body three-view fashion concept sheets.
- Lesson: "Young Guochao xiqu" should read as a styling store product line, not stage costume restoration. The best balance is 70% traditional headwear silhouette + 30% modern wearable fashion construction.
- Scope: project
- Evidence count: multiple accepted iterations in one project
- Promote? no

## 2026-05-08 | dongjiao-guochao-xiqu | Body-Friendly Clothing Without Changing Body Type

- User said: Need 10 designs that do not expose the navel, are mid-length and covering, suitable for slightly chubby girls. Then corrected: these ten look too fat; the person should not become fat, redesign the clothes.
- System changed: Added a hard prompt separation between body shape and clothing fit: keep the model normal young fashion-model proportions, but make the clothing size-inclusive and forgiving. Required no exposed belly, no cropped top, hip-covering jackets, long cloud-collar overlays, A-line layers, relaxed trousers, skirt-over-pants, vertical embroidery panels, and soft drape over belly/hips.
- Result: V10 regular-body covering series corrected the misunderstanding. It preserved the youthful model while creating practical, covering outfits for real customers.
- Lesson: When asking image models for "slightly chubby-friendly" fashion, explicitly say the person must not become plus-size or bulky; only the clothing should be flattering and covering. Put this in all future body-friendly fashion prompts.
- Scope: project / user-candidate
- Evidence count: 1 clear correction
- Promote? candidate after repetition in future styling projects

## 2026-05-08 | dongjiao-guochao-xiqu | Presentation Deliverables

- User said: Build an HTML layout for the 50 plus the previous four. Then asked about garbled question marks, then requested PDF because mobile could not open the HTML, then asked for non-compressed version because the PDF was blurry.
- System changed: Generated a visual gallery HTML and multiple PDF export variants. Kept PDFs out of Git per user instruction.
- Result: HTML gallery and image derivatives were committed; PDF files remain local and untracked.
- Lesson: For image-heavy client review, keep two delivery tracks: responsive HTML for desktop/in-app review, and high-resolution PDF export for phone/WeChat sharing. For final Git commits, confirm whether PDFs should be included, because high-res PDFs can be large and often are delivery artifacts rather than source assets.
- Scope: project
- Evidence count: 1
- Promote? no

