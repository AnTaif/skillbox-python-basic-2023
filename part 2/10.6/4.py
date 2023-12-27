class Chat:
    def __init__(self):
        self.messages = []

    def show_chat(self):
        print("Current chat:")
        for message in self.messages:
            print(message)

    def send_message(self, user_name, message):
        new_message = f"{user_name}: {message}"
        self.messages.append(new_message)
        print(f"Message sent: {new_message}")

chat = Chat()

while True:
    user_name = input("Enter your name: ")

    print("Menu:")
    print("1. Show current chat")
    print("2. Send a message")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        chat.show_chat()
    elif choice == "2":
        message = input("Enter your message: ")
        chat.send_message(user_name, message)
    else:
        print("Invalid choice. Please enter 1 or 2.")
