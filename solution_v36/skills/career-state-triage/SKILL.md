---
name: career-state-triage
description: Builds a short internal status card from the latest observe result - which of Skill, Network and Output can still grow at this level, how much Health and Dignity can be spent, a hidden-risk estimate with the quarters since the last defuse, and the months to the next half-year review. Use first at every decision point, before choosing a story option or a quarterly action.
---

# Career state triage

## When to use
At every decision point, right after observe has returned the current state.

## Turn rule
The card is internal reasoning, not a reply. Every decision ends with a tool call in the same turn; a decision written as text is not a decision.

## Procedure
1. Read the latest observe result: the visible statistics, the month, the monthly feed (salary, HR remark, review grade, promotion, warnings) and your own earlier notes. Never use a value from memory.
2. Ledger of the three promotion drivers (Skill, Network, Output). Each level caps them at a ceiling that is not published.
   - A driver is capped when its value at this quarterly phase is no higher than its highest value at this level two quarterly phases ago, although something in between was meant to raise it (a growth action, a main action or a story result). It stayed flat, or rose and fell back. Compare only the values written in your quarterly notes; no effect arithmetic is needed. One flat quarter is not enough.
   - When you mark a driver capped, write the highest value it reached at this level into the ledger, in the form "<driver> capped at <value>, L<level>". That value is the recorded cap of this driver at this level. It comes from this run's own observe results only.
   - At the same level, compare the current value with the recorded cap at every decision; no Energy is spent only to test a cap:
     - below the recorded cap: open again (a story result or a slip took it down); growth for it counts until it is back at the recorded cap;
     - above the recorded cap: it was not capped; it is open again and the recorded cap is dropped;
     - at the recorded cap: capped.
   - Every driver that is not capped is open. After a promotion all three are open again and the recorded caps of the old level no longer apply; record new ones as they are found at the new level.
   - Decide that a driver is capped only from this comparison across two quarterly phases, never from a single value. The recorded cap is used only afterwards, at the same level, in the comparison above.
3. Mode. Push when at least one driver is open; rebuild when all three are capped.
4. Health and Dignity bands (our own policy, not a game threshold). Read the top of each scale from the handbook (show_employee_handbook); if the handbook gives no top, use the 0-10 range in this competition's public documentation. Every band is a share of that top, rounded up to a whole point. An early promotion raises salary and level for every later month, so the floor is lowest at the start and rises by year.
   - Safe band: 70% of the top or more. Nothing needs managing.
   - Floor: 30% of the top in months 1-12, 40% in months 13-24, 50% from month 25.
   - Guard months (career-state-triage step 6): the floor is 1 point lower, but only for an option that keeps Output, Skill or Network when the other options lower one of them.
   A choice may spend Health or Dignity only if it stays at the floor or above. Below the floor, only recovery and options with no cost to it are allowed. When the floor rises at month 13 or 25, a statistic below the new floor is brought back up first.
5. Hidden-risk estimate: low, rising or high.
   - HR remark, five steps from calm to alarm: (0) "doing all right lately"; (1) "some risk lately, but it isn't serious yet"; (2) "the risks have piled up"; (3) "you're on your own now"; (4) "everything you buried is about to go off".
   - Story signs: an option of the risky kinds in monthly-event-response was chosen, a note carries "risk flag", or a thread came back after such a choice.
   - High: since the last Defuse legacy risk, the remark has reached step 2 or a higher step, or three or more story signs have appeared. Rising: since the last defuse, one or two story signs, or the remark rose from step 0 to step 1. Low: neither.
   - After a defuse, a remark that stays at the same step does not raise the estimate by itself, because the remark lags; the defuse gap decides the next defuse. Only a new step or new story signs make the estimate high again.
   - The remark can lag: in our runs it stayed at step 0 for months before a blow-up, and a calm remark at the end did not mean nothing was left. Count the defuse gap: quarterly phases since the last Defuse legacy risk. A blow-up does not reset it.
   - After a blow-up, the next two quarters are post-blow-up: add no new risk.
6. Time: months to the next quarterly phase and to the next review (months 6, 12, 18 and so on). In our runs the review used the state at the end of the month before, so the two months before each review (months 4-5, 10-11 and so on) are guard months in which no quarterly action can repair a lost point.
7. Expectation check: compare the expectation in your last note with what changed. On a miss, add one short lesson to the next note naming the kind of option or action and its real effect, never the event's name. Earlier lessons outrank the general vocabulary in monthly-event-response.

## Output (internal, two or three lines)
Mode, open drivers and recorded caps; Health and Dignity room above this year's floor; risk estimate with the defuse gap and "post-blow-up" when it applies; months to the next review and whether this is a guard month.

## Priorities near a limit
- Health or Dignity below the floor in two observations in a row outranks everything else.
- After a C or D grade, or a warning-tone half-year talk, the open drivers come first for the next two quarters, in story choices as well as in Energy: one more weak review can end the run.
- Two promotion windows at the same level without a promotion: change the main action pattern instead of repeating it (quarterly-resource-planner main action rule 3).
- Output is needed for promotion but is not scored at the end and drops easily; Network and Skill are both. In our runs the upper levels asked for much more Skill and more months at the level, so Skill stays worth raising long after Network and Output are capped.
- At L1 the windows at months 6 and 12 count most: a run still at L1 after month 12 seldom recovers.
