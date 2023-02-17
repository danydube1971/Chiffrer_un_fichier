# Chiffrer_un_fichier
Chiffrer et déchiffrer n'importe quel fichier (AES 256 bits) avec un mot de passe ciblé

Chiffrer un fichier :
Ce script chiffre un fichier en utilisant l'algorithme de chiffrement AES (Advanced Encryption Standard) avec une clé dérivée d'un mot de passe.

Voici les étapes effectuées par le script:

1. Importation des modules Crypto.Cipher et hashlib.
2. Demande à l'utilisateur d'entrer le nom du fichier à chiffrer et le mot de passe.
3. Utilisation du module hashlib pour hasher le mot de passe en utilisant l'algorithme de hachage SHA-256, afin d'obtenir une clé de chiffrement.
4. Ouverture du fichier à chiffrer en mode lecture binaire ('rb'), lecture des données dans le fichier et stockage des données dans la variable "data".
5. Ajout d'octets nuls à la fin des données pour compléter le dernier bloc de 16 octets (la taille de bloc de chiffrement AES utilisée dans ce script).
6. Création d'un nouvel objet de chiffrement AES-256 avec la clé dérivée du mot de passe et un vecteur d'initialisation (IV) généré aléatoirement.
7. Chiffrement des données en utilisant le mode CBC (Cipher Block Chaining) d'AES et stockage des données chiffrées dans la variable "encrypted_data".
8. Écriture des données chiffrées dans un nouveau fichier avec l'extension ".enc" ajoutée au nom du fichier d'origine. Le nouveau fichier est ouvert en mode écriture binaire ('wb') et les données chiffrées sont écrites dans le fichier.
