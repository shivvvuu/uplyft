# uplyft
# 🛒 E-commerce Sales Chatbot (Next.js + Django + JWT)

This project is a full-stack **E-commerce Sales Chatbot** application built using **Next.js** for the frontend and **Django (DRF)** for the backend. The goal is to simulate a user-friendly, intelligent chatbot that helps customers find products and assists in the purchase process — all backed by secure JWT-based authentication.

---

## 📌 Case Study: Development of an E-commerce Sales Chatbot

In the modern e-commerce space, responsive and intelligent chatbots play a critical role in improving the customer shopping experience. This project aims to simulate such a chatbot interface connected to a mock e-commerce inventory.

---

## 🎯 Objectives

- Build a chatbot that can understand natural language queries and return relevant product results.
- Implement secure login functionality using JWT authentication.
- Provide a smooth, session-persistent user experience.
- Ensure a modular and scalable backend using Django with a mock inventory.

---

## 🧩 Features

### ✅ Frontend (Next.js)

- Responsive UI: Supports desktop, tablet, and mobile views.
- JWT Authentication: Login/logout with access and refresh token flow.
- Persistent Chat Sessions: Timestamps, message history, and reset button.
- Product Exploration: Users can search for products using natural queries.
- Clean UI/UX: Simple interface for real-time bot interaction.

### ✅ Backend (Django + DRF)

- JWT Auth (via `djangorestframework-simplejwt`).
- REST API endpoints:
  - `/api/login/` – authenticate users.
  - `/api/token/refresh/` – refresh JWT access tokens.
  - `/api/chat/` – accept user input and return chatbot responses.
- NLP Layer: Basic sentence parsing to match products.
- Mock Inventory: 100+ fake products in categories like books, electronics, or clothing.
- CSRF handling for cookie-based interactions.

---

## 🛠️ Tech Stack

| Layer       | Technology          |
|-------------|---------------------|
| Frontend    | Next.js, Tailwind CSS |
| Backend     | Django, DRF         |
| Auth        | JWT (SimpleJWT)     |
| DB          | SQLite (mock RDBMS) |
| Dev Tools   | Postman, VS Code    |

---

## 🗂️ Project Structure


---

## 🔐 JWT Authentication Flow

- On login, access and refresh tokens are generated.
- The frontend stores the access token in memory and the refresh token in `HttpOnly` cookies (or localStorage for simulation).
- Token refresh is handled automatically before expiration.

---

## 💬 Chatbot Logic

- Parses user queries via a simple sentence parser.
- Matches keywords with product attributes (name, category, description).
- Returns relevant product list with links.
- Example: User types “show me wireless headphones” → returns relevant products.

---

## 📊 Database

- Populated with 100+ mock entries using Faker and custom seed scripts.
- Each product includes: `name`, `category`, `price`, `description`, and `image`.

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ecommerce-chatbot.git
cd ecommerce-chatbot

cd backend
python -m venv venv
source venv/bin/activate
poerty install
make migrate
python manage.py seed_products  # Custom command to add mock data
make runserver
