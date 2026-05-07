# Scene Prompt Writer for AI Video Projects

## Goal

Generate high-quality photorealistic scene establishing shots for AI video projects. Transform scene requirements (location, time, mood, color temperature) into detailed prompts that produce cinematic, spatially coherent, lived-in environments without people.

## Core Principles

1. **Space First, Details Second** - Start with spatial layout and camera angle, then add details
2. **Photorealism Over Abstraction** - Use concrete physical terms (film stock, lens, materials) not abstract adjectives (beautiful, amazing)
3. **Lived-In, Not Showroom** - Include signs of human presence and daily use
4. **Cinematic Composition** - Think like a cinematographer: foreground/midground/background, depth, lighting

## Method: 5-Step Prompt Construction

### Step 1: Establish Camera & Space (MANDATORY)

```
Create an ultra-photorealistic [wide-angle/medium/close-up] [documentary-style/cinematic] photograph of [location type], empty with no people, [time of day], shot with [lens] on [camera], [film stock], natural film grain, [aspect ratio].

SPATIAL LAYOUT - [ANGLE] VIEW:
The camera positioned at [height/position], capturing [dimensions and depth]. The composition shows clear foreground, midground, and background layers.
```

**Key elements:**
- Lens choice: 24mm (wide establishing), 35mm (medium), 50mm (standard), 85mm (portrait)
- Camera: medium format camera, full-frame DSLR, cinema camera
- Film stock: Kodak Portra 400 (warm natural), Kodak Ektar 100 (saturated), Fuji Pro 400H (muted)
- Aspect ratio: 21:9 (cinematic), 16:9 (standard), 4:3 (classic)

### Step 2: Layer the Space (MANDATORY)

Describe in order: FOREGROUND → MIDGROUND → BACKGROUND

```
FOREGROUND ([position]):
[Specific objects with materials, textures, placement, state of use]

MIDGROUND ([position], main focus):
[Primary subject/furniture with dimensions, materials, spatial relationships]

BACKGROUND ([position]):
[Walls, windows, architectural features, light sources]
```

**Spatial vocabulary:**
- Position: left/right/center, near/far, corner, against wall
- Dimensions: "1.5m tall", "2m wide", "approximately 6m deep"
- Relationships: "between", "in front of", "behind", "arranged at angles"

### Step 3: Add Lived-In Details (CRITICAL for warmth)

Include 5-10 signs of human presence:

**Daily use items:**
- Half-full tea cup with stains
- Reading glasses on open notebook
- Smartphone charging cable
- Half-eaten food
- Thermos, water bottle

**Use traces:**
- Cushion with sitting indent
- Sweater draped over chair
- Slippers kicked off
- Thread ends on floor
- Scattered tools (not perfectly arranged)

**Personal items:**
- Jacket on hook
- Bag hanging
- Calendar with notes
- Photos or postcards
- Small plants (slightly dusty)

**Time traces:**
- Sun-faded areas
- Tea stains on surfaces
- Worn paths on floor
- Yellowed paper
- Dust in corners

### Step 4: Specify Lighting (MANDATORY)

```
LIGHTING:
[Light source] from [direction], [quality]. Color temperature [K]. [Atmosphere description]. [Shadow characteristics]. [Light behavior - rays, falloff, reflections].
```

**Light quality vocabulary:**
- Soft/hard, diffused/direct, warm/cool
- Volumetric light rays, god rays
- Natural window light, golden hour, blue hour
- Side lighting, backlighting, top lighting
- Gentle shadows with soft edges, dramatic shadows with hard edges

### Step 5: Photorealism Keywords & Negative Prompt

**Photorealism triggers (add 5-10):**
- ultra-photorealistic, documentary-style, candid photo
- taken with a real camera, realistic photograph
- visible [material] texture: wood grain, fabric weave, skin pores
- natural imperfections, subtle flaws
- film grain, shallow depth of field
- natural light falloff, real shadows
- no artificial smoothing, no CGI look
- candid moment, unposed

