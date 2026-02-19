# 🛒 CAPSTONE PROJECT – Pytest Automation Framework

## 📌 Project Overview

This project is an End-to-End (E2E) Test Automation Framework built using:

- Python
- Pytest
- Selenium (assumed)
- Page Object Model (POM)
- JSON-based test data

The framework automates core e-commerce workflows including login, product search, cart management, and logout validation.

---

# 📂 Project Structure

CAPSTONE-PROJECT
│
├── pytest_framework
│ ├── data
│ │ └── testdata.json
│ │
│ ├── pages
│ │ ├── base_page.py
│ │ ├── login_page.py
│ │ ├── home_page.py
│ │ ├── product_page.py
│ │ ├── cart_page.py
│ │ ├── logout_page.py
│ │ └── init.py
│ │
│ ├── reports
│ ├── screenshots
│ │
│ ├── tests
│ │ ├── conftest.py
│ │ ├── test_login.py
│ │ ├── test_search.py
│ │ ├── test_add_to_cart.py
│ │ ├── test_update_cart.py
│ │ ├── test_logout.py
│ │ └── init.py
│ │
│ ├── config.ini
│ ├── requirements.txt
│ └── utils.py




---

# 🧱 Framework Architecture

The project follows the **Page Object Model (POM)** design pattern:

- Page logic is separated from test logic
- Reusable methods are defined in page classes
- Tests focus only on validations and flow

---

# 📁 Folder & File Responsibilities

## 🔹 data/

### `testdata.json`
- Stores test data such as:
  - User credentials
  - Product names
  - Test inputs

---

## 🔹 pages/

Contains Page Object Model classes.

### `base_page.py`
- Common reusable methods:
  - click()
  - send_keys()
  - wait_for_element()
  - get_text()
- Parent class for all page classes.

### `login_page.py`
- Handles login functionality:
  - Enter username
  - Enter password
  - Click login

### `home_page.py`
- Handles homepage operations:
  - Search for product
  - Navigate to product page

### `product_page.py`
- Handles product details page:
  - View product details
  - Add product to cart

### `cart_page.py`
- Handles shopping cart actions:
  - Update product quantity
  - Remove item from cart
  - Validate cart contents

### `logout_page.py`
- Handles logout functionality:
  - Click logout
  - Validate logout success

---

## 🔹 tests/

Contains all test cases.

### `conftest.py`
- Pytest fixtures
- Browser setup and teardown
- Common reusable configurations

---

# ✅ End-to-End Scenarios Covered

## 1️⃣ User Login

**Test File:** `test_login.py`  
**Pages Used:** `login_page.py`

✔ User enters valid credentials  
✔ User logs in successfully  
✔ Login validation is performed  

> Note: Registration page is not implemented separately. Login assumes an existing user.

---

## 2️⃣ Product Search & Product Details

**Test File:** `test_search.py`  
**Pages Used:** `home_page.py`, `product_page.py`

✔ User searches for a product  
✔ User navigates to product details  
✔ Product details are validated  

---

## 3️⃣ Add to Cart

**Test File:** `test_add_to_cart.py`  
**Pages Used:** `product_page.py`, `cart_page.py`

✔ User selects product  
✔ Adds product to cart  
✔ Validates product in cart  

---

## 4️⃣ Update Cart & Remove Item

**Test File:** `test_update_cart.py`  
**Pages Used:** `cart_page.py`

✔ User updates product quantity  
✔ Removes item from cart  
✔ Validates cart update  

---

## 5️⃣ Logout & Session Validation

**Test File:** `test_logout.py`  
**Pages Used:** `logout_page.py`

✔ User logs out  
✔ Session is terminated  
✔ Access to protected pages is restricted after logout  

---

# ⚙️ Configuration Files

### `config.ini`
- Stores environment configurations
- Base URL
- Browser configuration

### `requirements.txt`
- Contains all project dependencies
- Install using:

```bash
pip install -r requirements.txt
