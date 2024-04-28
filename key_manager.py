from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.backends import default_backend
import rsa

def generate_and_save_keys():
    # Генерация ключей и сохранение на диск
    public_key, private_key = rsa.newkeys(1024)

    # Сохранение приватного ключа
    with open("private_key.pem", "wb") as f:
        f.write(private_key.save_pkcs1())

    # Сохранение публичного ключа
    with open("public_key.pem", "wb") as f:
        f.write(public_key.save_pkcs1())

def load_keys():
    # Загрузка ключей из файлов
    with open("private_key.pem", "rb") as f:
        private_key_data = f.read()
        private_key = serialization.load_pem_private_key(private_key_data, password=None, backend=default_backend())

    with open("public_key.pem", "rb") as f:
        public_key_data = f.read()
        public_key = serialization.load_pem_public_key(public_key_data, backend=default_backend())

    return public_key, private_key

def serialize_public_key(public_key):
    return public_key.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

def deserialize_public_key(public_key_bytes):
    return serialization.load_pem_public_key(public_key_bytes, backend=default_backend())
