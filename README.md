


# 🎬 MoviePy Reels Generator  

Bu loyiha **Python + MoviePy** yordamida Instagram/TikTok **Reels** yoki boshqa qisqa videolarni avtomatik generatsiya qilish uchun yaratilgan.  

## 📂 Loyihaning tuzilishi  

```bash
moviepy-test/
│── main.py              # Dastur boshlanish nuqtasi
│── video_builder.py     # Video yig‘ish jarayoni
│── text_utils.py        # Matnni rasmga chizish yordamchisi
│── assets/              # Resurslar (fon rasmi, shriftlar va boshqalar)
│   ├── background.jpg   # Fonda ishlatiladigan rasm
│   └── fonts/           # Shriftlar papkasi
│── venv/                # Virtual muhit (Python kutubxonalar)
│── output/              # Tayyor videolar shu yerga saqlanadi
````

---

## ⚙️ O‘rnatish

1. Loyihani yuklab oling yoki klon qiling:

```bash
git clone https://github.com/username/moviepy-reels.git
cd moviepy-reels
```

2. Virtual muhit yarating:

```bash
python -m venv venv
```

3. Virtual muhitni yoqing:

* Windows:

  ```bash
  venv\Scripts\activate
  ```
* Linux/Mac:

  ```bash
  source venv/bin/activate
  ```

4. Kerakli kutubxonalarni o‘rnating:

```bash
pip install moviepy pillow
```

---

## ▶️ Ishga tushirish

```bash
python main.py
```

✅ Natijada tayyor video `output/reels_output.mp4` fayliga saqlanadi.

---

## 📝 Kodning qisqacha izohi

* **main.py**

  * `build_video()` funksiyasini chaqiradi va videoni yaratadi.

* **video\_builder.py**

  * `background.jpg` fonini yuklaydi
  * Matnlarni (`headline`, `subheadline`) rasm sifatida chizib videoga qo‘shadi
  * `CompositeVideoClip` orqali ularni birlashtiradi
  * Tayyor videoni `.mp4` faylga yozadi

* **text\_utils.py**

  * `draw_text_image()` funksiyasi yordamida matndan rasm yaratadi
  * Matnni shrift bilan markazga joylashtiradi

---

## 🖼 Misol chiqish

👉 `background.jpg` fon ustiga matn qo‘yilib, `output/reels_output.mp4` ko‘rinishida saqlanadi.

---

## 🔮 Kelajakda qo‘shish mumkin

* ✅ Music qo‘shish (`.mp3` fayldan)
* ✅ Animatsiyalar (`fadein`, `slide`, `zoom` effektlar)
* ✅ Ko‘p sahifali reels generatori (1 ta fon + turli matnlar)
* ✅ Logo / watermark qo‘shish

---

## 📌 Talablar

* Python 3.8+
* [MoviePy](https://github.com/Zulko/moviepy)
* [Pillow](https://pypi.org/project/Pillow/)

---

## 👨‍💻 Muallif

Loyiha foydalanuvchi tomonidan **o‘rganish va amaliyot** uchun yaratilgan.
