import socket
import pickle
import random

HOST = '127.0.0.1'
PORT = 8080

# Параметры Диффи-Хеллмана
p = 23  # большое простое число
g = 5   # примитивный корень по модулю p

# Генерируем секретный ключ клиента
a = random.randint(1, p-1)
A = pow(g, a, p)

# Подключаемся к серверу и отправляем параметры
with socket.socket() as sock:
    sock.connect((HOST, PORT))
    sock.send(pickle.dumps((p, g, A)))

    # Принимаем параметры сервера
    msg = sock.recv(1024)
    p, g, B = pickle.loads(msg)

    # Вычисляем общий секрет
    K = pow(B, a, p)
    print("Общий секрет:", K)

    # Отправляем и шифруем сообщение
    message = "Привет, сервер!"
    encrypted_message = [pow(ord(char), K, p) for char in message]
    sock.send(pickle.dumps(encrypted_message))

    # Принимаем и расшифровываем ответ
    encrypted_response = pickle.loads(sock.recv(1024))
    response = ''.join([chr(pow(char, K, p)) for char in encrypted_response])
    print("Ответ от сервера:", response)

