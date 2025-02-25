class startapp:
    def __init__(self, username, password, customer):
        self.username = username
        self.password = password
        self.customer = customer

    def display_info(self):
        print(f"Admin Username: {self.username}")
        print(f"Managing Customer: {self.customer}")


admin1 = Admin("admin123", "securepass", "John Doe")


admin1.display_info()
