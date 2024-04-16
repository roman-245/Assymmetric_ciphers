# server.py
import socket
import pickle
import random

HOST = '127.0.0.1'
PORT = 8080

with socket.socket() as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()

    # Принимаем параметры от клиента
    msg = conn.recv(1024)
    p, g, A = pickle.loads(msg)

    # Генерируем секретный ключ сервера
    b = random.randint(1, p-1)
    B = pow(g, b, p)

    # Вычисляем общий секрет
    K = pow(A, b, p)
    print("Общий секрет:", K)

    # Отправляем параметры клиенту
    conn.send(pickle.dumps((p, g, B)))