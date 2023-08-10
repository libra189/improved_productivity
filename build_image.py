import subprocess

import toml

IMG_NAME: str = "improved_productivity"

# イメージのバージョンをpyprojectから読み込み
with open("./pyproject.toml", "r") as f:
    obj = toml.load(f)

img_version: str = obj["tool"]["poetry"]["version"]
tag = f"{IMG_NAME}:{img_version}"

# イメージのビルド
print("Build start.")

cmd = ["docker", "build", "-t", tag, "."]
subprocess.run(cmd)

print("Build finished.")
