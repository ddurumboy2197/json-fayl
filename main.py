import os

def chiqar_fayl_nomi(katalog):
    for fayl in os.listdir(katalog):
        if fayl.endswith('.txt'):
            print(fayl)

chiqar_fayl_nomi('.')
```

Kodni ishlatish uchun, siz katalogni o'zgartiring. Misol uchun, agar siz hozirgi katalogda `.txt` fayllar nomlarini chiqarishni istaysiz, `.` ni katalog deb qabul qilish uchun katalog parametrini `.` ga teng qo'yishingiz kerak.
