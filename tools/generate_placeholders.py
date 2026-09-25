"""Generate replaceable 1280x720 scene art, character standees, and WAV cues.

Run with Python 3 and Pillow. No runtime Python dependencies are added to Ren'Py.
The generated assets are already included in this project.
"""

from pathlib import Path
import math
import struct
import wave

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1] / "game"
BG = ROOT / "images" / "backgrounds"
CH = ROOT / "images" / "characters"
AU = ROOT / "audio"
for folder in (BG, CH, AU):
    folder.mkdir(parents=True, exist_ok=True)

FONT = Path("C:/Windows/Fonts/arial.ttf")
BOLD = Path("C:/Windows/Fonts/arialbd.ttf")


def font(size, bold=False):
    source = BOLD if bold else FONT
    return ImageFont.truetype(str(source), size) if source.exists() else ImageFont.load_default()


def scene(name, sky, floor, label, kind):
    im = Image.new("RGB", (1280, 720), sky)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 480, 1280, 720), fill=floor)
    d.line((0, 480, 1280, 480), fill="#8090a4", width=6)

    if kind == "bedroom":
        d.rectangle((790, 120, 1130, 405), fill="#48618a", outline="#d6e5fc", width=8)
        d.ellipse((855, 155, 960, 260), fill="#fff0a0")
        d.rectangle((90, 410, 580, 560), fill="#30394e")
        d.rectangle((135, 350, 380, 430), fill="#7392ad")
        d.rectangle((690, 380, 1050, 430), fill="#273148")
        d.rectangle((740, 200, 985, 380), fill="#121b30", outline="#78d7ed", width=8)
        d.rectangle((770, 230, 955, 350), fill="#284963")
        d.ellipse((1060, 405, 1140, 485), fill="#ffbd70")
    elif kind == "gate":
        d.rectangle((180, 180, 1100, 530), fill="#8396a9", outline="#d9e6f5", width=9)
        d.rectangle((270, 280, 1010, 520), fill="#354b65")
        d.rectangle((505, 255, 775, 520), fill="#b0cbe0", outline="#d9e6f5", width=7)
        d.rectangle((330, 208, 950, 267), fill="#263a59")
        d.text((445, 215), "CAMPUS", font=font(38, True), fill="#ffffff")
    elif kind == "classroom":
        d.rectangle((105, 130, 760, 395), fill="#254c4a", outline="#b7d0c9", width=10)
        d.rectangle((835, 110, 1150, 380), fill="#86a7c2", outline="#d5e7f3", width=8)
        for x in (125, 490, 855):
            d.polygon([(x, 520), (x + 260, 520), (x + 325, 590), (x - 50, 590)], fill="#566a7a")
    elif kind == "hallway":
        for x in range(105, 1200, 245):
            d.rectangle((x, 80, x + 150, 475), fill="#53708c", outline="#bed6ec", width=8)
            d.ellipse((x + 115, 285, x + 130, 300), fill="#f8cf84")
        d.line((0, 690, 640, 490, 1280, 690), fill="#95a4b9", width=5)
    elif kind == "canteen":
        d.rectangle((100, 160, 1180, 340), fill="#6d8d8c")
        d.rectangle((150, 310, 1130, 480), fill="#ac865c")
        for x in (250, 640, 1030):
            d.ellipse((x - 110, 505, x + 110, 565), fill="#d8bd87")
            d.rectangle((x - 90, 560, x - 70, 680), fill="#6f5945")
            d.rectangle((x + 70, 560, x + 90, 680), fill="#6f5945")
    elif kind == "lab":
        for x in (120, 440, 760, 1080):
            d.rectangle((x - 95, 285, x + 95, 455), fill="#101d32", outline="#8ca7c0", width=8)
            d.rectangle((x - 75, 310, x + 75, 420), fill="#176269")
            d.rectangle((x - 135, 450, x + 135, 490), fill="#7e8798")

    # Small environmental label makes each generated background identifiable.
    d.rounded_rectangle((28, 22, 430, 77), radius=14, fill="#111827bf")
    d.text((47, 33), label, font=font(28, True), fill="#f3f6fc")
    im.save(BG / f"{name}.png", optimize=True)


