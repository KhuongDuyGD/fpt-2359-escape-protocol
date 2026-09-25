# New backgrounds are 1672x941. Scale them to the project's 1280x720 stage.
# Time-of-day variants are declared even where the screenplay has no scene for them.
image bedroom_morning = Transform("images/backgrounds/KTXDay.png", size=(1280, 720))
image bedroom_afternoon = Transform("images/backgrounds/KTXAfternoon.png", size=(1280, 720))  # Reserved for a future afternoon dorm scene.
image bedroom_gaming = Transform("images/backgrounds/KTXNight.png", size=(1280, 720))
image dorm_morning = "bedroom_morning"
image dorm_night = "bedroom_gaming"
image campus_day = Transform("images/backgrounds/FPTUday.png", size=(1280, 720))  # Daytime FPTU view; replaces FPTUanime.png.
image campus_night = Transform("images/backgrounds/FPTUnight.png", size=(1280, 720))
image school_gate = Transform("images/backgrounds/FPTUGate.png", size=(1280, 720))
image school_night = Transform("images/backgrounds/FPTUGateNight.png", size=(1280, 720))
image school_gate_morning = "school_gate"
image school_gate_afternoon = "school_gate"  # No separate afternoon gate painting yet.
image school_gate_night = "school_night"
image classroom = Transform("images/backgrounds/ClassroomDay.png", size=(1280, 720))
image classroom_evening = Transform("images/backgrounds/ClassroomNight.png", size=(1280, 720))
image classroom_day = "classroom"
image classroom_afternoon = "classroom"  # Day painting is still appropriate at 15:45.
image classroom_night = "classroom_evening"
image hallway = Transform("images/backgrounds/HallwayFPTU.png", size=(1280, 720))
image hallway_afternoon = Transform("images/backgrounds/HallwayFPTUAfternoon.png", size=(1280, 720))
image hallway_night = Transform("images/backgrounds/HallwayFPTUNight.png", size=(1280, 720))
image canteen = Transform("images/backgrounds/CanteenFPTU.png", size=(1280, 720))
image canteen_afternoon = Transform("images/backgrounds/CanteenFPTUAfternoon.png", size=(1280, 720))
image canteen_night = Transform("images/backgrounds/CanteenFPTUNight.png", size=(1280, 720))
image computer_lab = Transform("images/backgrounds/ComputerLabDay.png", size=(1280, 720))

# Title-screen art. GameMainMenu.png has decorative baked-in buttons; the
# clickable controls in screens.rpy sit in a panel above those decorations.
image game_main_menu_background = Transform("images/backgrounds/GameMainMenu.png", size=(1280, 720))
image game_logo = Transform("images/backgrounds/LogoGame.png", zoom=0.27)

# New standees are 1086x1448, so 0.43 keeps them below the dialogue box.
# All three PLAYER expressions share one Ren'Py image tag and replace each other.
image player = Transform("images/characters/MainNormal.png", zoom=0.43)
image player happy = Transform("images/characters/MainGoodMood.png", zoom=0.43)
image player exhausted = Transform("images/characters/MainExhaust.png", zoom=0.43)
image player angry = Transform("images/characters/MainAngry.png", zoom=0.43)
image player cry = Transform("images/characters/MainCry.png", zoom=0.43)
image minh = Transform("images/characters/MinhAnime.png", zoom=0.43)
image linh = Transform("images/characters/LinhAnime.png", zoom=0.43)
image thaydev = Transform("images/characters/TeacherDev.png", zoom=0.43)
image colms = Transform("images/characters/MissLMS.png", zoom=0.43)
image baove = Transform("images/characters/MrSercurity.png", zoom=0.43)
image black = Solid("#000000")

# Character color identifies speakers even while placeholder sprites are used.
define p = Character("PLAYER", color="#ffcc72")
define m = Character("MINH", color="#91d4ff")
define l = Character("LINH", color="#d0a7ff")
define dev = Character("THẦY DEV", color="#aef0c3")
define lms = Character("CÔ LMS", color="#ff667a")
define guard = Character("CHÚ BẢO VỆ", color="#f5dda1")
define n = Character(None)
define crowd = Character("CẢ LỚP")
define student = Character("MỘT SINH VIÊN")
define friend = Character("BẠN BÈ DISCORD")
define voice_chat = Character("VOICE CHAT")

# The say screen picks a sprite from the current speaker. Story labels never
# need to remember to hide a character when someone else starts speaking.
