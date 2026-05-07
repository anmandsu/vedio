# Research Index

Project: 《雀神》 / `queshen`

Research scope: first-episode opening scene, `SC01_UNDERGROUND_CASINO`, based only on the 4-page setup PDF.

## Minimum Viable Research Pack

| Requirement | Status | Anchor |
|---|---|---|
| 3 comparable visual references | met | `Casino Royale` poker-table tension; `Rounders` poker-room language; `赌神` Hong Kong gambling-film genre signal |
| 1 director/tone reference | met | `Casino Royale` card scene problem: make table play cinematic through information, reaction, and pressure |
| 1 cinematography reference | met | Phil Meheux / Cooke Optics interview + secondary cinematography analysis |
| 1 editing/continuity reference | met | `Rounders` screenplay and card-table scene language; `Casino Royale` poker-scene analysis |
| 1 production design / physical reference | met | Pexels casino table and mahjong tile photos saved in `research/atmosphere_refs/` |
| 1 sound / atmosphere reference | met | `Rounders` screenplay's poker-room sound cues plus script's mahjong/knock/smoke anchors |
| Source cards | met | `research/source-register.md` |

## Search Log

| Date | Tool | Query / Command | Result | Use |
|---|---|---|---|---|
| 2026-05-06 | OpenCLI | `opencli list -f yaml` | Confirmed `google`, `douban`, `bilibili`, `youtube`, and other adapters are available | Required OpenCLI start step |
| 2026-05-06 | OpenCLI | `opencli google search "casino poker scene cinematography lighting tension interview" --limit 6 --lang en -f md` | Found casino-scene craft articles and cinematography discussion leads | Early direction/cinematography leads |
| 2026-05-06 | OpenCLI | `opencli google search "Rounders screenplay poker scene" --limit 6 --lang en -f md` | Found Brian Koppelman's official Rounders screenplay post | Tier A screenplay anchor |
| 2026-05-06 | OpenCLI | `opencli douban search "赌神" --type movie --limit 5 -f md` | Confirmed `赌神` series metadata and Hong Kong gambling-film genre lineage | Comparable genre axis |
| 2026-05-06 | OpenCLI | `opencli google search "Casino Royale poker scene cinematography interview Phil Meheux" ...` | Failed with stale/detached page identity | Logged gap; web search used as fallback |
| 2026-05-06 | Web search | `Cooke Optics Phil Meheux Casino Royale 15th anniversary interview poker scene` | Found Cooke Optics Phil Meheux interview | Cinematography / lighting anchor |
| 2026-05-06 | Web search | `Brian Koppelman Rounders screenplay pdf` | Found Koppelman's official screenplay post | Screenplay / table-language anchor |
| 2026-05-06 | Web search | `Pexels casino dealer dimly lit table 6664144`, `Pexels mahjong tiles green felt` | Found physical table and tile photo pages | Physical/atmosphere refs |
| 2026-05-06 | PowerShell + Pexels API | `casino poker table dark`, `poker chips table`, `mahjong tiles` | Saved four reference images under `research/atmosphere_refs/` | Physical table, props, lighting texture |

## Reference Axes For SC01

| Axis | Reference | Source Tier | Borrow | Avoid |
|---|---|---|---|---|
| Card-table suspense | `Casino Royale` poker sequence craft discussion | Tier A/B mix | Treat the table as a duel of observation, reaction, and controlled push-ins | Do not copy Bond luxury or tournament poker directly |
| Underground gambler language | `Rounders` screenplay | Tier A | Use voiceover, table sound, money/hand/eye detail to make rules legible | Do not make the scene talky or American poker-coded |
| Hong Kong gambling-film charge | `赌神` | Tier A/B mix | Let the hero's table presence become mythic once he turns the game | Do not drift into parody comedy or slapstick |
| Physical reality | Pexels casino/mahjong references | Tier B visual refs | Use felt/table shine, chip/tile rows, hands, dealer-space density, low practical light | Do not make the casino an abstract neon void |

## Research Gaps

- No full first-episode script has been imported, so this research only supports the opening casino scene.
- We have not done a deep source pass on real Chinese underground gambling rooms; current space references combine casino table photos and genre inference.
- We have not locked actor face references; character bibles remain draft seeds.
