# 生産性向上試作プロジェクト

## 概要

プロジェクトの生産性を向上するために開発周りのあらゆることを自動化してみる。

## 依存関係

| Name         | Version | Description                                          |
| ------------ | ------- | ---------------------------------------------------- |
| Python       | 3.11    | 開発言語                                             |
| Poetry       | 1.5.1   | パッケージマネージャー                               |
| Poe the Poet | 0.21.1  | タスクランナー [Link](https://poethepoet.natn.io/)   |
| act          | 0.2.49  | GAローカル実行 [Link](https://github.com/nektos/act) |

## レポジトリ運用方法

品質向上のためにコード保存時等のタイミングで自動実行処理を設定済み。
実行タイミングと内容は下記の通り。

自動実行タイミングと内容
1. 保存時 (VSCode, pre-commit)
    フォーマッター(black, isort)を自動実行
2. git push時 (pre-commit)
    リンター(flake8, mypy)を自動実行
3. pull request作成時、更新時 (GitHub Actions)
    自動テスト(pytest)を自動実行
4. タグpush時 (GitHub Actions)
    自動的にDocker imageをビルドし、Docker Hubにプッシュ

## GitHub Actionsローカル実行方法

GitHub Actions自体のテストをしたいときはローカル実行環境である`act`を利用する。

準備
1. [act](https://github.com/nektos/act)をインストール
2. .secrets.exampleから`.secrets`をコピーし、認証情報を記入

実行
```bash
act --secret-file .secrets <イベント>
```

| イベント     | 実行内容                         |
| ------------ | -------------------------------- |
| pull_request | 自動テストを実施                 |
| push         | Dockerイメージのビルドとプッシュ |

## ToDo

- [x] 自動テストの導入
- [x] pre-commitの導入
    コミット前にformatterの実行, プッシュ前にlinterの実行
- [x] サービス稼働用コンテナイメージの作成
- [x] Github actionの導入
    - [x] CIパイプラインを構築し、mainへのpull request作成時にテストを実行
    - [x] タグプッシュ時にサービス稼働用コンテナイメージ作成
- [ ] 構造化ログの導入
- [ ] OpenAPIを利用した仕様書の自動生成
