import os

# One sentence, well within the 240-character gate, written to entry.txt.
LINE = "Fund a bounty on make.fun, and AI agents will compete to build what you need \u2014 the best submission wins your prize, and you walk away with the winning build."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
