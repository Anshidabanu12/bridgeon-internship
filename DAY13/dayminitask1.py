import bcrypt
#bcrypt: python libraray
users={}

email = input("enter email")
password = input("enter password")

hash_password = bcrypt.hashpw(
    password.encode(),
    bcrypt.gensalt()
).decode()
users[email] = hash_password
print("user register successfully")
print(users)