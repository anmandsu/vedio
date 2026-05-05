# Research Index

Project: 替嫁恋人：大佬她只想复仇
Research phase: style and shot-language first, before character/scene image generation.

## Department Status

| Department | Status | Key Source | Tier |
|------------|--------|------------|------|
| Director | v0 complete | Bilibili vertical short-drama craft subtitle + industry articles | B/C |
| Cinematography | v0 complete | Bilibili vertical composition subtitle | C |
| Editing | v0 complete | Bilibili editing search + vertical short-drama craft subtitle | C |
| Production Design | v0 direction only | Script locations + industry premium-production trend | B/D |
| Sound | v0 direction only | Script beats + short-drama pacing inference | D |
| Reference Works | search started | micro-drama industry references, no fixed drama mimic chosen | B/C |

## OpenCLI Search Log

| Date | Site | Query | Results | Tier |
|------|------|-------|---------|------|
| 2026-05-05 | opencli list | `opencli list -f yaml` | Confirmed `doubao`, `bilibili`, `douban`, `google` adapters exist. | Tool check |
| 2026-05-05 | doubao | 中文竖屏短剧: 都市豪门、替嫁、复仇、契约恋爱、强反转爽剧的导演/摄影/剪辑/美术/声音规则 | Timed out after 90s; not used as evidence. | Gap |
| 2026-05-05 | bilibili search | `竖屏短剧 拍摄 剪辑 节奏 爽剧 豪门 复仇` | Returned craft/analysis videos including vertical shooting logic, short-drama editing, golden 3 seconds, and revenge-drama edits. | C |
| 2026-05-05 | bilibili subtitle | `BV1AyA8z1EFu` | Subtitle extracted; key claims: vertical drama has weak/absent middle shot, relies on closeup/extreme closeup, expression montage, multi-angle editing, and short on-face line delivery. | C |
| 2026-05-05 | bilibili video | `BV1AyA8z1EFu` | Metadata fetched after diagnostic retry; title: `短剧入行竟栽在竖屏？别再用横屏逻辑拍短剧了！`, author 张暴撕, published 2026-03-01. | C |
| 2026-05-05 | bilibili video | `BV1Pv7DzVEjt` | Adapter returned `Failed to fetch`; skipped after one failed attempt. | Gap |
| 2026-05-05 | google search | `Chinese vertical short drama production style pacing cinematography 2025` | Found industry articles on vertical micro-drama growth, rapid pacing, vertical format, production efficiency. | B/C |
| 2026-05-05 | google search | `micro drama vertical screen short drama China rapid pacing production 2025` | Found People's Daily, Xinhua, Jing Daily, TIME, China Media Project, and other references. | B/C |
| 2026-05-05 | douban search | `豪门 复仇 契约恋爱 电视剧` | Returned no usable results for this query. | Gap |
| 2026-05-05 | google search | `现代 中式 豪门 婚礼 别墅 红毯 入口`; `luxury Chinese villa wedding red carpet entrance`; `bridal car interior veil closeup luxury wedding`; `vertical short drama closeup lighting wedding daylight` | OpenCLI Google adapter failed with stale page/detached errors; switched to Pexels/API and web search fallback. | Gap |
| 2026-05-05 | Pexels API | `luxury wedding red carpet` | Saved JSON references under `research/physical_refs/`; useful for aisle/red-carpet structure but not Chinese luxury specificity. | C |
| 2026-05-05 | Pexels API | `bride veil car` | Saved JSON references under `research/physical_refs/`; useful for bridal car interior, veil translucency, face-through-veil framing. | C |
| 2026-05-05 | Pexels API | `black suit man luxury event` | Saved JSON references under `research/physical_refs/`; useful for black suit authority, cuff/suit inserts, corridor/event entrance posture. | C |
| 2026-05-05 | Pinterest API | `Chinese luxury wedding villa red carpet` | Failed with HTTP 429 Too Many Requests; skipped to avoid repeated calls. | Gap |
| 2026-05-05 | Pexels API | `daylight wedding ceremony` | Saved JSON references under `research/atmosphere_refs/`; useful for high-key outdoor ceremony daylight and guest background density. | C |
| 2026-05-05 | Pexels API | `red carpet daylight event` | Saved JSON references under `research/atmosphere_refs/`; useful for red-carpet daylight exposure and vertical body framing. | C |
| 2026-05-05 | Pexels API | `luxury event close up daylight` | Saved JSON references under `research/atmosphere_refs/`; useful for polished tableware/specular luxury closeups and bright event atmosphere. | C |

## Research Decisions

- The project should not chase slow prestige-drama grammar first. Its main grammar is vertical short drama: closeup, object insert, reaction cut, fast reversal, and hard episode hook.
- 9:16 is not a crop of 16:9. It needs its own blocking: one face dominant, one readable object, one emotional turn per shot.
- Director model: short-drama showrunner rather than auteur director. The director protects hook density, emotional legibility, and payoff timing.
- Crew form: compact vertical-drama unit with director, cinematographer, editor-continuity, production designer, sound designer, and visual continuity supervisor.

## Gaps

- Need stronger China-specific 1A reference for villa wedding entrance/red carpet; current Pexels red-carpet references are structural only.
- Need stronger China-specific 1A reference for villa wedding entrance/red carpet; current Pexels red-carpet references are structural only.
- Need source-backed visual references for character costume and main locations before writing image prompts.
