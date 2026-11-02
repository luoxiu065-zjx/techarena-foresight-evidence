# Foresight Agents - Tech Arena UK 2026 - evidence of versions v37 / v38 and their test games

All times are UTC (= UK time during the competition week). This repository was created to show, with git commit timestamps, when the Skill versions below were written and tested. Nothing here was changed after the files were copied; the file modification times are listed as they are on the development machine.

## Submissions on the contest site (team Foresight Agents)

| when (UTC) | record id | content | status when last checked |
|---|---|---|---|
| 2026-10-30 17:16 | 6ae4d0ea3a5df6820e0909f8 | v28g | Accepted, 31.74 (cut-off 2) |
| 2026-11-01 22:56 | 6ae7c2fb3a5df6820e093067 | v28j | Cancelled (superseded by the next upload) |
| 2026-11-01 23:47 | 6ae7cf773a5df6820e0932e1 | v36 | Waiting (final cut-off) |

## Zip checksums on the development machine

| zip | bytes | md5 |
|---|---|---|
| foresight_v28g_solution.zip | 49252266 | 55d1cb6db3caae6abc067e4b2db3cdb2 |
| foresight_v28j_final.zip | 49253302 | 76ba8b10a4843f972c467cc492548f98 |
| foresight_v36_final.zip | 49253973 | 298d75b01596d637f11c9992a82d89ad |

## File modification times of the Skill versions (as on the development machine)

### solution_v36

- 2026-11-01 23:56:52 UTC  solution_v36/README.md
- 2026-11-01 22:40:26 UTC  solution_v36/design/decision_report.md
- 2026-11-01 22:40:26 UTC  solution_v36/design/skills_design.md
- 2026-11-01 23:56:51 UTC  solution_v36/manifest.json
- 2026-11-01 22:40:26 UTC  solution_v36/skills/career-state-triage/SKILL.md
- 2026-11-01 22:40:26 UTC  solution_v36/skills/monthly-event-response/SKILL.md
- 2026-11-01 22:40:26 UTC  solution_v36/skills/quarterly-resource-planner/SKILL.md

### solution_v37

- 2026-11-01 23:14:45 UTC  solution_v37/README.md
- 2026-11-01 23:15:23 UTC  solution_v37/design/decision_report.md
- 2026-11-01 23:15:01 UTC  solution_v37/design/skills_design.md
- 2026-11-01 23:13:31 UTC  solution_v37/manifest.json
- 2026-11-01 23:21:52 UTC  solution_v37/skills/career-compass/SKILL.md
- 2026-11-01 23:22:04 UTC  solution_v37/skills/quarter-plan/SKILL.md
- 2026-11-01 23:21:56 UTC  solution_v37/skills/story-option-choice/SKILL.md

### solution_v38

- 2026-11-02 00:07:47 UTC  solution_v38/README.md
- 2026-11-02 00:07:47 UTC  solution_v38/design/decision_report.md
- 2026-11-02 00:07:47 UTC  solution_v38/design/skills_design.md
- 2026-11-02 00:07:47 UTC  solution_v38/manifest.json
- 2026-11-02 00:07:47 UTC  solution_v38/skills/career-state-triage/SKILL.md
- 2026-11-02 00:07:47 UTC  solution_v38/skills/monthly-event-response/SKILL.md
- 2026-11-02 00:07:47 UTC  solution_v38/skills/quarterly-resource-planner/SKILL.md

## Full games of v37 and v38 (official model deepseek-v4-flash via OpenRouter, local and rented-server instances)

| game | version | where | started (UTC) | result |
|---|---|---|---|---|
| 109 | v37 | local instance 1 | 2026-11-01 23:28 | 71.04, completed 48, L5 |
| 111 | v38 | server r1 | 2026-11-02 00:08 | 74.67, completed 48, L6 at month 48 |
| 112 | v38 | server r3 | 2026-11-02 00:08 | 69.12, completed 48, L5 |
| 104 | v36 | server r1 | 2026-11-01 22:40 | 73.47, completed 48, L5 |
| 105 | v36 | server r3 | 2026-11-01 22:40 | 38.51, health zero at month 42 |
| 114 | v37 | local instance 1 | 2026-11-02 00:44 | 69.67, completed 48, L5 |
| 115 | v37 | server r3 | 2026-11-02 00:52 | 71.93, completed 48, L5 |
| 116 | v38 | server r4 | 2026-11-02 00:44 | 60.17, completed 48, L5 |

