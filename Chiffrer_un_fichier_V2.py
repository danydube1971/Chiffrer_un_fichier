"""Voici un script python3 pour Linux Mint qui utilise la bibliothèque PyCryptodome pour chiffrer un fichier avec AES 256 bits et 
demander un mot de passe à l'utilisateur (entre 4 et 32 caractères). 
Vous avez besoin du module python3 cryptodome. Installez-le avec la commande pip3 install pycryptodome"""

from Crypto.Cipher import AES
import hashlib

# Récupérer le nom du fichier à chiffrer
filename = input("Entrez le nom du fichier à chiffrer: ")

# Récupérer le mot de passe
while True:
    password = input("Entrez le mot de passe (4 à 32 caractères): ")
    if 4 <= len(password) <= 32:
        break
    print("Le mot de passe doit contenir entre 4 et 32 caractères.")

# Hasher le mot de passe pour obtenir une clé de chiffrement
key = hashlib.sha256(password.encode('utf-8')).digest()

# Ouvrir le fichier à chiffrer
with open(filename, 'rb') as file_in:
    data = file_in.read()

# Ajouter des octets nuls pour compléter le bloc
block_size = 16
padding_size = block_size - len(data) % block_size
data += b'\0' * padding_size

# Chiffrer les données avec AES-256
cipher = AES.new(key, AES.MODE_CBC)
encrypted_data = cipher.iv + cipher.encrypt(data)

# Enregistrer les données chiffrées dans un nouveau fichier
with open(filename + '.enc', 'wb') as file_out:
    file_out.write(encrypted_data)


