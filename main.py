"""One Word From Grandma.

Writes exactly one word -- the word Grandma would text about AI -- to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

"Beepboop": the sound a baffled, warm grandma makes when her grandchild
tries to explain the robots. One word, instantly readable, tied to
machines rather than any subject at all, and funny without a caption.
"""

import os

# Exactly one word, 8 characters: Grandma's baffled robot noise.
ENTRY = "Beepboop"

MAX_CHARS = 30


def main() -> None:
    text = ENTRY
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    # Judge criterion 1: exactly one word, no sentence, no punctuation tricks.
    if len(text.split()) != 1 or not text.isalpha():
        raise ValueError("entry must be exactly one word of letters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
