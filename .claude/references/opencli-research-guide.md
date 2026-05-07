# OpenCLI Research Guide

OpenCLI is the execution/search layer. Use it to collect material with low token cost, then summarize into project files.

## Preference Order

1. Existing OpenCLI adapter with JSON output.
2. `opencli browser` extraction from a logged-in page.
3. Normal web search.
4. Manual user-provided source.

## Rules

- Keep raw web/browser payloads out of long-term memory.
- Save distilled source cards to `research/source-register.md`.
- If the tool returns structured JSON, keep only the fields needed for film decisions.
- Do not treat search snippets as enough evidence for craft rules.

## Useful Tasks

- Find comparable films and interviews.
- Extract article text or video page metadata.
- Capture reference image pages or moodboard candidates.
- Use logged-in sites for sources that generic browsing cannot access.

