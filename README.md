# 🚀 Space Cargo Management System

A full-stack web application that manages cargo on a space station — allowing users to add, search, retrieve, dispose, and return items efficiently. Built using **FastAPI** for the backend and **React + Tailwind CSS** for the frontend, it offers a clean UI and powerful API for seamless space logistics.

---

## 🌐 Live Preview

> 🔹 Frontend: http://localhost:3000  
> 🔹 API Docs: http://localhost:8000/docs  
> 🔹 ReDoc: http://localhost:8000/redoc

---

## 🛠 Tech Stack

- **Frontend:** React.js, Tailwind CSS, Axios  
- **Backend:** FastAPI, SQLite, SQLAlchemy, Pydantic  
- **Tools:** Node.js, Python 3, Uvicorn

---

## 📁 Project Structure

```
space_cargo_management/
├── backend/
│   ├── main.py            # FastAPI routes and server logic
│   ├── models.py          # SQLAlchemy DB models
│   ├── schemas.py         # Pydantic schemas
│   ├── database.py        # DB connection
│   └── utils.py           # Helper functions
├── frontend/
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── index.js
│       └── components/
│           ├── CargoForm.jsx
│           ├── CargoList.jsx
│           ├── RetrieveCargo.jsx
│           ├── WasteManager.jsx
│           └── ReturnPlan.jsx
└── README.md
```

---

## ⚙️ Backend Setup (FastAPI + SQLite)

### 1. Navigate to backend

```bash
cd backend
```

### 2. Create virtual environment (optional)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

### 4. Start the backend server

```bash
uvicorn main:app --reload
```

### 5. Access API Docs

- Swagger UI: http://localhost:8000/docs  
- ReDoc: http://localhost:8000/redoc

---

## 🎨 Frontend Setup (React + Tailwind CSS)

### 1. Navigate to frontend

```bash
cd frontend
```

### 2. Install dependencies

```bash
npm install
```

### 3. Start frontend server

```bash
npm start
```

App will be live at: [http://localhost:3000](http://localhost:3000)

---

## 🔗 Connecting Frontend with Backend

- Ensure backend is running on `localhost:8000`.
- Axios is configured in frontend to make requests to this API.
- FastAPI includes CORS middleware — no CORS issues!

---

## 🚀 API Endpoints

| Method | Endpoint                 | Description                   |
|--------|--------------------------|-------------------------------|
| GET    | `/cargo/`                | Get list of all cargo         |
| POST   | `/cargo/`                | Add a new cargo               |
| GET    | `/cargo/{id}`            | Get specific cargo by ID      |
| GET    | `/search/?query=...`     | Search cargo by name          |
| PUT    | `/cargo/{id}/dispose`    | Mark cargo as disposed        |
| POST   | `/return_plan/`          | Generate a return plan        |

---

## 📦 Sample Workflow

1. Add new cargo using the form in the frontend.
2. View all cargo in the Cargo List.
3. Retrieve a cargo item using ID.
4. Dispose of unwanted items.
5. Generate optimized return plans for leftover cargo.

---

## 🧠 Author

**Sukanya Ghosh**  
[GitHub](https://github.com/sukanyaghosh74)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

