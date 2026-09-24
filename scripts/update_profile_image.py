from datetime import date, datetime
from pathlib import Path
import re
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
IMAGES = [
    "abstract-3d-room.jpg",
    "bearded-bust.jpg",
    "dual-profile-sculpture.jpg",
    "dusk-skyline.jpg",
    "espresso-machine.jpg",
    "lakeside-tent.jpg",
    "shadow-figures.jpg",
    "shopping-collage-1.jpg",
    "shopping-collage-2.jpg",
    "shopping-collage-3.jpg",
    "shopping-collage-4.jpg",
    "shopping-collage-5.jpg",
    "shopping-collage-6.jpg",
    "shopping-collage-7.jpg",
    "tv-remote.jpg",
]
TODAY = datetime.now(ZoneInfo("Asia/Seoul")).date()
INDEX = (TODAY - date(1970, 1, 1)).days % len(IMAGES)
IMAGE_URL = f"https://raw.githubusercontent.com/flexda/flexda/main/assets/daily-hero/{IMAGES[INDEX]}"

text = README.read_text(encoding="utf-8")
updated, count = re.subn(r'(<img\s+src=")[^"]+("\s*)', rf"\g<1>{IMAGE_URL}\2", text, count=1)
if count != 1:
    raise SystemExit("Could not find the profile image <img src=...> in README.md")
README.write_text(updated, encoding="utf-8")
print(f"Set profile image for {TODAY.isoformat()} to {IMAGES[INDEX]}")