**Negative prompt (ALWAYS include):**
```
Negative prompt: people, figures, humans, cartoon, illustration, painting, blurry, deformed, low quality, overexposed, underexposed, plastic look, AI artifacts, over-saturated colors, perfect symmetry, sterile, showroom, museum display, too clean, modern office, fluorescent lighting, no soul, cluttered chaos
```

## Photorealism Keyword Library

### Camera & Technical
- 24mm/35mm/50mm/85mm lens
- f/1.8, f/2.8, f/4 aperture
- shallow depth of field, deep focus
- medium format camera, full-frame DSLR
- Kodak Portra 400, Fuji Pro 400H, Kodak Ektar 100
- natural film grain, subtle grain
- shot on [camera model]: Hasselblad, Leica, Canon 5D

### Lighting
- soft natural daylight from [direction]
- golden hour sunlight, blue hour atmosphere
- dramatic side lighting, gentle top lighting
- volumetric god rays, light beams with dust particles
- natural window light, diffused through curtains
- warm/cool color temperature [K]
- natural light falloff, realistic shadows

### Texture & Material
- visible wood grain texture
- fabric weave clearly visible
- individual threads discernible
- surface imperfections, scratches, wear marks
- natural patina, aged materials
- dust particles, subtle dirt
- real material properties, tactile quality

### Realism Modifiers
- photorealistic, ultra-photorealistic, hyper-realistic
- documentary photography style
- candid photo, unposed moment
- natural imperfections, real-world flaws
- no artificial smoothing, no post-processing
- authentic, genuine, honest representation
- taken with a real camera, not CGI

### Avoid AI Look
- no over-saturated colors
- no perfect symmetry
- no plastic skin/surfaces
- no heavy makeup/filters
- slight motion blur (if applicable)
- natural color grading
- real-world lighting physics

## Scene Type Templates

### Traditional Workshop/Studio
```
Wide-angle (24mm) interior, 6m×4m×3m space, traditional architecture (wood/brick), multiple work stations, tools and materials visible, storage areas, natural window light, lived-in details (tea cup, slippers, personal items), warm undertones despite cool lighting.
```

### Residential Interior
```
Medium shot (35mm), domestic space, furniture showing use (cushion indents, throws), personal items (photos, books, plants), natural clutter, soft window light, warm color palette, intimate scale.
```

### Outdoor Location
```
Wide establishing (24mm), natural landscape or urban environment, clear foreground/midground/background, atmospheric perspective, natural lighting (golden hour/overcast), environmental details (vegetation, architecture), sense of place and scale.
```

## Quality Checklist

Before generating, confirm:

- [ ] Camera angle and lens specified
- [ ] Spatial dimensions provided (approximate OK)
- [ ] Foreground/midground/background described
- [ ] 5+ lived-in details included
- [ ] Lighting direction, quality, and color temp specified
- [ ] 5+ photorealism keywords included
- [ ] Material textures described (wood grain, fabric weave, etc.)
- [ ] Negative prompt included
- [ ] "no people" explicitly stated
- [ ] Aspect ratio specified (21:9 for cinematic)

## Common Pitfalls

❌ **Too focused on objects, not space** - Describing items without spatial context
✅ Fix: Start with room dimensions and camera position

❌ **Abstract adjectives** - "beautiful", "amazing", "atmospheric"
✅ Fix: Use concrete terms - "Kodak Portra 400", "soft side lighting", "wood grain texture"

❌ **Too clean/perfect** - Looks like a showroom
✅ Fix: Add 5-10 lived-in details (tea cup, slippers, thread ends)

❌ **Vague lighting** - "good lighting", "nice light"
✅ Fix: Specify source, direction, quality, color temp - "soft natural daylight from left window, 3200K, diffused through paper panels"

❌ **Missing photorealism keywords** - Prompt reads like a description
✅ Fix: Add technical photography terms - "shot with 35mm lens", "film grain", "shallow depth of field"

❌ **No negative prompt** - AI adds unwanted elements
✅ Fix: Always include comprehensive negative prompt

## Cost Optimization: img2img for Time Variations

