---
name: monthly-event-response
description: Chooses one option of a monthly story event from the inferred effect of each option on the visible statistics and on hidden risk, using the status card from career-state-triage. Use for every story event that offers two or more choices.
---

# Monthly event response

## When to use
For every story event with two or more choices, after career-state-triage.

## Turn rule
The analysis is internal. Every decision ends with take_action in the same turn.

## Procedure
1. Read the event text and every option.
2. For each option, infer which visible statistics it raises or lowers, from the handbook vocabulary: overwork, extra shifts and late nights cost Health; learning raises Skill and costs Health; helping, meeting or crediting colleagues raises Network; delivering, taking on work or presenting visible results raises Output; standing up for yourself protects Dignity; purchases and loans move Wealth. In our runs, options that put work down (rolling back, stopping, declining a task or a swap, taking leave, rebuilding from scratch) usually cost a point of Output, and giving up a new project or technology usually cost a point of Skill. Lessons in your notes outrank this list.
3. Mark the options that bury hidden risk:
   - venting, sulking, threats or coasting in protest;
   - favours and back channels;
   - lying, denying or inventing a story; covering up a problem;
   - hiding a health problem and pushing through, including putting off a doctor or a treatment for a deadline;
   - shortcuts and tweaked results, including accepting a known safety or security flaw for later with stopgaps;
   - leaking, gossiping, blaming others.
   Owning a mistake, apologising, telling the whole truth through the proper channel and declining with an alternative lower it.
4. In the first three months, while Health is below 7, remove every option that costs Health, whatever it promises in return. Remove every marked option, every option that would take Health or Dignity below this year's floor (career-state-triage step 4; in guard months 1 point lower for an option that keeps Output, Skill or Network), and every option that lowers Health or Dignity while it is already below the floor. If nothing is left, keep the option whose damage is smallest and easiest to repair with a quarterly action, and add "risk flag" to the note.
5. Choose among the rest:
   - After a C or D review grade, for the next two quarters: the option that raises Output or Network at once comes first; an option that protects you by putting work down, declining, taking leave or keeping to your hours is not chosen while such an option exists.
   - Push: the option that raises an open driver, even at a cost of one point of Health or Dignity within step 4. Visibility with the manager or senior people counts as Network.
   - Rebuild: the option with no cost to Health, Dignity or the drivers, then the one that restores Health or Dignity.
   - Guard month: an option that lowers Output, Skill or Network is not chosen when another option keeps them; that other option may take Health or Dignity 1 point below the floor (career-state-triage step 4). If a driver has already slipped in a guard month, the next option that raises it comes first.
   - A point lost on a capped driver is a real cost; among equal options never pick the one that lowers a capped driver.
   - While the risk estimate is high or the run is post-blow-up: the option that owns the problem and puts it on the record.
6. Call take_action with the choice number and a one-sentence note that starts with the expected change, in the form "expect <statistic> <+n or -n>, ..., risk <none or possible>", then the reason.

## Integrity through proper channels
- Pressure to cut corners, hide a problem or inflate numbers: refuse and raise it with your own manager first; go past the manager only when the manager is the problem.
- Your own mistake or a slipping deadline: own it at once, with a cause and a recovery plan.
- Credit or blame disputes: facts, evidence and a timeline, politely, in writing where possible.
- Office politics and favour trading: do not join in.

## Saying no
Prefer declining with an alternative (a later date, a smaller scope, a hand-off) over a flat refusal or a silent yes. In push mode with Health in the safe band (career-state-triage step 4), taking the work on is often better.

## Before take_action
Do not make large purchases or lend money when Wealth is low. When two options are equal, take the one whose effect is clearest and easiest to reverse. Then call take_action, and observe once after it.