scene("bedroom_morning", "#566f96", "#354456", "BEDROOM • MORNING", "bedroom")
scene("school_gate", "#8fbad2", "#6b8790", "SCHOOL GATE", "gate")
scene("classroom", "#a9b5b2", "#697474", "CLASSROOM", "classroom")
scene("hallway", "#7d93ac", "#687c91", "HALLWAY", "hallway")
scene("canteen", "#d1b789", "#80745d", "CANTEEN", "canteen")
scene("computer_lab", "#637c8e", "#485667", "COMPUTER LAB", "lab")
scene("classroom_evening", "#9a797d", "#665360", "CLASSROOM • EVENING", "classroom")
scene("school_night", "#172646", "#243247", "SCHOOL • 23:59", "gate")
scene("bedroom_gaming", "#222a53", "#2d2542", "BEDROOM • RGB ON", "bedroom")


def character(name, label, coat, skin="#f4c7a3", skeleton=False):
    im = Image.new("RGBA", (450, 690), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    outline = "#152033"
    if skeleton:
        d.ellipse((150, 55, 300, 205), fill="#eee9db", outline=outline, width=7)
        d.ellipse((178, 115, 202, 135), fill=outline)
        d.ellipse((248, 115, 272, 135), fill=outline)
        d.polygon([(222, 138), (205, 164), (239, 164)], fill=outline)
        for y in range(255, 480, 30):
            d.arc((130, y, 320, y + 85), 185, 355, fill="#eee9db", width=8)
        d.line((225, 205, 225, 510), fill="#eee9db", width=17)
        limb = "#eee9db"
    else:
        d.ellipse((145, 48, 305, 208), fill=skin, outline=outline, width=7)
        d.pieslice((143, 42, 308, 175), 180, 360, fill="#1d2738")
        d.ellipse((185, 127, 199, 141), fill=outline)
        d.ellipse((252, 127, 266, 141), fill=outline)
        d.arc((200, 135, 255, 170), 0, 180, fill=outline, width=4)
        d.rounded_rectangle((105, 205, 345, 525), radius=65, fill=coat, outline=outline, width=8)
        limb = coat
    d.line((125, 265, 65, 450), fill=limb, width=36)
    d.line((325, 265, 385, 450), fill=limb, width=36)
    d.line((175, 500, 155, 640), fill=limb, width=40)
    d.line((275, 500, 295, 640), fill=limb, width=40)
    d.rounded_rectangle((72, 543, 378, 603), radius=18, fill="#101827e8")
    box = d.textbbox((0, 0), label, font=font(32, True))
    d.text(((450 - box[2]) / 2, 551), label, font=font(32, True), fill="#ffffff")
    im.save(CH / f"{name}.png", optimize=True)


character("player", "PLAYER", "#df8a49")
character("minh", "MINH", "#4795be")
character("linh", "LINH", "#9168b1")
character("thaydev", "THẦY DEV", "#4c9b78")
character("colms", "CÔ LMS", "#b34e64", skin="#e5bac3")
character("baove", "BẢO VỆ", "#b89957")
character("skeleton_player", "PLAYER", "#eeeeee", skeleton=True)


def cue(name, notes, duration=0.17, volume=0.27):
    rate = 22050
    samples = []
    for frequency in notes:
        count = int(rate * duration)
        for index in range(count):
            edge = min(1.0, index / 180, (count - index) / 280)
            tone = math.sin(2 * math.pi * frequency * index / rate)
            samples.append(int(32767 * volume * edge * tone))
        samples.extend([0] * int(rate * 0.045))
    with wave.open(str(AU / f"{name}.wav"), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(rate)
        output.writeframes(struct.pack("<" + "h" * len(samples), *samples))


cue("alarm", [880, 660, 880, 660, 880], 0.13)
cue("school_bell", [784, 784, 587], 0.28)
cue("notification", [988, 1319], 0.11)
cue("windows_update_error", [392, 330, 261], 0.16)
cue("dramatic_boss_encounter", [147, 196, 147, 110], 0.30)
cue("success_ending", [523, 659, 784, 1047], 0.22)
cue("bad_ending", [440, 349, 293, 220], 0.28)

print("Generated placeholder backgrounds, characters, and sounds in", ROOT)
