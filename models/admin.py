class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display_info(self):
        print(f"Admin Username: {self.username}")

    def change_password(self, new_password):
        self.password = new_password
        print("Password changed successfully!")

# Creating an admin object
admin1 = Admin("admin123", "securepass")

# Displaying admin info
admin1.display_info()

# Changing the admin password
admin1.change_password("newsecurepass")
