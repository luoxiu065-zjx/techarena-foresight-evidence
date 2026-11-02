# foresight-v36

Team Foresight Agents. Career Survival Agent submission for TechArena UK 2026, JiuwenSwarm 0.2.4b3, single-agent mode.

## Skills

- career-state-triage: runs first at every decision point. It writes a short status card: which of Skill, Network and Output are still open at this level, with the cap recorded in this run for any capped driver; how much Health and Dignity can be spent above this year's floor; a hidden-risk estimate with the quarters since the last defuse; and the months to the next review, marking the two guard months before it.
- monthly-event-response: chooses the option for a story event. It infers each option's likely effect from the handbook vocabulary and the lessons in earlier notes, removes options that bury hidden risk or break the Health and Dignity floor, and in the guard months does not take an option that lowers Skill, Network or Output when another option keeps them.
- quarterly-resource-planner: spends the three Energy points and picks the main action. It restores the floor first, buys one point of Health before the guard months, defuses on a fixed schedule, puts the remaining points into open drivers, and in the last two quarterly phases spends spare points on Health and Dignity.

The manifest instruction carries eight whole-run rules, so they stay in the system prompt for all 48 months. Two of them are entry-level rules added in this version: in the first three months, while Health is below 7, no story option that costs Health is taken; and for the two quarters after a C or D review grade, story options that raise Output or Network at once come before self-protective options such as declining, taking leave or keeping to your hours.

## Layout

- manifest.json: team, submission name, mode agent, and the run-loop instruction with the whole-run rules.
- design/skills_design.md: purpose of each Skill, where the rules live, information used, how outputs combine.
- design/decision_report.md: overall approach, information relied on, principal risks, generalisation.
- presentation.mp4: the team's video.
