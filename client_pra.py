import socket
import sys
from faker import Faker

# TCP/IPソケットを作成。
# UNIXソケットをストリームモードで作成。
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# このサーバが接続を待つUNIXソケットのパスを設定
server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

# サーバーに接続を試みる。
try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

fake = Faker()

# サーバに接続後、サーバにメッセージを送信。
try:
    # データをバイト形式で送る。
    message = b'sending a message to the server side from ' + fake.name().encode()
    sock.sendall(message)

    # サーバからの応答を待つ時間を3秒間に設定。
    sock.settimeout(3)

    try:
        while True:
            # 受け取るデータの最大量は64バイトとする。
            data = str(sock.recv(64))

            if data:
                print('server response: ' + data)
            else:
                break
    except(TimeoutError):
        print('socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()