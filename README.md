# Local Chat Messenger

このアプリケーションは、UNIX ソケットを使用してローカルマシン上で簡単なチャットを行うことができるシンプルなメッセージングアプリケーションです。

## 概要

`server.py` はチャットサーバとして機能し、クライアントからの接続をリッスンし、メッセージを受信して処理し、応答を送信します。`client.py` はクライアントアプリケーションで、サーバに接続し、メッセージを送信し、サーバからの応答を受信します。

## 必要なもの

*   Python 3.10.12 (動作確認済み)。 より古いバージョンでも動作する可能性がありますが、完全に保証されるものではありません。 より新しいバージョンについては未検証です。
*   `faker` ライブラリ (クライアント側のダミーデータ生成用)

## インストール

1.  リポジトリをクローンまたはダウンロードします。
2.  `faker` ライブラリをインストールします。
    ```bash
    pip install Faker
    ```

## 使い方

1.  **サーバの起動:**
    ```bash
    python server_pra.py
    ```
    サーバは `/tmp/socket_file` に UNIX ソケットを作成し、接続を待ち受けます。

2.  **クライアントの起動:**
    ```bash
    python client_pra.py
    ```
    クライアントはサーバに接続し、メッセージを送信し、サーバからの応答を表示します。複数のクライアントを同時に起動して、チャットをシミュレートできます。

## コードの説明

### `server.py`

*   `socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)`: UNIX ソケットをストリームモードで作成します。
*   `server_address = '/tmp/socket_file'`: サーバが接続を待ち受ける UNIX ソケットのパスを設定します。
*   `os.unlink(server_address)`: 以前の接続が残っている場合に、サーバアドレスを削除します。
*   `sock.bind(server_address)`: ソケットをアドレスにバインドします。
*   `sock.listen(1)`: ソケットが接続要求を待ち受けるようにします。
*   `sock.accept()`: クライアントからの接続を受け入れます。
*   `connection.recv(64)`: 最大 64 バイトのデータを一度に読み込みます。
*   `connection.sendall(response.encode())`: メッセージをバイナリ形式に戻してから送信します。
*   接続ごとに`closing current connection`を表示し、ソケットを閉じます。

### `client.py`

*   `socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)`: UNIX ソケットをストリームモードで作成します。
*   `server_address = '/tmp/socket_file'`: サーバが接続を待ち受ける UNIX ソケットのパスを設定します。
*   `sock.connect(server_address)`: サーバーに接続を試みます。
*   `Faker()`: `faker` ライブラリを使用して、ダミーデータを生成します。
*   `sock.sendall(message)`: データをバイト形式でサーバに送信します。
*   `sock.settimeout(3)`: サーバからの応答を待つ時間を 3 秒に設定します。
*   `sock.recv(64)`: 最大 64 バイトのデータを受信します。
*   `closing socket`を表示し、ソケットを閉じます。

## ライセンス

[MIT](LICENSE)