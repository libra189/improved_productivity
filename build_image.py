import subprocess

import toml


def main():
    """ローカル環境でコンテナイメージをビルドし、dockerhubへプッシュ"""

    # イメージのバージョンをpyprojectから読み込み
    with open("./pyproject.toml", "r") as f:
        obj = toml.load(f)

    img_name = obj["tool"]["poetry"]["name"]
    img_version = obj["tool"]["poetry"]["version"]
    tag = f"libra189/{img_name}:{img_version}"

    # イメージのビルド
    print("Image build.")
    cmd = ["docker", "build", "-t", tag, "."]
    subprocess.run(cmd)

    print("Push image to dockerhub.")
    cmd = ["docker", "push", tag]
    subprocess.run(cmd)


if __name__ == "__main__":
    main()
