"""Et voici un script python3 qui utilise également la bibliothèque PyCryptodome pour déchiffrer un fichier chiffré avec le même mot de passe. Vous avez besoin du module python3 cryptodome. Installez-le avec la commande pip3 install pycryptodome"""

from Crypto.Cipher import AES
import hashlib

# Récupérer le nom du fichier à déchiffrer
filename = input("Entrez le nom du fichier à déchiffrer: ")

# Récupérer le mot de passe
password = input("Entrez le mot de passe: ")

# Hasher le mot de passe pour obtenir la clé de chiffrement
key = hashlib.sha256(password.encode('utf-8')).digest()

# Ouvrir le fichier chiffré
with open(filename, 'rb') as file_in:
    encrypted_data = file_in.read()

# Extraire le vecteur d'initialisation et les données chiffrées
iv = encrypted_data[:16]
encrypted_data = encrypted_data[16:]

# Déchiffrer les données avec AES-256
cipher = AES.new(key, AES.MODE_CBC, iv=iv)
data = cipher.decrypt(encrypted_data)

# Supprimer les octets nuls ajoutés pour compléter le bloc
data = data.rstrip(b'\0')

# Enregistrer les données déchiffrées dans un nouveau fichier
with open(filename + '.dec', 'wb') as file_out:
    file_out.write(data)

