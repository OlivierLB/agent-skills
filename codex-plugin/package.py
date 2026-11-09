#!/usr/bin/env python3
"""Build a Codex directory ZIP from the canonical Decision Review skill."""

import argparse
import json
import shutil
import tempfile
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE = Path(__file__).resolve().parent
MANIFEST = PACKAGE / ".codex-plugin" / "plugin.json"
ICON = PACKAGE / "assets" / "decision-review.svg"
SKILL = ROOT / "skills" / "productivity" / "decision-review" / "SKILL.md"


def validate(manifest):
    for field in ("name", "version", "description", "author", "interface"):
        if not manifest.get(field):
            raise SystemExit(f"Manifest field is required: {field}")
    if not manifest["author"].get("name"):
        raise SystemExit("Manifest field is required: author.name")
    if not isinstance(manifest.get("skills"), str):
        raise SystemExit("Manifest field 'skills' must point to the packaged skill directory.")
    interface = manifest["interface"]
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category", "capabilities", "composerIcon", "logo"):
        if field not in interface:
            raise SystemExit(f"Manifest field is required: interface.{field}")
    if len(interface["displayName"]) > 30:
        raise SystemExit("interface.displayName must be 30 characters or fewer.")
    if len(interface["shortDescription"]) > 30:
        raise SystemExit("interface.shortDescription must be 30 characters or fewer.")
    if len(interface["longDescription"]) > 4000:
        raise SystemExit("interface.longDescription must be 4000 characters or fewer.")
    if not isinstance(interface["capabilities"], list):
        raise SystemExit("interface.capabilities must be a list.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path, help="Destination ZIP path")
    args = parser.parse_args()

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Create the plugin manifest first: {MANIFEST}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {MANIFEST}: {exc}")

    validate(manifest)
    for asset_field in ("composerIcon", "logo"):
        asset_path = (PACKAGE / interface_path(manifest, asset_field)).resolve()
        if not asset_path.is_file() or PACKAGE.resolve() not in asset_path.parents:
            raise SystemExit(f"Missing or out-of-package asset: {asset_path}")
    if not SKILL.is_file() or not ICON.is_file():
        raise SystemExit("The canonical skill or package icon is missing.")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="decision-review-package-") as temp_dir:
        stage = Path(temp_dir)
        (stage / ".codex-plugin").mkdir()
        (stage / "skills" / "decision-review").mkdir(parents=True)
        (stage / "assets").mkdir()
        shutil.copy2(MANIFEST, stage / ".codex-plugin" / "plugin.json")
        shutil.copy2(SKILL, stage / "skills" / "decision-review" / "SKILL.md")
        shutil.copy2(ICON, stage / "assets" / ICON.name)
        with zipfile.ZipFile(args.output, "w", zipfile.ZIP_DEFLATED) as archive:
            for file_path in sorted(stage.rglob("*")):
                if file_path.is_file():
                    archive.write(file_path, file_path.relative_to(stage).as_posix())
    print(args.output.resolve())


def interface_path(manifest, field):
    value = manifest["interface"][field]
    if not isinstance(value, str) or not value.startswith("./"):
        raise SystemExit(f"interface.{field} must be a package-relative path beginning with './'.")
    return value[2:]


if __name__ == "__main__":
    main()
