import re
import pathlib
import unicodedata

CONTENT_DIR = "content"

def wp_slugify(title):
    # lower
    title = title.lower()

    # unicode normalize: çãé → cae
    title = unicodedata.normalize("NFKD", title)
    title = title.encode("ascii", "ignore").decode("ascii")

    # wordpress-like rules
    title = title.replace(".", "-")
    title = re.sub(r"[!?,:;]", "", title)
    title = re.sub(r"\s+", "-", title)
    title = re.sub(r"-{2,}", "-", title)

    return title.strip("-")

for md in pathlib.Path(CONTENT_DIR).rglob("*.md"):
    text = md.read_text(encoding="utf-8")

    if "slug:" in text:
        continue

    m = re.search(r'^title:\s*"(.*)"', text, re.MULTILINE)
    if not m:
        continue

    title = m.group(1)
    slug = wp_slugify(title)

    text = text.replace(
        m.group(0),
        f'{m.group(0)}\nslug: "{slug}"'
    )

    md.write_text(text, encoding="utf-8")
    print(f"OK → {md} → {slug}")

