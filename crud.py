
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

def add_user(user):
    users.append(user)

def get_user_by_id(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            return True
    return False

def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return True
    return False

print("Original users:", users)

add_user({"id": 3, "name": "Chae", "email": "chae@example.com"})
print("After adding Chae:", users)

print("Retrieve user with ID 2:", get_user_by_id(2))

update_user(1, name="Alicia")
print("After updating Alice:", users)

delete_user(2)
print("After deleting Bob:", users)
