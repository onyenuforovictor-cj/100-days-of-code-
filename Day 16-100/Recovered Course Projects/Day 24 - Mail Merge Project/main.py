from pathlib import Path


PLACEHOLDER = "[name]"
PROJECT_DIR = Path(__file__).resolve().parent
NAMES_FILE = PROJECT_DIR / "Input" / "Names" / "invited_names.txt"
LETTER_FILE = PROJECT_DIR / "Input" / "Letters" / "starting_letter.txt"
OUTPUT_DIR = PROJECT_DIR / "Output" / "ReadyToSend"


def main():
    names = NAMES_FILE.read_text(encoding="utf-8").splitlines()
    template = LETTER_FILE.read_text(encoding="utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for name in names:
        name = name.strip()
        if name:
            letter = template.replace(PLACEHOLDER, name)
            (OUTPUT_DIR / f"letter_for_{name}.txt").write_text(letter, encoding="utf-8")


if __name__ == "__main__":
    main()
