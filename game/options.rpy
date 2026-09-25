# Project settings. Copy the whole `game` folder into a Ren'Py 8.x project.
define config.name = "FPT: 23:59 Escape Protocol"
define config.version = "2.0"
define build.name = "FPT2359EscapeProtocol"
define config.save_directory = "FPT2359EscapeProtocol"
define config.screen_width = 1280
define config.screen_height = 720
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.check_conflicting_properties = True
define config.window_icon = "images/backgrounds/GameIcon.png"

init python:
    # Prevent local playtest ZIPs and screenshot checks entering later builds.
    build.classify("dist/**", None)
    build.classify("tests/**", None)
    build.classify("tools/**", None)
