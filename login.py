def login(username, password):
    # Example credentials
    correct_username = "user"
    correct_password = "pass123"

    if username == correct_username and password == correct_password:
        return "Login successful!"
    else:
        return "Invalid credentials!"
