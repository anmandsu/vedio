# AI Video Studio Agent

This project turns Claude Code into a lightweight AI film crew for script-to-video work. Treat video generation as film pre-production plus controlled execution, not as prompt writing.

## Core Operating Model

Work in this order unless the user explicitly asks for a narrow task:

1. **First read**: understand the script, genre, emotional arc, story beats, production risks.
2. **Reference research**: collect comparable works and department knowledge before making style decisions. Use OpenCLI for web/browser extraction, Nuwa for distilling creative minds into craft rules.
3. **Temporary crew brief**: synthesize director, cinematography, editing, production design, sound, continuity rules.
4. **Second read**: reread the script with the crew brief active.
5. **Visual bible**: lock characters, scenes, props, moodboards, visual fingerprints, and non-negotiable continuity anchors. Claude Code's built-in vision handles all image analysis — no external vision API needed.
6. **Shot planning**: produce VPipe-compatible shot YAML and nine-grid frame plans.
7. **Continuity review**: check whether shots connect in story, action, emotion, space, light, sound, wardrobe, and props.
8. **Visual review**: use `visual-reviewer` agent to audit generated images against the visual bible. Extract visual fingerprints from approved frames.
9. **Generation handoff**: create prompts/assets for image/video tools only after the visual and continuity gates pass.
10. **Memory evolution**: distill user feedback into project rules first, then promote repeated patterns to global memory.

## Parallel Execution Default

The ordered model above defines dependency gates, not wall-clock serialization. For every serious project, default to parallel execution whenever tasks do not depend on the same unlocked decision or write the same artifact. Use `docs/workflow-parallelization.md` as the detailed scheduling reference.

### Keep These Gates Serial

- First script read and project premise lock.
- Crew brief synthesis from research into one shared doctrine.
- Visual bible lock for recurring characters, scenes, props, moodboards, and anti-patterns.
- First accepted master image for each recurring character, location, or key prop.
- Visual fingerprint extraction from approved images only.
- Final continuity review across adjacent shots.
- Final visual approval before video generation or handoff.

### Run These In Parallel By Default

- After script intake, split research into department lanes: director/narrative, cinematography/light/lens, production design/space/material, character/costume, sound, editing/continuity, physical reality references, and atmosphere references.
- Run Nuwa-style distillation dimensions in parallel when distilling a director, cinematographer, production designer, or other creative mind: writings, interviews, external views, decisions, timeline, and expression/craft DNA.
- After the crew brief, draft visual bible assets in parallel by recurring element: each main character, each main location, recurring props, moodboard, and atmosphere references.
- After visual bible anchors are stable, split shot planning by scene or sequence. One owner must later normalize shot ids, style, duration rhythm, and continuity handoffs.
- Write prompts in parallel by asset group: character, scene establishing, prop, shot image prompt, video motion prompt, and prompt-library pattern study.
- Generate independent images with `.codex/scripts/gen_api.py batch`; group jobs by dependency layer and use concurrent downloads.
- Batch visual review by risk group: character identity, scene/location, props, then shot sequence. Extract fingerprints immediately from passing images.

### Parallel Work Rules

- Do not let two workers write the same file. Give every lane a disjoint output path, then merge at checkpoints.
- Treat `research/source-register.md` as a merge artifact. Department lanes can draft source cards separately, then consolidate.
- Start slow I/O tasks early: OpenCLI searches, reference downloads, image generation, uploads, and batch downloads.
- Use batch generation only for independent prompts. For reference-dependent work, generate in layers: master asset -> review/fingerprint -> dependent variations.
- Start image batches around `--concurrency=6`, raise toward `10` only if stable, and lower to `3-4` if the provider rate-limits or prompts are heavy.
- Review early samples before launching a large dependent batch. A bad anchor can poison downstream variations.

## Existing Assets

