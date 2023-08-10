# 生産性向上試作プロジェクト

## 概要

プロジェクトの生産性を向上するために開発周りのあらゆることを自動化してみる

## 依存関係

言語 Python 3.11
パッケージマネージャー Portry 1.5.1
タスクランナー [Poe the Poet 0.21.1](https://poethepoet.natn.io/)
Github Actions ローカル実行 [act](https://github.com/nektos/act)

## 自動実行

### pre-commit

- black
- isort

### pre-push

- flake8
- mypy

### create marge request

- pytest

### approval marge request

- build docker image

## ToDo

- [x] 自動テストの導入
- [x] pre-commitの導入
    コミット前にformatterの実行, プッシュ前にlinterの実行
- [x] サービス稼働用コンテナイメージの作成
- [ ] Github actionの導入
    - [x] CIパイプラインを構築し、mainへのpull request作成時にテストを実行
    - [ ] pull request承認時にサービス稼働用コンテナイメージ作成
- [ ] 構造化ログの導入
- [ ] OpenAPIを利用した仕様書の自動生成