For same location at different times:
1. Generate base scene (morning) with full detailed prompt
2. Use base as reference image for other times (evening, night)
3. img2img prompt focuses only on lighting changes:
   ```
   Same interior space and layout as reference image.
   Change only: [evening/night] lighting, color temperature [K], [lighting description].
   Maintain all furniture, objects, and spatial layout exactly as reference.
   ```

This saves 60-70% of generation cost for location continuity.

## Example: Traditional Workshop Morning

```
Create an ultra-photorealistic wide-angle establishing shot of a traditional Shu embroidery workshop interior, empty with no people, early morning light, documentary photography style, shot with 24mm wide lens on medium format camera, Kodak Portra 400 film stock, natural film grain, 21:9 cinematic aspect ratio.

SPATIAL LAYOUT - WIDE ANGLE VIEW:
Camera at human eye level near entrance, capturing 6m deep × 4m wide traditional Chinese workshop space.

FOREGROUND (left):
Low wooden work table with open needle box (needles scattered, not arranged), silk thread spools (some unrolled, trailing onto table), ceramic tea cup half-full with rim stains, half-eaten steamed bun on small plate, reading glasses on open notebook with handwritten notes, smartphone charging cable, scissors, ruler. Natural clutter of recent use.

MIDGROUND (center, main focus):
Three wooden embroidery frames - large frame (1.5m tall) with half-finished peony silk work (needle still stuck mid-stitch), medium frame with cushioned stool (cushion showing sitting indent), smaller frame with stretched fabric. Standing lamp with sweater draped over it. Floor has thread ends and fabric scraps.

BACKGROUND (far wall):
Traditional Chinese lattice windows (2m wide) with translucent paper panels, soft morning light streaming through. Windowsill: small potted plant (dusty leaves), water bottle, wall calendar with dates circled in red. Right: tall wooden cabinet with glass doors, silk thread spools in rows (not perfectly aligned). Left wall: two completed embroidery pieces (slightly crooked), coat hook with jacket and canvas bag.

LIVED-IN DETAILS:
Pair of slippers by stool, thermos on floor, small electric fan in corner (dusty), window paper yellowed from sun, books stacked near cabinet, wall clock showing 7:15 AM, faded floor areas from daily sunlight, small radio on shelf.

ARCHITECTURAL:
Aged wood panel walls (visible grain, peeling paint, nail holes), old wooden floor planks (worn smooth in paths, natural patina, tea stains), 3m ceiling height.

LIGHTING:
Soft natural daylight from lattice windows, diffused through paper panels, cool-toned 3200K with warm undertones on wood surfaces, gentle shadows with soft edges, natural light falloff, volumetric light rays with dust particles. Early morning quality - tender, quiet.

COLOR PALETTE:
Cool morning blues and grays, warm wood browns (rosewood, aged pine), muted silk colors (deep crimson, jade green, golden yellow slightly desaturated), natural patina of used materials.

ATMOSPHERE:
Working studio, not museum display. Someone works here daily. Warmth, history, quiet dignity of craft. Space waits for owner to return. Restrained melancholy with underlying warmth.

PHOTOREALISTIC DETAILS:
Visible wood grain texture, fabric weave, individual silk threads, dust particles in light, tea stains, worn cushion fabric, natural shadows, real depth of field, candid moment, natural imperfections, honest texture of daily life.

COMPOSITION REFERENCE:
Documentary photography of traditional craft spaces, Edward Hopper's quiet presence, Vilhelm Hammershøi's empty rooms with implied human presence, Japanese wabi-sabi aesthetic.

Negative prompt: people, figures, humans, cartoon, illustration, painting, blurry, deformed, low quality, overexposed, plastic look, AI artifacts, over-saturated colors, perfect symmetry, sterile showroom, museum display, too clean, modern office, fluorescent lighting, no soul, cluttered chaos
```

## Integration with Video Pipeline

This skill is part of the video production pipeline:

