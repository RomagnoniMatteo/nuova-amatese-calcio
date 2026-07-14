import json, re, os

BASE = os.path.dirname(__file__)
OUT = os.path.join(BASE, "..", "src", "data")
os.makedirs(OUT, exist_ok=True)

MONTHS = {
    "gennaio": 1, "febbraio": 2, "marzo": 3, "aprile": 4, "maggio": 5,
    "giugno": 6, "luglio": 7, "agosto": 8, "settembre": 9, "ottobre": 10,
    "novembre": 11, "dicembre": 12,
}

def date_to_iso(day, month_name, year):
    m = MONTHS[month_name.lower()]
    return f"{year:04d}-{m:02d}-{int(day):02d}"

def season_year(month_name):
    # Season runs June(2026) .. April(2027)
    m = MONTHS[month_name.lower()]
    return 2026 if m >= 6 else 2027

def clean_text(text):
    text = re.sub(r"^\*{1,2}\s*", "", text)
    text = re.sub(r"\*\(([^)]*)\)\*", r"(\1)", text)
    text = re.sub(r"\*{1,2}", "", text)
    return text.strip()

def parse_dialogue_lines(lines):
    script = []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        # stage direction block on its own line: **[...]** or [...]
        stage_match = re.match(r"^\*{0,2}\[(.+)\]\*{0,2}$", line)
        if stage_match:
            script.append({"type": "stage", "text": stage_match.group(1).strip()})
            continue
        # dialogue line: -> or → then SPEAKER: text  (speaker may be **bold**)
        m = re.match(r"^(?:→|->)\s*\*{0,2}([^:*]+?)\*{0,2}\s*:\s*(.*)$", line)
        if m:
            speaker = m.group(1).strip()
            text = clean_text(m.group(2).strip())
            script.append({"type": "line", "speaker": speaker, "text": text})
            continue
        # continuation line (wrapped dialogue, no arrow) -> append to previous line's text
        if script and script[-1]["type"] == "line":
            script[-1]["text"] += " " + clean_text(line)
        else:
            script.append({"type": "note", "text": line})
    return script

def parse_story(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    blocks = [b.strip() for b in content.split("###") if b.strip()]
    episodes = []
    for block in blocks:
        lines = block.splitlines()
        date_line = lines[0].strip()
        title_line = lines[1].strip()
        body_lines = lines[2:]

        dm = re.match(r"^(\d{1,2})\s+([A-Za-zàèéìòù]+)$", date_line)
        day, month_name = dm.group(1), dm.group(2)
        year = season_year(month_name)
        iso = date_to_iso(day, month_name, year)

        tm = re.match(r"^X?\s*##\s*(\d+)\.\s*(.+)$", title_line)
        number = int(tm.group(1))
        title = tm.group(2).strip()

        script = parse_dialogue_lines(body_lines)

        episodes.append({
            "id": f"ep-{number:02d}",
            "number": number,
            "date": iso,
            "title": title,
            "instagramUrl": None,
            "script": script,
        })
    episodes.sort(key=lambda e: e["number"])
    return episodes

def parse_podcasts(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    blocks = [b.strip() for b in content.split("###") if b.strip()]
    podcasts = []
    for i, block in enumerate(blocks, start=1):
        lines = block.splitlines()
        header = lines[0].strip()
        iso, title = [p.strip() for p in header.split("|", 1)]
        body_lines = lines[1:]
        script = parse_dialogue_lines(body_lines)
        podcasts.append({
            "id": f"pod-{i:02d}",
            "date": iso,
            "title": title,
            "script": script,
        })
    podcasts.sort(key=lambda p: p["date"])
    return podcasts

episodes = parse_story(os.path.join(BASE, "story.txt"))
podcasts = parse_podcasts(os.path.join(BASE, "podcasts.txt"))

# Preserve instagramUrl values a human already filled in, in case this script
# is re-run after story.txt changes (regenerating would otherwise wipe them).
episodes_out_path = os.path.join(OUT, "episodes.json")
if os.path.exists(episodes_out_path):
    with open(episodes_out_path, encoding="utf-8") as f:
        existing = {e["id"]: e.get("instagramUrl") for e in json.load(f)}
    for e in episodes:
        if existing.get(e["id"]):
            e["instagramUrl"] = existing[e["id"]]

with open(episodes_out_path, "w", encoding="utf-8") as f:
    json.dump(episodes, f, ensure_ascii=False, indent=2)

with open(os.path.join(OUT, "podcasts.json"), "w", encoding="utf-8") as f:
    json.dump(podcasts, f, ensure_ascii=False, indent=2)

print(f"episodes: {len(episodes)}, podcasts: {len(podcasts)}")
for e in episodes:
    print(e["number"], e["date"], e["title"], "-", len(e["script"]), "righe")
