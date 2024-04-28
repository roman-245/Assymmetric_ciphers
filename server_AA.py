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

    # Принимаем и расшифровываем сообщение
    encrypted_message = pickle.loads(conn.recv(1024))
    message = ''.join([chr(pow(char, K, p)) for char in encrypted_message])
    print("Получено сообщение:", message)

    # Шифруем и отправляем ответ
    response = "Привет, клиент!"
    encrypted_response = [pow(ord(char), K, p) for char in response]
    conn.send(pickle.dumps(encrypted_response))
