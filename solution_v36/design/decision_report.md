# Decision report

Team: Foresight Agents
Submission: foresight-v36

## 1. Overall decision approach

1. Reach each review with the promotion drivers as high as the level allows. Level is 30% of the score and salary follows it. Health and Dignity may be spent for this, down to a floor that rises by year (30%, then 40%, then 50% of the scale), so the first year can push harder than the last.
2. Protect the review in the two months before it. A point of Network, Output or Skill lost in those months cannot be bought back before the review, so the agent keeps the drivers even at one point of Health or Dignity below the floor, and buys one point of Health in the Energy phase just before those months to make room for it.
3. Never pay for a driver that no longer responds. The agent learns each level's ceiling during the run by comparing each driver with its highest value two quarterly phases earlier, and records that value as the cap. A driver that later falls below the record is topped back up; one that rises above it was not capped after all.
4. Keep hidden risk low on a schedule, not on the HR remark alone. Before the first promotion, every review without a promotion is followed by a defuse. After it, two quarters without a defuse force one. An HR remark at step 2 or higher forces one at any time.
5. Do not waste the quarter. Unused Energy is lost, so when every driver is capped the spare points go to Skill learning, and in the last two quarterly phases they go to Health and Dignity, which count in the ending score.
6. Keep the rules alive for 48 months. Whole-run rules sit in the manifest instruction, which is in the system prompt on every call; the Skills are loaded again after every review.

7. Two guards for the entry level, both from counts over our logged games: in the first quarter no Health-costing story option is taken while Health is below 7 (most of our runs had burned Health to the floor by month 3 and then had to choose protective options that cost the drivers); and for two quarters after a C or D grade the story choice goes to the option that raises Output or Network at once, never to the self-protective one, because a second weak review ends the run.

## 2. Public information and in-run feedback the approach relies on

- The public handbook and documentation: levels, the visible statistics and their ranges, the review calendar, the score weights and the failure directions.
- The menu shown at every quarterly phase, with the effect and Energy price of every action and the statement that unused Energy does not roll over.
- The state from observe after every action. The expectation in each note is compared with what changed, and the recorded caps are compared with the current values.
- The HR partner's monthly remark (five published steps) and the review grades.
- The agent's own note fields: ledger with recorded caps, forecast to the next review, defuse gap, expectations and lessons.

The agent does not use event titles, event order or any unpublished number. The caps it uses are values it observed in the same run. The Health and Dignity floors are our own policy, and the Skills say so.

## 3. Principal risks

- The first windows are partly luck. Whether the month-6 and month-12 reviews promote depends on the story events of those months: some events offer no clean option that keeps every driver, and at L1 one lost point is enough to miss the window. Runs of the same version ranged from a promotion at month 6 to none at all, so a single run says little about a version.
- The run can stop before month 48. The runner allows 20 continuations, and in one run with the official model the agent began ending each turn with a short canned reply instead of a tool call, until the runner stopped the game. The manifest says that every decision ends with a tool call in the same turn; we have not found a way to rule this out completely.
- Rules fade in a long context. Every call resends the game log. After the whole-run rules moved into the manifest, the defuse schedule held to month 48 in our later runs, but the reload after each review is still missed in some runs.
- The model may misjudge a story option. A helpful-looking option often cost a point of Network or Output, and a choice that looks safe can bury risk. The lessons in the notes, the risky-kind list and the fixed defuse schedule limit the damage.
- Fixed floors. The Health and Dignity floors are fixed shares chosen from our own runs, not values the agent learns. The handbook publishes only the failure directions, not how low is too low. In an environment where events cost more, the first-year floor leaves little margin, the guard-month exception lowers it by one more point, and the Skills do not yet raise the floor when a warning appears.
- Language drift. The framework instance we used sets Chinese as its response language, and the official model often reasons in Chinese even though every deliverable and note is English. We did not see this change decisions by itself, but it makes the context longer.

## 4. How the design generalises beyond the development dataset

The rules are written in terms of the visible statistics, the menu's published effects, the month number and the kind of choice an option offers, never a particular event. The ceilings are not built in: the agent finds them in each run and records them, so a different set of ceilings or effect sizes is handled the same way. Lessons about kinds of option are learned inside the run as well. If events change wording or order, the agent still classifies the same kinds of choice. The floors, the guard months and the defuse schedule are expressed in months and shares of the published scales, so they do not depend on the development dataset either.
