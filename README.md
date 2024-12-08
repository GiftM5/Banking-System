# Banking System (Web-based)

A simple banking system built with Flask and SQLite. This system allows users to register, log in, view their balance, deposit, withdraw, update their account, and delete their account. The project uses Flask as the backend web framework and SQLite for database storage.

## Features

- **User Registration**: Create a new user account.
- **User Login**: Log in with an existing account.
- **Balance View**: View the balance of the account after login.
- **Deposit Funds**: Deposit money into your account.
- **Withdraw Funds**: Withdraw money from your account.
- **Update Account**: Modify your account details.
- **Delete Account**: Delete your account from the system.

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Setup and Installation

### 1. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/banking-system.git
cd banking-system

Application Structure
app.py: The main file containing Flask routes, app initialization, and logic.
templates/: This folder contains the HTML templates for the various pages (homepage, login, register, etc.).
static/: This folder holds static files such as CSS and images.
models.py (if separated): Contains the database models (e.g., User model).

Usage
Once the server is running, you can access the following features:

1. Home Page
Access the home page at http://127.0.0.1:5000/. Here, users can navigate to the login and registration pages.

2. Registration
To create a new account, navigate to the Register page and provide a username and password. If the username already exists, an error will be displayed.

3. Login
Once registered, users can log in using their credentials. After successful login, they will be redirected to the homepage and can access their balance.

4. Deposit
On the homepage, users can deposit money into their account by entering an amount. The balance will be updated after the deposit.

5. Withdraw
Users can withdraw money from their account. The withdrawal amount will be deducted from their balance.

6. Update Account
Users can update their account information, such as the username or password.

7. Delete Account
Users can delete their account, and all related data will be removed from the system.

Files and Folders
app.py: Main application file that contains routes and app logic.
templates/: Folder containing HTML files for rendering.
homepage.html: The homepage that shows options after login.
login.html: Login form for existing users.
register.html: Registration form for new users.
deposit.html: Page to deposit funds.
withdraw.html: Page to withdraw funds.
update_account.html: Page to update user account details.
static/: Folder containing CSS files for styling.
styles.css: The CSS file that styles the web pages.



Official Flask documentation: https://flask.palletsprojects.com/

Official SQLAlchemy documentation: https://docs.sqlalchemy.org/