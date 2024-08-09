import re


def chatbot():
    print("Hello! I am a simple chatbot. How can I help you today?")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if re.search(r'\b(bye|exit)\b', user_input):
            print("Chatbot: Goodbye! Have a nice day!")
            break

        # Respond to greetings
        elif re.search(r'\b(hello|hi|hey)\b', user_input):
            print("Chatbot: Hi there! How can I assist you?")

        # Respond to inquiries about the weather
        elif re.search(r'\b(weather)\b', user_input):
            print("Chatbot: The weather is nice today!")

        # Respond to time-related queries
        elif re.search(r'\b(time)\b', user_input):
            print("Chatbot: I don't have a watch, but you can check the time on your device!")

        # Respond to date-related queries
        elif re.search(r'\b(date)\b', user_input):
            print("Chatbot: I don't keep track of dates, but you can easily find it on your calendar!")

        # Respond to favorite color inquiry
        elif re.search(r'\b(favorite color)\b', user_input):
            print("Chatbot: My favorite color is blue! What's yours?")

        # Respond to name-related queries
        elif re.search(r'\b(name)\b', user_input):
            print("Chatbot: I don't have a specific name, but you can call me Chatbot!")

        # Respond to joke requests
        elif re.search(r'\b(joke)\b', user_input):
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")

        # Respond to basic math queries
        elif re.search(r'\b(calculate|math)\b', user_input):
            print("Chatbot: I can help with basic math. Try asking a specific question like 'What is 2 + 2?'")

        # Handle specific math queries like "What is 2 + 2?"
        elif re.search(r'\b(what is)\b', user_input):
            try:
                # Extract the math expression
                equation = re.search(r'what is (.+)', user_input).group(1)
                result = eval(equation.strip())
                print(f"Chatbot: The result is {result}.")
            except:
                print("Chatbot: Sorry, I couldn't calculate that. Please make sure your input is correct.")

        # Respond to favorite food inquiry
        elif re.search(r'\b(favorite food)\b', user_input):
            print("Chatbot: I don't eat, but I've heard pizza is pretty popular!")

        # Respond to thank you
        elif re.search(r'\b(thank you|thanks)\b', user_input):
            print("Chatbot: You're welcome!")

        # Handle unknown queries
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")


if __name__ == "__main__":
    chatbot()