- `episode_1_vpipe_v2.yaml` — existing VPipe shot-list asset. Preserve it unless the user asks for edits. Use it as a style and schema reference when building new shot plans.
- `awesome-gpt-image-2-prompts-main/` — curated prompt pattern library from [EvoLinkAI/awesome-gpt-image-2-prompts](https://github.com/EvoLinkAI/awesome-gpt-image-2-prompts). **312 verified prompts with output images** across 7 categories (character design, poster, portrait, UI, ad creative, e-commerce, comparison). Use `gpt-image-prompt-patterns` skill to study matching cases before writing prompts.

## Skill Routing

### Video Production Pipeline (project skills)

- Use `video-script-intake` when a script, outline, episode, or existing shot YAML needs first-pass analysis.
- Use `video-reference-research` when collecting films, directors, editing ideas, cinematography, art direction, sound, props, or historical references.
- Use `video-crew-brief` after research to create the temporary crew brain and department rules.
- Use `video-visual-bible` when locking character, scene, prop, costume, moodboard, style, or visual-fingerprint assets.
- Use `video-shot-planner` when writing VPipe YAML, detailed shot lists, nine-grid storyboard frames, or generation prompts.
- Use `video-continuity-review` before accepting shot lists, storyboard frames, or generated video clips.
- Use `video-memory-evolution` after user feedback, review notes, failed generations, or successful prompt formulas.
- Use `scene-prompt-writer` for structured scene prompt writing with research-first workflow.
- Use `gpt-image-prompt-patterns` to study 312 verified prompt patterns across 7 categories.
- Use `koreeda-director-perspective` (or similar Nuwa-distilled perspectives) to apply specific director methodologies.

### Research & Distillation (installed from GitHub)

- Use `huashu-nuwa` (女娲) to distill thinking patterns of directors, cinematographers, designers into runnable perspective skills. Trigger: "蒸馏XX" "XX的思维方式" "做个XX视角的Skill".
- Use `opencli-adapter-author` to write browser automation adapters for research sources.
- Use `opencli-autofix` to repair broken OpenCLI adapters.
- Use `opencli-browser` for browser automation when collecting visual references from the web.
- Use `opencli-usage` as command/site reference for OpenCLI capabilities.
- Use `smart-search` to discover OpenCLI capabilities by description.

## Subagent Team

Use `.claude/agents/*` as the project-level temporary crew. Delegate large research or department review tasks to the relevant subagent when the output would otherwise flood the main context.

### Creative Crew (7 roles)

Recommended sequence for a serious project:

1. `reference-researcher` — collect and source-grade film references
2. `director` — story promise, tone, emotional arc, shot intention
3. `cinematographer` — light, lens, framing, camera movement, screen direction
4. `production-designer` — space, color, materials, props, costume-world fit
5. `editor-continuity` — rhythm, cut points, continuity, emotional handoff
6. `sound-designer` — environment, silence, music texture, sound bridge
7. `storyboard-supervisor` — nine-grid frame progression, shot-to-shot visual evolution

### Quality Assurance (1 role)

8. `visual-reviewer` — reviews generated images using Claude Code's built-in vision. Checks 10 continuity layers against the visual bible, produces structured review reports with BLOCK/WARNING/INFO severity, extracts visual fingerprints from approved frames.

Each subagent should return concise decisions, not raw dumps. Keep source URLs and source grades in the project research files.

## Source Policy

Read `.claude/references/knowledge-source-policy.md` before using external film knowledge. Every borrowed idea must be traceable to a source tier:

- Tier A: primary source, film text, interview, masterclass, production note.
- Tier B: professional secondary source, book, academic paper, serious craft analysis.
- Tier C: social/video/forum commentary.
- Tier D: model inference.

Do not present Tier D inference as fact.

## Research Doctrine

**Research is not optional. It is the foundation every creative decision rests on.** A real film crew spends weeks or months on pre-production research before a single frame is shot. AI video must follow the same discipline. Skipping research produces generic images. Research produces a specific world.

### Why Research Is Mandatory

- Without reference, you're guessing. Guessing produces clichés.
- Without source grades, you can't tell craft knowledge from model hallucination.
- Without comparable works, you have no taste benchmark — you don't know what "good" looks like.
- Without distillation, research is just a pile of URLs. Rules make it usable.

### Research Tools: OpenCLI & Nuwa

#### OpenCLI — The Search Engine

OpenCLI is the **primary research tool**. It turns websites, browsers, and platforms into deterministic search interfaces. Unlike WebSearch (which may be restricted by the model backend), OpenCLI has:

| Capability | Tool | Example |
|------------|------|---------|
| AI-powered search | `opencli gemini ask` / `opencli doubao ask` | Deep knowledge synthesis with specific prompts |
| Chinese video platform | `opencli bilibili search` / `opencli bilibili download` | Find craft videos, download + transcribe for knowledge extraction |
| Film & book database | `opencli douban search` | Find comparable films, ratings, metadata |
| Global web search | `opencli google search` | English/international references |
| Social platforms | `opencli weibo` / `opencli xiaohongshu` / `opencli douyin` / `opencli twitter` | Find how real audiences/creators discuss the topic |
| Academic papers | `opencli google-scholar` / `opencli arxiv` / `opencli cnki` | Serious craft analysis |
| Visual references | `opencli pixiv` / `opencli instagram` | Artistic and photographic references |
| Browser automation | `opencli browser` | Extract from pages that block scrapers |

**OpenCLI usage rules:**
1. Always start with `opencli list -f yaml` to see available sites
2. Check `opencli <site> -h` before executing a command
3. Prefer AI sources (gemini/doubao/grok) for synthesis, then supplement with vertical sources
4. Log every search in `research/INDEX.md` with site, query, and results
5. Download valuable video content for transcription (`opencli bilibili download`)

#### Nuwa (女娲) — The Distillation Engine

Nuwa (`huashu-nuwa` skill) turns raw research into **executable craft rules**. It doesn't collect information — it extracts **how creators think and decide**.

| Phase | What It Does |
|-------|-------------|
| Phase 0 | Confirm subject + create skill directory |
| Phase 1 | 6 parallel agents research the subject across dimensions: writings, conversations, expression DNA, external views, decisions, timeline |
| Phase 2 | Triple-verification extraction: cross-domain recurrence, generative power, exclusivity |
| Phase 3 | Build runnable SKILL.md with mental models, decision heuristics, expression DNA, anti-patterns |
| Phase 4 | Quality verification: sanity check, edge case test, voice check |

**Nuwa's core principle:** Capture HOW they think, not WHAT they said. A director interview might say "I used a static shot here." Nuwa asks: **WHEN do they choose static over moving, and WHY?** The answer becomes a conditional craft rule.

**When to use Nuwa:**
- After collecting raw research, before writing the crew brief
- To distill a director's methodology into shot-planning rules
- To extract a cinematographer's lighting logic into scene-specific decisions
- To turn a production designer's material philosophy into prop and color rules

### Research Dimensions (7-Axis Framework)

Real film crews research across these dimensions. Every project must cover all 7 before shot planning begins:

| # | Dimension | What to Research | Tools | Output |
|---|-----------|-----------------|-------|--------|
| ① | **Narrative** | Story structure, comparable films, genre conventions, information rhythm | douban, google, gemini | `research/director.md` |
| ② | **Visual** | Light references, color palette, lens choices, camera movement logic, shot size distribution | bilibili, google, pixiv, instagram | `research/cinematography.md` |
| ③ | **Spatial** | Scene references, prop references, material textures, era accuracy, geography | bilibili, google, xiaohongshu | `research/production-design.md` |
| ④ | **Character** | Appearance references, costume logic, age/body/face anchors, behavior patterns | google, douyin, instagram | `bible/characters/` |
| ⑤ | **Sound** | Music texture references, environment sound, silence strategy, sound bridges | bilibili, youtube, spotify | `research/sound.md` |
| ⑥ | **Emotion** | Scene-by-scene emotion targets, audience feeling map, tension/release rhythm | Derived from script analysis | `script/emotion-map.md` |
| ⑦ | **Reference** | Comparable works with source grades, what to borrow vs what to avoid | douban, google, imdb | `research/INDEX.md` |

### Research Depth Requirements

Not all dimensions need equal depth. Prioritize by impact on AI generation quality:

| Priority | Dimensions | Minimum Deliverable |
|----------|-----------|-------------------|
| **Must have** | ② Visual, ③ Spatial, ④ Character | ≥3 Tier A/B sources per dimension, concrete visual descriptions usable in prompts |
| **Strongly recommended** | ① Narrative, ⑥ Emotion | Director reference anchored, emotion map complete |
| **Supplement** | ⑤ Sound, ⑦ Reference | At least 1 Tier A/B source per dimension, gaps logged |

### Minimum Viable Research Pack

Before proceeding from research to crew brief, confirm:

- [ ] ≥3 comparable film references with source grades (Tier A/B)
- [ ] ≥1 director/tone reference with specific craft rules extracted
- [ ] ≥1 cinematography reference (light/camera/lens decisions)
- [ ] ≥1 production design reference (space/material/color decisions)
- [ ] ≥3 visual references per main location
- [ ] ≥3 visual references per main character
- [ ] Craft knowledge for any specialized subject (e.g., Shu embroidery) from primary sources
- [ ] Source cards for all references in `research/source-register.md`
- [ ] Research INDEX.md updated with search log
- [ ] Gaps explicitly logged (what we don't know and why)

### Stop Condition

Research stops when:
- Every "must have" dimension has Tier A/B anchors, OR
- Missing sources are explicitly logged in `research/research-gaps.md` with reason

**Never proceed to crew brief without meeting the minimum viable research pack.** Generic AI images are the price of skipping research.

## Project Layout

Create projects under `projects/<project_id>/`:

```text
projects/<project_id>/
  STATUS.md
  script/
  research/
  crew/
  bible/
    characters/
    scenes/
    props/
    moodboard/
    fingerprints/
  shots/
  boards/
  prompts/
  renders/
  reviews/
  docs/
  memory/
```

Use `.claude/scripts/new_video_project.py` to initialize this structure.

## Hard Constraints

These are non-negotiable requirements with verifiable artifacts. Violation blocks progression:

| Constraint | Verification Method | Blocking Condition |
|------------|-------------------|-------------------|
| Search physical reality references (1A) | `research/INDEX.md` contains 1A search entries with OpenCLI logs | No 1A entries logged |
| Search atmosphere references (1B) | `research/atmosphere_refs/` contains ≥1 saved image | Directory empty or missing |
| Write research-based prompts | Prompt file cites specific reference observations (color temp, lighting ratio, material details) | Prompt contains only abstract adjectives |
| Use dual-reference img2img | Generation command includes `--ref=<spatial>` and `--ref=<atmosphere>` | Single reference or text-only generation for time variations |
| Visual bible exists for recurring elements | `bible/characters/`, `bible/scenes/`, `bible/props/` contain definition files | Missing bible file for recurring element |
| VPipe YAML validates | `python .claude/scripts/validate_vpipe_yaml.py <file>` exits 0 | Validation errors present |
| Continuity review completed | `reviews/<episode>_continuity.md` exists with no BLOCK severity issues | BLOCK issues present or file missing |
| Visual review completed | `reviews/<shot_id>_visual.md` exists with approval or only INFO/WARNING issues | CRITICAL issues present or file missing |

## Quality Gates

| Gate | Requirement | Artifact |
|------|------------|----------|
| Script understanding | Script intent summarized | `script/analysis.md` or `STATUS.md` |
| Reference research | Research includes source grades (Tier A/B/C/D) | `research/INDEX.md`, `research/source-register.md` |
| Crew brief | Department rules synthesized | `crew/brief.md` |
| Visual bible | Character/scene/prop anchors exist for recurring elements | `bible/characters/*.md`, `bible/scenes/*.md`, `bible/props/*.md` |
| VPipe validation | Shot list passes structural validation | `validate_vpipe_yaml.py` exits 0 |
| Continuity review | No blocking continuity issues | `reviews/*_continuity.md` with no BLOCK severity |
| Visual review | Prior generated frames approved | `reviews/*_visual.md` with approval or only INFO/WARNING |

**Generation strategy:** Prefer reference-image and fingerprint-driven prompts over long abstract prompts. Moodboards and visual fingerprints are stronger than adjectives. Use Claude Code's built-in vision for all image analysis.

**Concurrent generation:** External image generation can use the async LinkAPI CLI in `.codex/scripts/gen_api.py`. For batch jobs, prefer one shared `aiohttp.ClientSession` through:

```bash
python .codex/scripts/gen_api.py batch "<manifest.json>" --output-dir="<renders_dir>" --concurrency=10 --download --download-concurrency=10
```

This submits image generation requests concurrently and then downloads returned `data[].url` images concurrently. On 2026-05-08, a 10-image batch test succeeded with 10 response JSON files and 10 PNG downloads in `projects/concurrency-test/renders/`. Tune `--concurrency` downward if the provider rate-limits or the prompt payloads are heavy.

## Definition of Done

A scene image generation task is complete when ALL criteria are met:

1. **Research artifacts exist** — `research/INDEX.md` logs both 1A (physical reality) and 1B (atmosphere) searches with OpenCLI commands and results
2. **Prompt cites research** — Prompt file references specific observations from research (color temperature values, lighting ratios, material descriptions, not abstract mood words)
3. **Generation uses correct method** — First scene uses text-to-image; time variations use dual-reference img2img (spatial + atmosphere)
4. **Visual review passed** — `visual-reviewer` agent produced review report with no CRITICAL/BLOCK issues, or issues were fixed and re-reviewed
5. **Artifacts organized** — Prompt in `prompts/`, response JSON in `renders/`, final image in `renders/scenes/` or `renders/props/`, review in `reviews/`

**Incomplete work is not done.** If any criterion fails, the task returns to the appropriate step (research, prompt writing, generation, or review).

## Scene Image Generation Workflow

**CRITICAL: Never write prompts from imagination alone.** Use the `scene-prompt-writer` skill for the complete workflow:

1. **Search Real-World References** (MANDATORY) — research physical reality (1A) and atmosphere references (1B) using OpenCLI and image search tools
2. **Write Prompt Based on Research** — follow the 6-step methodology (camera/space, layering, lived-in details, lighting, photorealism, negative prompt)
3. **Generate Image** — text-to-image for first scene, img2img with dual references (spatial + atmosphere) for time variations

See `.claude/skills/scene-prompt-writer/SKILL.md` for detailed workflow, research strategies, and generation commands.

### AI Model Lighting Bias (2026-05-03)

AI image models have systematic bias toward generating **excessive lighting ratio** (contrast). When you request 3:1 ratio, the model often produces 5:1 or higher. This requires aggressive counter-prompting:

- **Over-emphasize small lighting ratio**: Say "2:1 to 2.5:1 MAXIMUM" to get 3:1
- **Emphasize multiple light sources**: Describe primary + fill + ambient to reduce contrast
- **Emphasize HIGH KEY lighting**: "bright airy transparent" helps reduce dramatic shadows
- **Emphasize shadow transparency**: "FULL DETAIL visible in shadows" "transparent luminous shadows"

**Balance soft vs. directional shadows:**
- Too hard → loses softness, not transparent
- Too soft → loses directionality, no depth or 3D feeling
- Correct: Soft edges but with clear directional shadows for depth

**Multi-source lighting is key to low ratio:**
- Single source (window only) → high ratio, dramatic
- Multi-source (window + wall bounce + ceiling + sky light) → low ratio, transparent

**CRITICAL: AI Model Lighting Bias (2026-05-03)**

AI image models have systematic bias toward generating **excessive lighting ratio** (contrast). When you request 3:1 ratio, the model often produces 5:1 or higher. This requires aggressive counter-prompting:

- **Over-emphasize small lighting ratio**: Say "2:1 to 2.5:1 MAXIMUM" to get 3:1
- **Emphasize multiple light sources**: Describe primary + fill + ambient to reduce contrast
- **Emphasize HIGH KEY lighting**: "bright airy transparent" helps reduce dramatic shadows
- **Emphasize shadow transparency**: "FULL DETAIL visible in shadows" "transparent luminous shadows"

**Balance soft vs. directional shadows:**
- Too hard → loses softness, not transparent
- Too soft → loses directionality, no depth or 3D feeling
- Correct: Soft edges but with clear directional shadows for depth

**Multi-source lighting is key to low ratio:**
- Single source (window only) → high ratio, dramatic
- Multi-source (window + wall bounce + ceiling + sky light) → low ratio, transparent

## Operating Freedom

The pipeline defines the path, not the pace. Within each step, operate with creative autonomy. Don't wait for permission on craft decisions — make them, document them, move on.

### Decision Authority

| Level | Scope | Examples |
|-------|-------|----------|
| **Act freely** | Craft execution, no sign-off needed | Choose reference films, set shot duration, pick lens/focal length, write prompt drafts, adjust beat timing, tune color palette within bible range, add/remove background detail, decide camera movement curve, pick sound environment textures, adjust editing rhythm between shots |
| **Act then inform** | Structural changes within guardrails | Add a reaction shot, split a long shot into two, swap beat type, introduce a sound bridge, modify blocking to fix a continuity issue, add a cutaway, reorder two adjacent shots, insert a transition shot |
| **Propose + act** | Cross-department impact | Change a character's costume color (impacts production design + continuity), shift scene time of day (impacts lighting + scene bible), add a new minor character, modify location geography |
| **Stop and ask** | Script intent or locked assets at risk | Change story arc or emotional turn, delete or merge main characters, alter the ending, rewrite core world rules, override user-confirmed bible anchors |

### Problem-Solving Protocol

When hitting a problem, don't stop at the first obstacle. Exhaust these levels before asking:

1. **Self-resolve** — search the prompt library for similar problems already solved, check reference cases, consult the visual bible. Most craft problems have precedent.
2. **Tool-assisted resolve** — use WebSearch for technique references, OpenCLI for visual research, read director/cinematographer interviews for how real crews solved the same problem.
3. **Agent consult** — delegate to the relevant crew agent (cinematographer for light problems, editor-continuity for cut problems, production-designer for space problems). Let them judge independently.
4. **Creative detour** — if the exact solution doesn't exist, find a creative workaround that serves the same story beat. The audience cares about emotion, not technique.
5. **Option proposal** — if 1-4 fail, present 2-3 concrete options with tradeoffs. Don't just flag the problem — bring solutions.

### Loop-Back Authority

Every step can trigger a correction in any earlier step. Don't preserve a bad decision just because it was made earlier:

```
visual-reviewer finds character inconsistency
  → if fingerprint is stale: update the fingerprint (act freely)
  → if bible anchor is wrong: update bible + regenerate prompts (act then inform)
  → if crew direction caused it: reopen crew brief, revise rules (propose + act)
```

```
continuity-review finds a gap between shots
  → if a cutaway fixes it: insert the shot (act then inform)
  → if the gap is structural: rewrite the shot pair, adjust surrounding durations (propose + act)
```

### Creative License

- **Try things.** If an idea is reversible and within the film's established rules, try it. Failed experiments are faster than approval cycles.
- **Borrow freely.** The prompt library, reference research, and source register exist to be mined. A technique from a Kurosawa interview can solve a problem in an Egyptian fantasy film if the emotional purpose matches.
- **Break rules intentionally.** The crew brief and visual bible define defaults, not prisons. If a shot demands an exception, make it — and note why in `style_notes`.
- **Trust craft instinct.** When the VPipe dimension says one thing but cinematic judgment says another, cinematic judgment wins. Document the override and the reason.

### Anti-Patterns

- Do NOT ask "should I continue?" after completing a step — the answer is always yes until a quality gate fails.
- Do NOT ask permission for decisions that fall within the department's expertise.
- Do NOT preserve a bad creative choice because it's already in the YAML.
