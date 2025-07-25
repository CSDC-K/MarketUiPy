
<div align="center">
  <img src="https://img.icons8.com/emoji/96/shopping-cart-emoji.png" width="80"/>
  <h1>MarketUiPy 🛒</h1>
  <p><strong>💻 GUI-based Python Market Management System</strong></p>
  <sub>Built with CustomTkinter</sub>
</div>

---

## 📸 Preview

> Add a screenshot of your UI here for better visibility

![Preview](Assets/img/preview.png)

---

## 🚀 Features

- 🔐 **Login screen** with username/password
- 🧍‍♂️ User account creation, editing, and deletion
- 🎓 **Permission levels** (`C`, `B`, `A`, `A+`, `S`, etc.)
- 🛍️ **Shopping panel** to add/remove items via ItemID
- 🧾 **Bill generation** with total prices
- 🗃️ JSON-based **local data storage**
- 🎨 Modern GUI with icons and color-coded permissions
- ⚙️ Cross-platform support (`Windows` & `Linux`)

---

## 📁 File Structure

```bash
MarketUiPy/
├── main.py                  # Main application file
├── Assets/
│   ├── img/                 # Icons for UI (home, user, search, etc.)
│   └── data/
│       ├── UserManagement.json
│       ├── Item.json
│       ├── Payment.json
│       └── FastItem.json
└── README.md
```

---

## 🛠️ Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install customtkinter pillow CTkListbox
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🔐 Permission Levels

| Code  | Description                             | Access Level       |
|-------|-----------------------------------------|--------------------|
| C     | Only sales access                       | 🔓 Basic            |
| B     | Sales + stock management                | 📦 Intermediate     |
| A     | Finance access                          | 💰 Finance          |
| A+    | Advanced finance access                 | 📈 Advanced         |
| A++   | Finance + auditing                      | 🕵️‍♂️ Expert         |
| S     | Full admin access                       | 🔐 Admin            |
| S+    | Create/edit/delete users                | 👑 Super Admin      |

---

## 📌 TODO

- [ ] Connect to SQLite or PostgreSQL
- [ ] Export receipts as PDF
- [ ] Add charts for sales visualization 📊
- [ ] Dark mode theme 🌙

---

## 🧑‍💻 Developer

Made with ❤️ by [CSDC-K](https://github.com/CSDC-K)

---

## 📄 License

MIT License – free to use, modify, and distribute.
