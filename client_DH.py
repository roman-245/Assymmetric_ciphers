# client.py
import socket
import pickle
import random

HOST = '127.0.0.1'
PORT = 8080

# Параметры Диффи-Хеллмана
p = 7
g = 5

# Генерируем секретный ключ клиента
a = random.randint(1, p-1)
A = pow(g, a, p)

# Отправляем параметры на сервер
with socket.socket() as sock:
    sock.connect((HOST, PORT))
    sock.send(pickle.dumps((p, g, A)))

    # Принимаем параметры сервера
    msg = sock.recv(1024)
    p, g, B = pickle.loads(msg)

    # Вычисляем общий секрет
    K = pow(B, a, p)
    print("Общий секрет:", K)