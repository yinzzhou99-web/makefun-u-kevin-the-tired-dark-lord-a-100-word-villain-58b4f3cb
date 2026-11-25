"""The Tired Dark Lord: a 100-word villain monologue.

Writes the monologue to /output/entry.txt. Standard library only,
no network, no third-party packages. The output directory is created
if missing and is never deleted by this program.
"""

import os

TEXT = """Come in. Mind the moat \u2014 the crocodiles left years ago. Ducks live there now. They hiss at intruders. They guard better.

You want the crystal, the crown, the prophecy. Third shelf, left. Don't touch the second one. It bites.

The throne squeaks. I've meant to fix it since the second war. The second war was eighty years ago.

Three hundred years I've ruled this valley. Burned villages. Cursed kings. Turned an entire army into newts. Or accountants. One of those.

So take it. Take the crystal, take the crown. Just leave the ducks. They're the only ones who ever came back."""

# The monologue above is the entry: a specific villain (three centuries
# of rule, burned villages, cursed kings, an army turned to newts) whose
# tiredness lives in the pauses and deflections, never in a plain claim.
# The last line is the sting: the ducks stayed when no one else did.


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    print("wrote %d bytes to %s" % (len(TEXT.encode("utf-8")), path))


if __name__ == "__main__":
    main()
