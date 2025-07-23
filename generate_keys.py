import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["ALPISUR", "UTPL"]
usernames = ["alpisur", "utpl"]
passwords = ["usuarioalpisur2025", "usuarioutpl2025"]

# Generar los hashes de las contraseñas
hashed_passwords = stauth.Hasher.hash_list(passwords)

# Guardar los hashes en un archivo
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

# Mostrar los hashes generados
for password, hash in zip(passwords, hashed_passwords):
    print(f"Contraseña: {password} -> Hash: {hash}")