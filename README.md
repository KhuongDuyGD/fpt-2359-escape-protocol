# FPT: 23:59 Escape Protocol

A complete Ren'Py visual novel based on `VisualNovelContent.txt`. The Vietnamese
dialogue and jokes follow the supplied screenplay. Generated placeholder PNGs
and WAV cues are included, so there are no missing asset paths.

## Run

Open this folder as a project in Ren'Py 8.x and choose **Launch Project**. The
project uses a 1280×720 virtual resolution. Ren'Py itself is not included.

To use this inside another normal Ren'Py project, copy the entire `game` folder
and replace that project's starter `script.rpy`, `screens.rpy`, and `options.rpy`
with the files here. Avoid keeping duplicate screen or label definitions.

## Controls

- Click, Enter, or Space: advance dialogue
- Mouse wheel up, Page Up, or **Back**: rollback
- **Skip** and **Auto**: quick menu under dialogue
- **Save**, **Load**, **History**, **Prefs**: quick menu under dialogue
- Esc or right click: game menu

The Ending Gallery on the main menu records endings across playthroughs. Both
endings offer **Return to Main Menu** and **Start New Game+**. New Game+ resets
the starting stats and shows “Difficulty Unlocked: SENIOR YEAR.”

## Files

- `game/script.rpy`: prologue, scenes, choices, and route checks
- `game/variables.rpy`: story stats, flags, gallery state, ending condition
- `game/characters.rpy`: cast and image declarations
- `game/screens.rpy`: HUD, dialogue, menus, gallery, ending cards
- `game/endings.rpy`: both endings and New Game+
- `game/audio.rpy`: sound cue names and flash transition
- `game/options.rpy`: project settings
- `tools/generate_placeholders.py`: reproducible placeholder assets

## Tuning the routes

Choice deltas are next to their menu entries in `game/script.rpy`. The GOOD
ENDING requires choosing **ĐI VỀ.**, `escape_point >= 4`, `energy > 0`, and
`pending_tasks <= 2`. Choosing to stay, running out of energy, reaching six
pending tasks, or attempting to leave without the required stats enters the
BAD ENDING route. The screenplay's morning attendance is recorded on arrival;
the late assignment adds one pending task and is marked uploaded in the night
route. The meeting's `PendingTasks -1` is clamped to zero so the HUD never shows
a negative task count.

Replace a placeholder image or sound with final art by keeping its current
filename, or update the corresponding declaration in `characters.rpy` or
`audio.rpy`.

## Verification

`game/testcases.rpy` contains Ren'Py engine tests for both endings and the
supporting menus. In a Ren'Py 8.5 SDK, run `renpy.py <project> lint --error-code`
and `renpy.py <project> test good_route` (or `bad_route` / `ui_screens`).
