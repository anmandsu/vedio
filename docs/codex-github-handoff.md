# Codex GitHub Handoff

This repo is a portable Codex video-studio system. Another computer can continue the work if it receives the system files, project files, references, memory, and generated anchor images.

## What To Include

Commit these paths for the portable system and the current project:

- `AGENTS.md` — main Codex operating rules.
- `.codex/` — Codex-compatible agents, skills, scripts, references, and `CODEX.md`.
- `.Codex/` — uppercase mirror used by this project.
- `.agents/` — shared skills if a target Codex setup reads this location.
- `awesome-gpt-image-2-prompts-main/` — image prompt pattern reference library.
- `projects/tijia-lianren/` — current active project, including scripts, research, bible, prompts, renders, reviews, and memory.
- `memory/` and `bible/` — global/project-level taste and visual continuity assets.
- `episode_1_vpipe_v2.yaml` — existing VPipe schema/style reference.
- `skills-lock.json` — installed skill snapshot.

Keep generated character anchor images in Git if file sizes stay reasonable. They are not disposable cache; they are identity references. For older projects or raw research media, either exclude them or use Git LFS.

## What Not To Include

Do not commit:

- API keys or `.env` files.
- `node_modules/`, Python virtualenvs, temp folders, browser caches.
- Very large generated videos/audio unless you intentionally use Git LFS.
- Raw downloaded research videos/audio under `projects/**/research/videos/` unless needed for reproducibility.

## First-Time Upload

Run from the workspace root:

```powershell
cd "C:\Users\123\Videos\vedio V3"
git init
git add AGENTS.md .codex .Codex .agents awesome-gpt-image-2-prompts-main projects/tijia-lianren memory bible episode_1_vpipe_v2.yaml skills-lock.json docs .gitignore
git commit -m "Add Codex AI video studio system"
git branch -M main
git remote add origin https://github.com/<your-user>/<your-repo>.git
git push -u origin main
```

If Git warns that a file is over GitHub's normal size limit, remove that file from the commit or use Git LFS.

Optional Git LFS setup for large media:

```powershell
git lfs install
git lfs track "*.mp4" "*.mov" "*.mp3" "*.wav"
git add .gitattributes
```

## Updating Later

```powershell
cd "C:\Users\123\Videos\vedio V3"
git status
git add AGENTS.md .codex .Codex .agents projects/tijia-lianren memory bible docs skills-lock.json .gitignore
git commit -m "Update project memory and identity-reference workflow"
git push
```

## Download On Another Computer

```powershell
git clone https://github.com/<your-user>/<your-repo>.git
cd <your-repo>
```

Then open the folder in Codex and ask:

```text
先读 AGENTS.md、.codex/CODEX.md、projects/tijia-lianren/STATUS.md 和 projects/tijia-lianren/memory/project-lessons.md，接着从当前进度继续。
```

## New Computer Checklist

- Confirm Codex opens the cloned workspace root.
- Confirm `AGENTS.md` is visible to the session.
- Confirm `projects/tijia-lianren/renders/images/` contains accepted anchor images.
- Confirm `projects/tijia-lianren/bible/fingerprints/` contains face anchors and prompt fragments.
- Set any needed API keys locally on the new machine; never store them in Git.
- If using external generation APIs, configure `LINKAPI_KEY`, `WHATAI_API_KEY`, or other provider keys outside the repo.

## Best Continuation Prompt

```text
你现在接手这个项目。请先读 AGENTS.md、.codex/CODEX.md、projects/tijia-lianren/STATUS.md、projects/tijia-lianren/memory/project-lessons.md、projects/tijia-lianren/memory/prompt-formulas.md。
重点：不要用纯文字多宫格生成人物定稿；用 bible/fingerprints/ 的脸锚图做本地图生图，一张状态图一张状态图生成，审核后再拼板。
```