1. **video-script-intake** → understand story
2. **video-reference-research** → collect visual references
3. **video-crew-brief** → establish creative direction
4. **video-visual-bible** → lock character/prop/scene anchors
5. **→ scene-prompt-writer (THIS SKILL)** → generate scene prompts
6. **video-shot-planner** → create shot lists with these scenes
7. **video-continuity-review** → verify scene consistency

## Usage

```
/scene-prompt-writer <scene_id> <location> <time> <mood> <color_temp>
```

Example:
```
/scene-prompt-writer SC01 "traditional Shu embroidery workshop" "early morning" "restrained melancholy with warmth" "3200K"
```

The skill will generate a complete prompt following the 5-step method.

---

## Detailed Research & Generation Workflow (from CLAUDE.md)

This section provides the complete research-before-generation workflow that must be followed before using the 5-step prompt construction method above.

### Step 1: Search Real-World References (MANDATORY)

Before writing any prompt, research TWO types of references:

#### 1A. Physical Reality References (lighting physics)

Use OpenCLI to understand how light actually behaves:

```bash
# Search for physical lighting behavior
opencli xiaohongshu search "<scene type> <time of day>"
opencli bilibili search "<scene type> lighting"
opencli google search "<scene type> photography"
opencli pixiv search "<scene type> interior>"
```

**What to search for:**
- Scene type + time of day (e.g., "traditional workshop morning", "embroidery studio evening")
- Lighting conditions (e.g., "golden hour interior", "twilight室内光线", "夜晚室内灯光")
- Architectural style (e.g., "traditional Chinese interior", "老房子室内")
- Specific elements (e.g., "embroidery frame", "wooden furniture natural light")

**Build cognitive understanding:**
- How does natural light behave at this time of day?
- What color temperature is typical? (morning: 3200-4000K, noon: 5500K, evening: 3500-4500K, night with lamps: 2700-3000K)
- When do people turn on indoor lights? (typically after sunset, not during golden hour)
- What shadows look like at different times?
- What materials and textures are present?

**Common mistakes to avoid:**
- ❌ Assuming evening = indoor lights on (evening/golden hour is natural light, night = lights on)
- ❌ Mixing incompatible light sources (e.g., strong sunlight + indoor lamps at the same time)
- ❌ Ignoring seasonal and geographic light quality differences
- ❌ Using abstract time descriptions without understanding actual lighting physics

#### 1B. Atmosphere References (aesthetic/mood)

**CRITICAL: Physical reality alone is not enough.** You also need atmosphere references that capture the desired aesthetic quality.

Use image search tools to find atmosphere references:

```bash
# Search for atmosphere/aesthetic references
python .claude/scripts/pexels_search.py "<scene type> <time> <mood>"
opencli xiaohongshu search "<scene aesthetic keywords>"
opencli pinterest search "<visual mood keywords>"
```

**What to search for:**
- Specific aesthetic qualities (e.g., "warm nostalgic interior", "gentle golden hour room", "restrained natural light")
- Color temperature + mood (e.g., "3500K warm cream interior", "muted amber workshop")
- Lighting ratio + atmosphere (e.g., "soft contrast interior", "gentle window light")

**Evaluate atmosphere references:**
- Color temperature (measure in Kelvin if possible)
- Lighting ratio (estimate key-to-fill contrast)
- Shadow characteristics (hard/soft, transparent/opaque)
- Overall mood (cinematic/documentary, dramatic/restrained)

**CRITICAL: Save approved atmosphere references for img2img.** When generating same-location time variations, use the atmosphere reference as an additional img2img input to guide the aesthetic, not just describe it in text.

### Step 2: Write Prompt Based on Research

Only after building real-world understanding, write the prompt using the 5-step methodology above.

**Reference the research:**
- Cite specific lighting observations from reference images
- Use concrete physical terms from real-world examples
- Match color temperature to actual time of day
- Describe light behavior you observed in references

**Use specific references to express desired feeling (表达越清晰越好):**

AI models understand concrete references better than abstract adjectives. Use:

