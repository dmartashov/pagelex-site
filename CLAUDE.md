# pagelex-site: rules for the coding agent

The website of PageLex (an iPhone app) at https://pagelex.app: static HTML and CSS, served by GitHub Pages from `main`. Danil is the developer; Cowork (a separate marketing session) plans and reviews; you are the one agent in the terminal. These rules were agreed in Cowork on 23 Nov 2026. This repository is public: nothing private goes into it, this file included.

Where `~/.claude/CLAUDE.md` differs from this file, this file wins. Its Part 2 (Swift, SwiftUI, skills) doesn't apply here; its reading rules, task flow, git rules, "Never" list and report headings do, with the changes below.

## 1. Sources
- `README.md`: how the site is built. `tools/build_home.py` holds every text of the four home pages (`index.html` English, `uk/`, `es/`, `de/`): change texts only there, then run `python3 tools/build_home.py .` from the repository root; never edit those four HTML files by hand. `support/index.html` and `assets/` are edited directly.
- Product facts: `~/Desktop/MyApps/PageLex/docs/PRD.md` (read-only; read only the section the prompt names). The marketing status: `~/Desktop/MyApps/PageLex/Claude outputs/marketing/00-STATUS.md` (read-only). Never write anything in the PageLex folder.
- A task named by an M task ID (for example P1-27) is described in `~/Desktop/MyApps/PageLex/docs/ROADMAP.md`: `grep -n 'P1-27 ·'` and read only its block.
- The prompt outranks your habits; if it conflicts with this file, the README or the PageLex documents, stop and report.

## 2. Task flow
1. Start check: run at the repository root, on branch `draft` (`git rev-parse --abbrev-ref HEAD` prints `draft`), with a clean `git status`. Otherwise stop, report and touch nothing.
2. Do only the task: its prompt. No redesign, renaming or reformatting on the side; put what you notice under "Suggestions".
3. Run the checks (section 4), write the report (section 5), and wait. Don't commit.
4. Danil looks at the pages in his browser and Cowork reviews; fixes happen in this same session.
5. Commit only after Danil writes "commit". Hours are not tracked here: they go into the M task in PageLex's ROADMAP, which this repository never touches.

## 3. Git
- Allowed: `status`, `diff`, `log`, `show`, `rev-parse`, `add <path>`, `rm <file the task names>`, and `commit` after Danil's command.
- Never: `push`, `pull`, `merge`, `rebase`, `reset`, `restore`, `checkout`, `switch`, `stash`, `tag`, `branch`, `clean`, `worktree`, `commit --amend`, `add -A`, `add .`, `commit -a`. All work is on `draft`; Danil pushes it and merges it into `main` when the site should go live.
- Commit messages in English: `P1-27: <what>` (the M task ID, or `Site:` when there is none), then 1–5 lines: what changed and why. Keep the `Co-Authored-By` line.

## 4. Checks (report each output)
1. If `tools/build_home.py` changed: `python3 tools/build_home.py .` ran, and running it again changes nothing (`git status --short` the same before and after the second run).
2. No outside scripts, styles, fonts or frames: `grep -rnE '<script|<iframe|@import|url\(https?:' --include='*.html' --include='*.css' .` prints nothing, and `grep -rnE '<(link|img)[^>]*(src|href)="https?://' --include='*.html' .` prints nothing. Plain links (`<a href=…>`, `mailto:`) are fine.
3. No mechanics on the pages (marketing decision 3: what the reader gets, not how the app works): `grep -rniE 'FSRS|WordNet|Foundation Models|algorithm|LLM' --include='*.html' .` prints nothing.
4. No App Store badge before release (Apple licenses it only for apps available for download): no badge image or badge-styled link; plain launch text only.
5. `cat CNAME` prints `pagelex.app`; `git status --short` lists only the files the task names.
6. Every changed page opens: `python3 -m http.server 8000` from the repository root, then the steps for Danil under report heading 6 (which pages, what to look at, which widths: an iPhone-sized window and a desktop one).

## 5. Report
Write the full report to `agent-reports/<task>-report-N.md` (git-ignored; a new N per run) with Bash, then print one terminal line `STATUS: done | done with warnings | blocked | stopped`. Headings as in `~/.claude/CLAUDE.md`, with: 3. Checks: section 4's outputs; 4. Skill files read: None; 6. Browser check for Danil: the steps. If writing the file is denied, print the report.

## 6. Boundaries
- Never change `CNAME`, the DNS, GitHub settings or anything outside this repository.
- No analytics, cookies, trackers, outside scripts or fonts, no forms that send data to another service unless the prompt names that decision (PageLex DECISIONS §2.14).
- Demo book text is public domain only (README names the books); never put text from a modern book into the repository.
- Spanish and German texts are AI-translated: change them only when the prompt gives the text.
- No prices, dates, numbers or claims about the app that the prompt or the PRD doesn't give. Never invent reviews, testimonials or user counts.
- No new dependencies: plain HTML, CSS and the Python standard library in `tools/`.
- `.claude/settings.json` enforces part of this, and only when Claude Code starts at the repository root.
