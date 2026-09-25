# FPT: 23:59 Escape Protocol

A complete Ren'Py visual novel based on `VisualNovelContent.txt` version 2.0.
The game now follows the new full-day screenplay, preserving its Vietnamese
dialogue, jokes, choices, and extended night route. The supplied FPTU/KTX art
is used for the cast and locations, with generated placeholder WAV cues. The
bad ending uses `MainExhaust.png`; the old skeleton image is not displayed.

## Run

Open this folder as a project in Ren'Py 8.x and choose **Launch Project**. The
project uses a 1280×720 virtual resolution. Ren'Py itself is not included.

To use this inside another normal Ren'Py project, copy the entire `game` folder
and replace that project's starter `script.rpy`, `screens.rpy`, and `options.rpy`
with the files here. Avoid keeping duplicate screen or label definitions.

## Controls

- Click, Enter, or Space: advance dialogue
- Mouse wheel up, Page Up, or **Back**: rollback
- **Skip** and **Auto**: quick menu above the dialogue box
- **Save**, **Load**, **History**, **Prefs**: quick menu above the dialogue box
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
- `tools/build_story.py`: one-time importer for this exact v2.0 screenplay
- `tools/generate_placeholders.py`: reproducible placeholder assets

## Character visibility

`screens.rpy` chooses a standee from the speaker of the current line. Only
that speaker appears. Narration and lines from characters without artwork
clear the standee automatically. The PLAYER expression changes by scene, so
the morning and night route use `MainExhaust.png`, while the successful escape
uses `MainGoodMood.png`. Story labels do not need manual `show` or `hide` calls.

## Tuning the routes

Choice deltas are next to their menu entries in `game/script.rpy`. The GOOD
ENDING requires choosing **Về.**, `escape_point >= 4`, `energy > 0`, and
`pending_tasks <= 2`. Choosing to stay, running out of energy, reaching six
pending tasks, or attempting to leave without the required stats enters the
BAD ENDING route. The screenplay's morning attendance is recorded on arrival;
the late assignment adds one pending task and is marked uploaded in the night
route. The meeting's `PendingTasks -1` is clamped to zero so the HUD never shows
a negative task count.

`characters.rpy` maps `FPTUday.png` to the daytime campus view (replacing the
missing `FPTUanime.png`). `KTXAfternoon.png` is declared for a future afternoon
dorm scene; the 18:02 ending uses `KTXNight.png`. The afternoon gate and
classroom scenes reuse their day paintings until dedicated assets exist. Extra
canteen time-of-day variants are declared for future scenes. To replace a sound
cue, update its path in `audio.rpy`.

## Verification

`game/testcases.rpy` contains Ren'Py engine tests for both endings, a failed
escape, and the supporting menus. In a Ren'Py 8.5 SDK, run
`renpy.py <project> lint --error-code` and `renpy.py <project> test`.
