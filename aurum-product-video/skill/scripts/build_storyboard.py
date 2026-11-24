"""Build the formatted XLSX storyboard from the Product Video agent's JSON.

Usage: python build_storyboard.py runs/<slug>/05_storyboard.json [out.xlsx]
"""
import json
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

COLS = [
    ("scene", "Scene #", 7),
    ("timecode", "Timecode", 11),
    ("shot", "Shot / Visual Description", 38),
    ("image_prompt", "Image Generation Prompt", 55),
    ("i2v_prompt", "Image-to-Video Prompt", 45),
    ("voice_prompt", "Voice Generation Prompt", 38),
    ("dialogue", "Dialogue / Voiceover", 40),
    ("caption", "On-Screen Caption", 26),
    ("localization", "Localization Notes (DE / US / JP)", 40),
]


def main() -> None:
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".xlsx")
    scenes = json.loads(src.read_text(encoding="utf-8"))
    if len(scenes) != 12:
        raise SystemExit(f"expected 12 scenes, got {len(scenes)}")

    wb = Workbook()
    ws = wb.active
    ws.title = "Storyboard"
    head_fill = PatternFill("solid", fgColor="2F5597")
    thin = Side(style="thin", color="BFBFBF")
    border = Border(left=thin, right=thin, top=thin, bottom=thin)

    for c, (_, title, width) in enumerate(COLS, start=1):
        cell = ws.cell(row=1, column=c, value=title)
        cell.font = Font(bold=True, color="FFFFFF", size=12)
        cell.fill = head_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border
        ws.column_dimensions[cell.column_letter].width = width
    ws.row_dimensions[1].height = 36

    for r, scene in enumerate(scenes, start=2):
        for c, (key, _, _) in enumerate(COLS, start=1):
            cell = ws.cell(row=r, column=c, value=scene.get(key, ""))
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            cell.border = border
        ws.row_dimensions[r].height = 190
    ws.freeze_panes = "C2"
    wb.save(out)
    print(f"wrote {out} ({len(scenes)} scenes)")


if __name__ == "__main__":
    main()