1. **Film references**: "像《花样年华》里的暖色调光线" "Lighting quality like [specific scene] in [film name]"
2. **Director style**: "王家卫式的暖色调" "侯孝贤式的自然光" "Wong Kar-wai warm tones" "Hou Hsiao-hsien natural light"
3. **Clear emotional descriptions**: "明媚的黄昏" (bright gentle dusk), "温柔的傍晚" (tender evening), "宁静的清晨" (quiet morning)
4. **Specific visual characteristics**: "3500K奶油色温" (3500K cream color temp), "3:1柔和光比" (3:1 gentle lighting ratio), "透明的阴影" (transparent shadows)

**Avoid vague adjectives**: "好看的" (nice-looking), "有感觉的" (with feeling), "氛围感" (atmospheric) - these are too abstract for AI to interpret consistently.

### Step 3: Generate Image

**For first scene of a location (text-to-image):**
```bash
LINKAPI_KEY="<key>" python .claude/scripts/gen_api.py image \
  "$(cat prompts/SC01_prompt.txt)" \
  --output=renders/SC01_response.json
```

**For same location at different times (img2img, saves 60-70% cost):**

**CRITICAL: Use BOTH spatial reference AND atmosphere reference for img2img.**

```bash
# 1. Upload base scene as spatial reference
PICUI_API_TOKEN="<token>" python .claude/scripts/picui_upload.py upload \
  renders/SC01.png --public
  # → Returns spatial_ref_url

# 2. Upload atmosphere reference (from Step 1B research)
PICUI_API_TOKEN="<token>" python .claude/scripts/picui_upload.py upload \
  research/atmosphere_refs/golden_hour_ref.jpg --public
  # → Returns atmosphere_ref_url
  
# 3. Generate time variation with BOTH references
LINKAPI_KEY="<key>" python .claude/scripts/gen_api.py image \
  "Same space as first reference. Change only: <time> lighting, <color_temp>K. Match atmosphere and lighting quality of second reference: <describe atmosphere ref characteristics>." \
  --ref="<spatial_ref_url>" \
  --ref="<atmosphere_ref_url>" \
  --output=renders/SC02_response.json
```

**img2img prompt focus:**
- State "Same interior space and spatial layout as first reference image"
- Specify lighting changes: time of day, color temperature, light sources
- Reference the atmosphere image: "Match lighting quality and atmosphere of second reference"
- Describe atmosphere ref characteristics: color temp, lighting ratio, shadow quality, mood
- Maintain all furniture, objects, architectural details from spatial reference
- Keep same camera angle and composition

**Why use atmosphere reference:**
- Text descriptions alone often produce overly dramatic or flat results
- AI models have strong biases toward cinematic lighting for terms like "golden hour"
- A real photo atmosphere reference anchors the aesthetic between "too dramatic" and "too flat"
- Atmosphere ref provides concrete color temperature, lighting ratio, and shadow characteristics

### Complete Workflow Summary

```
┌─────────────────────────────────────────────────────────────┐
│ 1. SEARCH REFERENCES (OpenCLI + Image Search)               │
│    ├─ 1A. Physical reality (lighting physics)               │
│    └─ 1B. Atmosphere references (aesthetic/mood)            │
│    ↓ Build real-world understanding + aesthetic anchors     │
│ 2. WRITE PROMPT (5-step methodology above)                  │
│    ↓ Based on research, not imagination                     │
│ 3. GENERATE IMAGE                                            │
│    ├─ First scene: text-to-image (full prompt)              │
│    └─ Time variations: img2img with spatial + atmosphere refs│
│    ↓ Review quality                                          │
│ 4. ITERATE if needed (adjust lighting, details)             │
└─────────────────────────────────────────────────────────────┘
```

**Cost optimization:**
- First scene of each location: text-to-image (full prompt)
- Same location, different times: img2img with dual references (saves 60-70% tokens)
- Upload approved base scene + atmosphere reference to picui.cn for img2img

**Key lesson learned (2026-05-03):**
- Physical reality research alone produces technically correct but aesthetically flat results
- Atmosphere references are MANDATORY for img2img to anchor the aesthetic quality
- "Restrained" does not mean "no atmosphere" — it means balanced between dramatic and flat
- Use atmosphere ref as img2img input, not just text description
