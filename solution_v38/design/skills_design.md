# Skills design

Team: Foresight Agents
Submission: foresight-v36

## 1. How we read the task

The agent starts at L1 and has 48 months. The ending score weighs level (30%), wealth (20%), health and dignity (15%), skill (15%), risk control (10%) and network (10%). Salary rises with level, so an early promotion pays for every month that follows and leaves time for the upper levels, which in our runs asked for much more Skill and more months at the level.

Promotion is decided at the half-year reviews (months 6, 12, 18 and so on) from Skill, Network and Output. Three things we saw in our own runs shaped the design.

- At each level a driver stops responding once it reaches a ceiling that is not published, so points spent on it after that are lost.
- The first two reviews matter most. In every run of ours that scored well, the agent was promoted at month 6 and again at month 12; a run still at L1 after month 12 seldom recovered. At L1 the ceilings are small, so one point of Network or Output lost to a story choice just before a review was enough to miss it, and the quarterly Energy phase that could restore it comes after the review.
- Hidden risk cannot be seen directly. The HR partner's monthly remark lags behind it; in one run it stayed at its calmest step for most of the first fourteen months, then jumped to the top step and a blow-up followed.

## 2. Where the rules live

Rules that must hold for all 48 months are in the manifest instruction, because the framework places it in the system prompt on every model call. The three Skills hold the procedures. They are read at the start and read again at the quarterly phase after each review, because a long game log pushes earlier tool results far back in the context.

The manifest states six whole-run rules:

1. Call observe once after each take_action.
2. Every decision ends with a tool call in the same turn.
3. Health and Dignity bands are shares of the top of each scale given in the handbook: 70% or more is safe; the floor is 30% in months 1-12, 40% in months 13-24 and 50% from month 25; below the floor, recover first. In the quarterly phases at the end of months 45 and 48, Energy left after any defuse goes to recovery. These are our own policy, not game thresholds.
4. In the two months before each review (the guard months), do not choose an option that lowers Output, Skill or Network when another option keeps them; that other option may take Health or Dignity one point below the floor. The quarterly phase just before the guard months buys one point of Health recovery unless Health is safe.
5. Before the first promotion, a review without a promotion is followed by a defuse; from the first promotion on, two quarterly phases without a defuse force one; each new HR remark at step 2 or higher forces one.
6. A driver is capped when its value at a quarterly phase is no higher than its highest value at this level two phases earlier, although something was meant to raise it; that highest value is recorded as its cap, and the current value is compared with the record at every decision.

## 3. The three Skills

### career-state-triage (first, at every decision point)

Purpose: turn the latest observe result into a short internal status card that the other two Skills read.

- Ledger. Each driver is compared with its highest value at this level two quarterly phases earlier. One flat quarter is not enough, because a story result may have taken a point at the same time. When a driver is marked capped, that highest value and the level are written into the note as its recorded cap. Below the record, the driver is open again and is topped back up; above it, the driver was never capped and the record is dropped; after a promotion all records are cleared. No Energy is spent only to test a cap.
- Mode. Push while at least one driver is open; rebuild when all three are capped.
- Health and Dignity bands by year, as in the manifest, with the one-point guard-month exception.
- Hidden-risk estimate (low, rising, high) from the HR remark's five published steps and from story signs (a risky kind of option was chosen, a note carries "risk flag", or a thread came back after such a choice). A remark that stays at the same step after a defuse does not count again. The card also counts the defuse gap; a blow-up does not reset it.
- Time. Months to the next quarterly phase and the next review; months 4-5, 10-11 and so on are guard months, in which no quarterly action can repair a lost point before the review.
- Expectation check. Every note carries an expectation in a fixed form ("expect Output +1, risk none"). On a miss, the next note adds a short lesson naming the kind of option and its real effect, never the event name, and lessons outrank the general vocabulary.
- Priorities near a limit: Health or Dignity below the floor twice in a row outranks everything; after a C or D grade or a warning-tone review the open drivers come first for two quarters; two windows at a level without a promotion change the main action.

### monthly-event-response (story events)

Purpose: choose one option of a story event.

- Infer each option's effect on the visible statistics from the lessons in earlier notes and the handbook vocabulary (overwork costs Health, learning raises Skill and costs Health, helping colleagues raises Network, delivering raises Output, standing up for yourself protects Dignity). In our runs, options that put work down usually cost a point of Output.
- Mark the options that bury hidden risk: venting or coasting in protest; favours and back channels; lying, denying or covering up; hiding a health problem; shortcuts and tweaked results, including accepting a known security flaw for later; leaking, gossip and blame. Owning a mistake, apologising, telling the whole truth through the proper channel and declining with an alternative lower it.
- Remove marked options and options that break the floor. If nothing is left, keep the least damaging option and flag it.
- Push mode prefers the option that raises an open driver; rebuild mode prefers the option with no cost. In guard months an option that lowers Output, Skill or Network is not chosen when another option keeps them, and a driver that has slipped is raised by the next option that can. While risk is high or after a blow-up, the option that owns the problem and puts it on the record comes first.

### quarterly-resource-planner (quarterly phase)

Purpose: spend the three Energy points and choose the main action.

- The first note of the phase starts with three fields filled from observed values: Ledger, Forecast to the next review, and Defuse gap.
- Energy, in order: bring Health or Dignity back to the floor, and at the phase just before the guard months buy one point of Health unless Health is safe; Defuse legacy risk when a trigger holds; in the phases at the end of months 45 and 48, recovery up to the top of the scale; then the open drivers, the one that rose least last quarter first. When all three drivers are capped, Health and Dignity go to the safe band, risk is defused, and the points left go to Skill learning, because the menu says unused Energy does not roll over. High-intensity work is not used: its own menu text says it raises hidden risk.
- Main action, first rule that applies: Lay low and reduce risk when Health is below the floor, risk is high, or in the two quarters after a blow-up; Repair a key relationship when Dignity is below the floor; Apply for rotation when Network and Output are capped and Skill is open, or when all three are capped (switching to a key project after two windows at the level without a promotion); Build a mentorship when only Network is open; otherwise Apply for a key project, because its menu effect raises all three drivers.

## 4. How the outputs combine

1. observe returns the state and the next event.
2. career-state-triage writes the card.
3. A story event goes to monthly-event-response; the quarterly phase goes to quarterly-resource-planner. Both read the card.
4. take_action sends the choice with a short English note that carries the expectation and, at the start of a quarter, the three fixed fields. take_action only reports success, so the agent calls observe once and the loop starts again.

The notes are the agent's memory across months. The ledger with recorded caps, the defuse gap, the expectations and the lessons are all written there, so the next card can check them.

## 5. Why no scripts or reference files

The decisions are judgements over natural-language events. A script cannot classify an event better than the model, and the menu already carries the exact effect and price of every action. The one piece of arithmetic the agent needs, comparing a driver with its recorded cap, is a single comparison the model does in its note. Everything fits in plain instructions, and leaving out executable content keeps the submission simple to review and inside the rules.
