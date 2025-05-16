# Luma-Ecommerce

Luma-Ecommerce is a Selenium-based automated testing project developed in Python using the PyTest framework. The goal of this project is to automate the **user registration** process on the Luma eCommerce site using randomly generated user data with the help of the **Faker** library. The project is structured using the **Page Object Model (POM)** for better code maintainability and scalability.

## 🔧 Tech Stack

- Python
- Selenium WebDriver
- PyTest
- Faker
- Page Object Model (POM)

## 📌 Features

- Automates the user **registration** functionality
- Uses **Faker** to generate realistic and random:
  - First names
  - Last names
  - Unique email addresses
  - Strong passwords
- Applies **Page Object Model** for clean and maintainable code
- Easily extendable for additional flows like login, cart, and checkout
- Clean and modular test structure
- PyTest-based test execution

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Luma-Ecommerce.git
cd Luma-Ecommerce
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the tests
```bash
pytest tests/
```

## 🧠 How It Works

This project uses **Faker** to create fake but realistic user data each time the test is run. The generated details include a first name, last name, email, and password. Selenium WebDriver automates the browser actions required to:
  - Navigate to the Luma eCommerce website
  - Open the registration page
  - Fill in the registration form with generated data
  - Submit the form
  - Validate successful registration

## 🛠️ Folder Structure

The project follows a clean folder structure using the Page Object Model (POM):

- `pages/register_page.py`
- `datas/login_data.py`
- `tests/test_luma.py`
- `conftest.py`
- `requirements.txt` — Python dependencies  
- `README.md` — Documentation for the project

## 📬 Contact

If you have any questions, suggestions, or feedback, feel free to contact me.
