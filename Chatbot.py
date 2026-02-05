import datetime

def chatbot(user_input):
    user_input = user_input.lower()

    # Greetings
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! How can I help you today?"

    # Name
    elif "your name" in user_input:
        return "I am a rule-based chatbot written in Python."

    # How are you
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking "

    # Date
    elif "date" in user_input:
        today = datetime.date.today()
        return f"Today's date is {today}"

    # Time
    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"Current time is {now}"

    # Simple math (addition)
    elif "add" in user_input:
        try:
            numbers = [int(s) for s in user_input.split() if s.isdigit()]
            return f"The sum is {sum(numbers)}"
        except:
            return "Please provide numbers to add."

    # Subtraction
    elif "subtract" in user_input:
        try:
            numbers = [int(s) for s in user_input.split() if s.isdigit()]
            return f"The result is {numbers[0] - numbers[1]}"
        except:
            return "Please provide two numbers."

    # Multiplication
    elif "multiply" in user_input:
        try:
            numbers = [int(s) for s in user_input.split() if s.isdigit()]
            return f"The result is {numbers[0] * numbers[1]}"
        except:
            return "Please provide numbers to multiply."

    # Division
    elif "divide" in user_input:
        try:
            numbers = [int(s) for s in user_input.split() if s.isdigit()]
            return f"The result is {numbers[0] / numbers[1]}"
        except:
            return "Please provide valid numbers."

    # Help
    elif "help" in user_input:
        return (
            "I can help with:\n"
            "- Greetings\n"
            "- Date & time\n"
            "- Simple math (add, subtract, multiply, divide)\n"
            "- Basic questions"
        )

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a nice day "

    # Unknown
    else:
        return "Sorry, I don't have an answer for that yet."

# Chat loop
print("Chatbot: Hello! Type 'exit' to stop.")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    print("Chatbot:", chatbot(user))
