#dictionary.py
data_mahasiswa = {
    "nama": "Muh ammar s",
    "nim": "D0425511",
    "jurusan": "sistem informasi",
    "ipk": 3.75
}

print("Data Mahasiswa Awal:")
print(data_mahasiswa)

# =========================================
# Mengakses nilai dictionary
# =========================================
print("\nNama Mahasiswa:", data_mahasiswa["nama"])
print("NIM:", data_mahasiswa.get("nim"))

# =========================================
# Menambah data baru ke dictionary
# =========================================
data_mahasiswa["angkatan"] = 2025
print("\nSetelah Menambah Angkatan:")
print(data_mahasiswa)

# =========================================
# Mengubah nilai dictionary
# =========================================
data_mahasiswa["ipk"] = 3.90
print("\nSetelah Update IPK:")
print(data_mahasiswa)

# =========================================
# Menghapus elemen dictionary
# =========================================
deleted = data_mahasiswa.pop("jurusan")
print(f"\nMenghapus 'jurusan' ({deleted})")
print(data_mahasiswa)

# =========================================
# Iterasi dictionary
# =========================================
print("\n--- Iterasi Dictionary ---")
for key, value in data_mahasiswa.items():
    print(f"{key} : {value}")
