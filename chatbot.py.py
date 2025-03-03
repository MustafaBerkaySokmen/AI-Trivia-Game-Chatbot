 
import openai

# Set your OpenAI API key here
openai.api_key = "Set your OpenAI API key here"

# Define a function that uses the OpenAI API to generate a response
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Define the main function to run the chatbot
def chatbot():
    print("Chatbot: Hi! I'm a chatbot powered by OpenAI. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye! Have a great day.")
            break
        response = generate_response(user_input)
        print("Chatbot:", response)

# Call the main function to run the chatbot
if __name__ == "__main__":
    chatbot()
