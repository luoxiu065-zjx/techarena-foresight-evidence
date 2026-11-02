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

## What v37 and v38 are

- v38 = v36 (the submitted version) with one change: the cap ledger for the promotion drivers is used only from the first promotion on (manifest rule 6, career-state-triage step 2).
- v37 = a version written from scratch on the evening of 1 November after re-reading the public rules and the week's logs: stage policy (entry / climb / senior / final year), Health kept at 7 or more before any Health-costing option, defuse schedule, ceiling ledger after two flat phases, no large hit in the month before a review.

Generated 2026-11-02 01:19:44 UTC.