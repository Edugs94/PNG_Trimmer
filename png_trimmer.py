from pathlib import Path
from PIL import Image

class ImageTrimmer:
    def __init__(self) -> None:
        self.folder = Path("trim")

    def run(self) -> None:
        if not self.folder.exists():
            return
        for path in self.folder.glob("*.png"):
            try:
                with Image.open(path) as img:
                    img = img.convert("RGBA")
                    _, _, _, a = img.split()
                    a = a.point(lambda p: p if p > 10 else 0)
                    img.putalpha(a)
                    bbox = img.getbbox()
                    if bbox:
                        img.crop(bbox).save(path)
            except Exception:
                continue

if __name__ == "__main__":
    ImageTrimmer().run()