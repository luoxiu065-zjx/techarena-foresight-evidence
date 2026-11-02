# Skills design - foresight-v37-ladder

## Why three Skills and a manifest

The game has two kinds of decision points - a monthly story event with options, and a quarterly phase with Energy actions and one main action - and both need the same reading of the state first. The three Skills follow that shape: one reads the state (career-compass), one chooses story options (story-option-choice), one plans the quarter (quarter-plan). The manifest holds the rules that must hold for all 48 months, because in our runs a rule that lived only in a Skill was followed early and forgotten once the context held months of game text. The manifest also tells the agent to reload the three Skills after every half-year review, as a tool call.

## career-compass

Purpose: turn the observe result into three decisions-before-the-decision: stage, target and repair items.

Information used: the visible statistics, level and months at level, the monthly feed (salary, HR remark, review grade, promotion, warnings), the menu when it is shown, and the agent's own last note.

Output: two or three internal lines. Stage is set from level and calendar (entry until the first promotion, climb, senior after twelve months at a level following two promotions, final year from month 37). The ledger marks each driver open or at its ceiling by watching movement across two quarterly phases; the target is the open driver that rose least, except that from the senior stage on Skill comes first. Repair items (Health or Dignity low, Health in watch, Wealth negative, Network at zero, hidden risk due, the month before a review) override the target.

## story-option-choice

Purpose: pick one option from the event's wording.

Information used: the event text and options, the target and repair items from career-compass, and the lessons the agent wrote in earlier notes.

Procedure: infer each option's effect from its wording, mark the options that bury hidden risk, remove the marked ones and the ones that cost Health while Health is not healthy, then choose the option that raises the target at no cost. Two reading patterns observed in our runs are stated as patterns, not as answers: options that put work or people down tend to cost a driver even when they sound sensible, and options that do the work together tend to keep or raise the drivers. The integrity section keeps the agent on the proper channel without steering it into the self-protective options that cost it points at the entry level.

## quarter-plan

Purpose: spend the three Energy points and pick the main action.

Information used: the menu's listed effects and prices (status_updates, energy_cost), the ledger, the stage, the defuse schedule and the calendar.

Procedure: recovery to the band first (plus one Health point before any review month unless Health is healthy, because the review uses the state before the review month), the scheduled defuse second, end-of-run recovery at months 45 and 48, then growth on open drivers with Skill first from the senior stage. The main action follows the stage: mentorship or key project at entry, rotation in the senior stage and final year, key project otherwise, and the protective actions (lay low, repair a relationship) only on the named repair items.

## How the outputs combine

career-compass produces stage, target and repair items; the other two Skills consume them and never re-derive them. The manifest rules bind all three: a story option or an Energy action that breaks a whole-run rule is not available to either Skill, whatever the local reasoning says. Every take_action note starts with the expected change, so career-compass can compare expectation with outcome at the next decision and write a lesson that outranks the general reading rules.