Three-game means: v37 = (71.04 + 69.67 + 71.93) / 3 = 70.88; v38 = (74.67 + 69.12 + 60.17) / 3 = 67.99. All six runs completed 48 months; none was dismissed at the first level.

Score reports (as written by the official runner) are in `notes/evidence/`.
## Full per-step logs

`notes/evidence/logs/game<no>_<version>/` holds, for each of the eight games above, the complete files the official runner wrote: `events-<start>.jsonl` (every observe result, every take_action call with its note, every model turn, with timestamps), `transcript-<start>.log` (the model's full text), and `score_report.json`. The directory name inside each folder is the run's start time in UTC.
 `notes/CHANGELOG.md` is the development log kept during the week, one entry per game and change.

## How the test games were run (tools and environment)

- Runner: the official participation repository `techarena-career-sim` (upstream commit 00b084a, 26 Oct 2026), unmodified, via `python -m career_sim_runner play --submission <solution dir> --ws-url ws://127.0.0.1:<agent port>`. One local game at a time per JiuwenSwarm instance; each game starts from a fresh instance and an empty emulator database.
- Framework and engine, identical on both machines: JiuwenSwarm 0.2.4b3 (single-agent mode, `"mode": "agent"`), career_emulator_engine 1.0.6, career_emulator_techarena 1.0.8, openjiuwen 0.1.16.post2, Python 3.12. The agent talked to the simulation only through the five official MCP tools.
- Model: deepseek-v4-flash through OpenRouter (`API_BASE=https://openrouter.ai/api/v1`, `MODEL_NAME=deepseek-v4-flash`). The organiser-issued competition key was nearly exhausted by then, so these eight games used the team's own OpenRouter key with the same model name. In the OpenRouter account settings of that key the allowed hosting providers were limited to the fp8 endpoints (DeepInfra, GMICloud, SiliconFlow, Parasail, Crusoe) and Baidu Qianfan was excluded; this is an account-level setting of our test key only, nothing in the submission material names a provider. The JiuwenSwarm instance setting `preferred_language: zh` was in place, so part of the model's internal reasoning in the transcripts is in Chinese; the Skills and all notes written to the game are English.
- Machine A (games 109 and 114): the team's Windows 11 laptop, JiuwenSwarm instance `career_emu`, agent port 19092.
- Machine B (games 104, 105, 111, 112, 115, 116): a rented Tencent Cloud CVM in Frankfurt, Ubuntu 22.04.5 LTS, 8 vCPU, 15 GB RAM, four JiuwenSwarm instances `r1`-`r4` each with its own copy of the runner and its own emulator database; up to three games ran at the same time. Its system clock is UTC+8 (`~/ta/notes/run.log` lines are in that zone); the timestamps inside `events-*.jsonl` and the output folder names are UTC.
- Per-game cost and token counts are in each `score_report.json` (`token_usage`). Typical full game: 50-90 M input tokens, 1.3-1.5 M tokens per month, USD 1.5-5 depending on which provider OpenRouter routed to.
- Each game was watched only through its log files; no process touched the running instance, the database or the outputs while a game was in progress.

## What v37 and v38 are

- v38 = v36 (the submitted version) with one change: the cap ledger for the promotion drivers is used only from the first promotion on (manifest rule 6, career-state-triage step 2).
- v37 = a version written from scratch on the evening of 1 November after re-reading the public rules and the week's logs: stage policy (entry / climb / senior / final year), Health kept at 7 or more before any Health-costing option, defuse schedule, ceiling ledger after two flat phases, no large hit in the month before a review.

Generated 2026-11-02 01:19:44 UTC.