import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "Source"
OUTPUT_DIR = ROOT / "Output"

VARIANTS = {
    "screen": (SOURCE_DIR / "Fechtfibel-screen.tex", "Fechtfibel-screen.pdf"),
    "paper": (SOURCE_DIR / "Fechtfibel-paper.tex", "Fechtfibel-paper.pdf"),
}

def build_variant(name: str) -> Path:
    source_file, output_name = VARIANTS[name]
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            "latexmk",
            "-pdf",
            "-interaction=nonstopmode",
            "-quiet",
            "-output-directory=../Output",
            source_file.name,
        ],
        cwd=SOURCE_DIR,
        check=True,
    )

    pdf_path = OUTPUT_DIR / output_name
    if not pdf_path.exists():
        raise FileNotFoundError(f"Expected PDF was not created: {pdf_path}")
    return pdf_path

def main() -> None:
    parser = argparse.ArgumentParser(description="Build the screen and paper PDF variants of Fechtfibel.")
    parser.add_argument(
        "--variant",
        choices=sorted(VARIANTS),
        action="append",
        dest="variants",
        help="Variant to build. Repeat to build more than one variant.",
    )
    args = parser.parse_args()

    variants = args.variants or list(VARIANTS)
    for variant in variants:
        print(f"Building {variant} variant...")
        build_variant(variant)

if __name__ == "__main__":
    main()
