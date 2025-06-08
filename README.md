
# 🔐 Amaliyot2025 – RC4 va A5/1 shifrlash algoritmlari

🎓 **Amaliy maqsad:**  
Ushbu loyiha Oqimli  shefirlash algortimlari (RC4 va A5/1) algoritmlaridan foydalanib matnni shifrlash va deshifrlash jarayonini tushunish, ularni amalda sinab ko‘rish uchun mo‘ljallangan. 

---

## 📌 Loyihaning imkoniyatlari

✅ Matnni RC4 yoki A5/1 algoritmi orqali shifrlash  
✅ Shifrlangan matnni deshifrlash (asl holatga qaytarish)  
✅ Har bir natijani `.xlsx` faylga avtomatik saqlash  

---

## 📦 O‘rnatilishi lozim bo‘lgan kutubxonalar

Quyidagi buyruq orqali barcha kerakli kutubxonalarni o‘rnating:

```bash
    uv add pandas openpyxl
```

Yoki `pyproject.toml` fayli asosida:

---

## ⚙️ Foydalanish

```bash
    python main.py
```

So‘ng sizdan algoritm tanlash so‘raladi:

```text
Algoritmni turini tanlang 
    1. RC4
    2. A5/1
```

Tanlovga qarab siz matn va kalit kiritasiz. Dastur natijani quyidagi fayllarga saqlaydi:

- 📄 `rc4_natija.xlsx` – RC4 algoritmi natijalari
- 📄 `a5_1_natija.xlsx` – A5/1 algoritmi natijalari

---

## 📁 Fayl va kodlar tuzilmasi

### 📂 `main.py`

Asosiy dastur:  
- Foydalanuvchidan algoritm tanlashni va matn-kalit kiritishni so‘raydi  
- Tanlangan algoritmni ishga tushiradi  
- Natijani `.xlsx` faylga yozadi

### 📂 `algorithms.py`

#### 📌 `rc4(key: bytes, data: bytes) -> bytes`

RC4 oqimli shifrlash algoritmi. XOR asosida ishlaydi. Kalitga asoslangan `keystream` hosil qiladi va matnni shifrlaydi.

#### 📌 `LFSR` klassi va `a5_1_encrypt`

A5/1 shifrlash algoritmi uchun 3 ta LFSR registrlardan foydalanadi.  
- Har bir registr o‘z uzunligi va `tap` joylashuvi bilan yaratiladi  
- Majority (ko‘pchilik) asosida qaysi registrlar harakatlanishini aniqlaydi  
- Har bir bit `keystream` orqali XOR qilinadi

#### 📌 `bytes_to_bits` / `bits_to_bytes`

Baytlarni bitlar ro‘yxatiga va aksincha o‘zgartirish uchun yordamchi funksiyalar.

#### 📌 `append_to_excel(filename, new_row)`

Excel faylga yangi qator qo‘shadi. Agar fayl mavjud bo‘lsa – mavjud ustunlarga yangi ma’lumot qo‘shadi. Yangi fayl ochmaydi.

---

## 🔎 RC4 algoritmi qanday ishlaydi?

📌 RC4 – bu oqimli shifrlash algoritmi bo‘lib, quyidagicha ishlaydi:
1. Kalit asosida `S` nomli massiv hosil qilinadi (`key scheduling algorithm`)
2. `S` massiv aralashtiriladi
3. Shifrlash paytida har bir belgi uchun `keystream` elementi olinadi
4. Har bir bayt `keystream` bilan XOR qilinadi

➡️ Shifrlash va deshifrlash algoritmi bir xil.

---

## 🔎 A5/1 algoritmi qanday ishlaydi?

📌 A5/1 – GSM mobil tarmoqlarida ishlatiladigan oqimli algoritm:
1. 64 bitli kalit 3 ta registrga (`R1`, `R2`, `R3`) yuklanadi
2. Har bir registrning harakatlanishi majority qoidasiga bog‘liq
3. Har bir bit uchun `R1 ⊕ R2 ⊕ R3` bit chiqariladi
4. Olingan `keystream` bitlar matn bilan XOR qilinadi

➡️ Deshifrlash ham xuddi shunday amalga oshiriladi.

---

## 📊 Natijalar qayerga yoziladi?

📁 `rc4_natija.xlsx` – RC4 shifrlangan/deshifrlangan matnlar  
📁 `a5_1_natija.xlsx` – A5/1 shifrlangan/deshifrlangan matnlar

Har bir yangi ishga tushurishda avvalgi faylga yangi qator **qo‘shiladi**, o‘chirilmaydi.

---

## ✍️ Mualliflar

👨‍💻 Ahmedov Tohirbek  
👨‍💻 Azizov Diyorbek  
👨‍💻 Qudratov Asadbek

Ushbu loyiha amaliyot va shifrlash algoritmlari bilan tanishish uchun tayyorlangan

🛠 Yordam yoki takliflar uchun bemalol bog‘laning!