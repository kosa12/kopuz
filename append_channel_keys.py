import os

locales_dir = "locales"
en_file = os.path.join(locales_dir, "en.ftl")

snippet = """
channel_mode = Channel Mode
channel_mode_stereo = Stereo
channel_mode_mono = Mono
channel_mode_left_only = Left only
channel_mode_right_only = Right only
channel_mode_swap_left_right = Swap L/R
"""

for fname in os.listdir(locales_dir):
    if not fname.endswith(".ftl") or fname == "en.ftl": continue
    path = os.path.join(locales_dir, fname)
    with open(path, "a", encoding="utf-8") as f:
        f.write("\n" + snippet.strip() + "\n")
    print(f"Updated {fname}")

