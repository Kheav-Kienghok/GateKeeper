# Login and Register with UI

## Project Overview
This project provides basic user authentication for accessing a website. Users can register an account to gain access to the system.

## Features
- **User Authentication:**
  - Users can register an account.
  - Users can log in using their registered credentials.
- **Password Security:**
  - Passwords are hashed for added security (currently implemented as basic encryption).

## Technologies Used
### Frontend/UI:
- **HTML**
- **CSS**
- **JavaScript**

### Backend:
- **Flask** (Python) to handle interactions between the frontend and backend.

## Current Security Measures
- Password hashing (basic encryption).


## Installation and Setup
### Prerequisites:
- Python 3.x installed on your system.
- A virtual environment tool such as `venv` or `virtualenv` (optional but recommended).

### Steps:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kheav-Kienghok/GateKeeper.git
   cd GateKeeper

2. **Create and activate a virtual environment (optional):**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run the application:**
    ```bash
    python app.py

5. **Access the application: Open a web browser and navigate to *http://127.0.0.1:5000***

## Usage Instructions

1. **Register an account** through the user interface:
   - Fill in the registration form with your username, email, and password.
   - The password will be securely hashed before being stored.
   
2. **Log in with your registered credentials**:
   - Enter your username and password.
   - The application will verify your credentials and log you in if they match.

3. **Access secured sections of the website**:
   - Once logged in, you will have access to protected pages that require authentication.
   - You can also log out anytime using the logout option in the navigation menu.

## Application Preview

Here is a `.gif` demonstrating how the application works, including registration and login:

![Application Preview](static\img\demo.gif)

This `.gif` shows the process of registering an account, logging in with credentials, and accessing the secured sections of the website.

### Directory Structure
```bash
project-folder/
├── instance/           # Contain Database
├── static/             # Contains CSS, JavaScript, and images
├── templates/          # Contains HTML templates
├── app.py              # Main Flask application
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```
---

## Notes

This project serves as a foundation for implementing user authentication. Future updates will focus on improving security and expanding functionality.


## Troubleshooting

- **Flask Not Running**: If the application fails to start, ensure all dependencies are installed by running `pip install -r requirements.txt`.
- **Port Binding Issues**: If you can't access the application at `http://127.0.0.1:5000/`, the port might be in use. Try changing the port by modifying `app.py` like this:
  ```python
  app.run(host='127.0.0.1', port=5001)  # Change to another port if needed

## Future Improvements
- **Enhanced Security**:
  - Implement more secure password hashing algorithms like Argon2 or PBKDF2.
  - Add multi-factor authentication (MFA).
  
- **User Roles**:
  - Implement different user roles (e.g., admin, regular user) to grant varying levels of access.
  
- **Email Verification**:
  - Add email verification upon registration to prevent spam or invalid users.