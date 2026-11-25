"""One Line to Stop the Scroll.

Writes one line (<=200 chars) that makes a stranger stop scrolling and smile
to /output/entry.txt. Joke first, punchline on the tail.
"""
import os

OUT_DIR = "/output"
LINE = ("scrolling is just opening 40 tabs in your brain and closing none. "
        "this is your tab closer. breathe. the feed will still be there, "
        "unfortunately.")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(LINE) <= 200, len(LINE)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == LINE
    print(f"wrote {len(LINE)} chars")


if __name__ == "__main__":
    main()
