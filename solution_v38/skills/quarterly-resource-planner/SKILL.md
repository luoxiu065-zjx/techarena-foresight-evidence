---
name: quarterly-resource-planner
description: Spends the three quarterly Energy points and chooses the quarterly main action from the status card - this year's Health and Dignity floor first, a defuse on a fixed count of quarters, open promotion drivers next, and nothing spent on a capped driver except Energy that would otherwise be lost. Use in the quarterly energy-action phase and the main-action choice, after career-state-triage.
---

# Quarterly resource planner

## When to use
When observe shows the quarterly energy-action phase or the main-action choice, after career-state-triage.

## Turn rule
The plan is internal. Every decision ends with take_action in the same turn. At the quarterly phase after each review (end of months 6, 12, ..., 42), load the three Skills again before the first quarterly decision.

## Procedure
1. Read the menu. Its status_updates and energy_cost give the exact effect and price of every action; use them, not memory. The same action may be chosen more than once within 3 points.
2. The first take_action note of the phase starts with three fields, filled only from the ledger and the observed values: "Ledger: <each driver: open with its value, or capped at its recorded value and level>; Forecast to m<next review>: <each open driver reached, close or far>, risk <low, rising or high>; Defuse gap: <quarterly phases since the last Defuse legacy risk>."
3. Energy, in this order:
   1. Floor: Health below this year's floor (career-state-triage step 4) takes Health recovery until it is at the floor or above; Dignity below the floor takes Mental recovery. At the quarterly phase just before the guard months (end of months 3, 9, 15 and so on), if this step has not bought any Health recovery, buy exactly one point of Health recovery, unless Health is already in the safe band; the other points follow the steps below.
   2. Defuse legacy risk, when any of these holds:
      - the risk estimate is high (a new HR step of 2 or above, or three story signs, since the last defuse); the defuse gap then counts again from this defuse;
      - the estimate is rising and the drivers for the next window are capped or reachable with the remaining point;
      - before the first promotion, the quarterly phase right after a review that passed without a promotion, whatever the HR remark says: the remark can stay calm for months while risk builds up;
      - from the first promotion on, the defuse gap has reached 2, whatever the HR remark says and even before a window;
      - the quarterly phases at the end of months 45 and 48.
   3. End of the run: in the quarterly phases at the end of months 45 and 48, the points left after steps 1 and 2 go to Health recovery and Mental recovery, the lower of the two first, up to the top of the scale. Health and Dignity count in the ending score. Steps 4 and 5 apply only to points still left after that.
   4. Push: the remaining points go to open drivers, the one that rose least last quarter first: Network maintenance for Network, Prepare report materials for Output, Skill learning for Skill if Health stays at the floor or above. A driver open because it is below its recorded cap gets only the points that bring it back to that value. High-intensity work is not used: its own menu text says it raises HiddenRisk.
   5. Rebuild (all drivers capped): Health recovery and Mental recovery up to the safe band (70% of the top), then Defuse legacy risk, then Skill learning with the points left if Health stays at the floor or above. Reserve only points that none of these can use: the menu says reserved Energy does not roll over. Skill counts in the ending score, and a Skill that rises above its recorded cap is open again.
   6. Never buy recovery past the top of the scale, and never buy growth for a capped driver except Skill learning with the points left in step 5.
4. Main action, the first rule that applies:
   1. Health below this year's floor, the risk estimate high, or the two quarters after a blow-up: Lay low and reduce risk (its menu effect lowers HiddenRisk and restores Health). A remark that stays at the same step after a defuse is not high, so it does not keep this rule on; the next quarter goes back to the rules below.
   2. Dignity below this year's floor: Repair a key relationship (its menu effect raises Dignity and Network).
   3. Network and Output both capped and Skill open: Apply for rotation. Only Network open: Build a mentorship. All three capped: Apply for rotation (its menu effect raises Skill and Network); if the last two review windows at this level both passed without a promotion while rotation was the main action, Apply for a key project instead.
   4. Otherwise, in every quarter including the one before a review: Apply for a key project, because its menu effect raises all three drivers at once.
   5. End of month 48: Build a mentorship if Network is open, otherwise Lay low and reduce risk.
5. Every other take_action note in the phase is one sentence: the action, the target driver and "expect <statistic> <+n or -n>".

## Check before each take_action
- No point on a capped driver except Skill learning with the points left in rebuild; no recovery past the top; in the phases at the end of months 45 and 48, Health and Dignity recovery comes before growth.
- A review just passed without the first promotion, or the defuse gap at 2 or more after the first promotion, or the HR remark at a new step of 2 or above since the last defuse: Defuse legacy risk is in this quarter's plan.
- Health and Dignity stay at the floor or above after the action (30%, 40% or 50% of the top by year; 1 point lower in guard months only for an option that keeps Output, Skill or Network).
- After take_action, observe once.
