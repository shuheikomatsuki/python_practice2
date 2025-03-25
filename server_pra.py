import socket
import os

# UNIXソケットをストリームモードで作成。
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# このサーバが接続を待つUNIXソケットのパスを設定
server_address = '/tmp/socket_file'

# 以前の接続が残っているなら、サーバアドレスを削除する。
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('starting up on {}'.format(server_address))

sock.bind(server_address)

# ソケットが接続要求を待機するようにする。
sock.listen(1)

while True:
    # クライアントからの接続を受け入れる。
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            # 最大で64バイトのデータを一度に読み込む。
            data = connection.recv(64)
            data_str = data.decode('utf-8')
            print('Received ' + data_str)
        
            if data:
                response = 'processing ' + data_str
                # メッセージをバイナリ形式に戻してから送信。
                connection.sendall(response.encode())
            else:
                print('no data from', client_address)
                break
    finally:
        print("closing current connection")
        connection.close()