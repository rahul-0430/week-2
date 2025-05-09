import hashlib

user_db = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in user_db:
        return "User already exists"
    hashed = hash_password(password)
    user_db[username] = hashed
    return "Created new user"

def login(username, password):
    
    hashed = hash_password(password)
    if username in user_db and user_db[username] == hashed:
        return "Login Successful"
    return "Invalid credentials"

print(register("john", "mypassword"))  
print(login("john", "mypassword"))     
print(login("john", "wrongpass"))     
