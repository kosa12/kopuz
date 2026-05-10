import os
import re

locales_dir = "locales"
en_file = os.path.join(locales_dir, "en.ftl")

def get_keys(path):
    keys = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            m = re.match(r'^([A-Za-z0-9_-]+)\s*=', line)
            if m:
                keys.add(m.group(1))
    return keys

en_keys = get_keys(en_file)
failures = False

for fname in os.listdir(locales_dir):
    if not fname.endswith(".ftl") or fname == "en.ftl": continue
    path = os.path.join(locales_dir, fname)
    loc_keys = get_keys(path)
    missing = en_keys - loc_keys
    if missing:
        print(f"File {fname} missing: {', '.join(missing)}")
        failures = True

if not failures:
    print("All files match en.ftl!")
