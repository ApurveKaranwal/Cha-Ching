# Cha-Ching 💸 – Expense Tracker

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi)
![JavaScript](https://img.shields.io/badge/Frontend-JavaScript-F7DF1E?logo=javascript&logoColor=black)
![HTML](https://img.shields.io/badge/HTML-5-orange?logo=html5)
![CSS](https://img.shields.io/badge/CSS-3-blue?logo=css3)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python)
![Database](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)
![Made With Love](https://img.shields.io/badge/Made%20With❤️-ChaChing-blue)





Cha-Ching is a simple and efficient **full-stack expense tracking application** that helps users record, manage, and analyze their daily expenses.  
It comes with a clean UI built using **HTML, CSS, JavaScript** and a powerful backend using **FastAPI**.

---

## 🚀 Features
- Add, view, update, and delete expenses  
- Categorize expenses  
- Display total expenses  
- Fast and lightweight backend  
- CORS-enabled API  
- Clean and responsive UI  
- A notes feature for entries like *“money given to a friend”*

---

## 🛠️ Tech Stack

### **Frontend**
- HTML  
- CSS  
- JavaScript  

### **Backend**
- FastAPI  
- Python  
- SQLAlchemy  
- SQLite (or any other DB)

---

## 📁 Project Structure
```Cha-Ching/
│── backend/
│ ├── main.py
│ ├── database.py
│ └── models.py
│── frontend/
│ ├── index.html
└── README.md
```

---

## ⚙️ Setup Instructions

### **1. Clone the repository**
```bash
git clone https://github.com/ApurveKaranwal/Cha-Ching.git
cd Cha-Ching
```
### **2. Backend Setup**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate # For Linux
pip install -r requirements.txt
uvicorn main:app --reload
```

Backend runs at:  
`http://127.0.0.1:8000`

### **3. Run Frontend**
Open the `index.html` file in the frontend folder using **Live Server**.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/expenses` | Get all expenses |
| POST | `/expenses` | Add a new expense |
| PUT | `/expenses/{id}` | Update an expense |
| DELETE | `/expenses/{id}` | Delete an expense |
| POST | `/notes` | Add special notes |

---

## 📝 Notes Feature
Use this to store information such as:
- *Gave ₹500 to a friend*
- *Pending amount from someone*

Notes are stored and displayed separately.

---

## 🤝 Contributing
Feel free to open issues or pull requests.

---

## 📄 License
This project is licensed under the **MIT License**.

