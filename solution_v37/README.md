# Foresight Agents - Career Survival Agent, submission "foresight-v37-ladder"

Team: Foresight Agents. Mode: `agent` (JiuwenSwarm 0.2.4b3, single agent). Model: the designated competition model.

## What is in this submission

- `manifest.json` - the run loop and eight whole-run rules that stay in the system prompt for all 48 months: framework facts (observe after every take_action, every decision ends with a tool call, short reasoning), the Health and Dignity planning bands, the hidden-risk reading and the defuse schedule, the ceiling rule for the promotion drivers, the month-before-review rule, and the end-of-run recovery.
- `skills/career-compass/SKILL.md` - runs first at every decision: sets the stage (entry, climb, senior, final year), keeps the ledger of which drivers are open or at their ceiling, names the target driver, and lists the repair items that override it.
- `skills/story-option-choice/SKILL.md` - reads the options of a story event from their wording, removes the ones that bury hidden risk or cost Health while Health is not healthy, and picks the option that raises the target at no cost.
- `skills/quarter-plan/SKILL.md` - spends the three Energy points (recovery, scheduled defuse, growth on open drivers) and picks the main action by stage.
- `design/skills_design.md`, `design/decision_report.md` - how the Skills divide the work, what information they use, the principal risks and how the design generalises.
- `presentation.mp4` - the team's English presentation.

## How the agent plays, in one paragraph

Each month the agent observes, sets stage and target with career-compass, chooses the story option with story-option-choice, and ends the turn with take_action. At each quarter end it spends Energy and picks the main action with quarter-plan. The whole-run rules in the manifest keep the invariants that a 48-month context would otherwise bury: Health first until it is healthy, a defuse on a fixed count of quarters, nothing spent on a driver at its ceiling, no large hit in the month before a review, and Health and Dignity restored before the ending. No Skill names an event or a numeric game threshold; every threshold in the Skills is the team's own planning band, stated as such.
