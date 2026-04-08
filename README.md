# 🌾 Agro Fresh – Farmer Driven Marketplace

Agro Fresh is a **Django-based web application** that connects farmers directly with customers, enabling the sale of fresh agricultural products without middlemen. The platform ensures fair pricing for farmers and fresh produce for consumers.

---

## 🚀 Features

### 👨‍🌾 Farmer Panel

* Add, update, and delete products
* Manage pricing and stock
* View customer orders

### 🛒 Customer Panel

* Browse products by category
* Add to cart and place orders
* View order history
* Rate and review products

### 🔐 Authentication System

* Separate login/signup for farmers and customers
* Secure user authentication

### 📦 Order Management

* Track order status (Pending, Shipped, Delivered)
* Order history for users

---

## 🛠️ Tech Stack

* **Backend:** Django, Python
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** SQLite (default)
* **Other:** Django Admin Panel

---

## 📂 Project Structure

```
agrofresh/
│
├── users/        # Authentication & user roles
├── products/     # Product management
├── orders/       # Order handling
├── reviews/      # Ratings & feedback
├── core/         # Homepage & main views
├── templates/    # HTML templates
├── static/       # CSS, JS, Images
└── db.sqlite3
```

---

## ⚙️ Installation & Setup

1. Clone the repository

```
git clone https://github.com/your-username/agrofresh.git
cd agrofresh
```

2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Apply migrations

```
python manage.py migrate
```

5. Run the server

```
python manage.py runserver
```

6. Open in browser

```
http://127.0.0.1:8000/
```

---

## 🔑 Admin Access

Create superuser:

```
python manage.py createsuperuser
```

Then login at:

```
http://127.0.0.1:8000/admin/

## 🌟 Future Enhancements

* 💳 Online Payment Integration (Razorpay/Stripe)
* 📍 Location-based farmer search
* 📱 Mobile responsiveness improvement
* 🤖 AI-based price prediction
* 🚚 Live delivery tracking

## 🎯 Purpose

The goal of Agro Fresh is to:

* Empower farmers 💪
* Eliminate middlemen 🚫
* Provide fresh and affordable products 🥦

