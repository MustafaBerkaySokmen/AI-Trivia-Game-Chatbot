import openai

# Set your OpenAI API key here
openai.api_key = "Set your OpenAI API key here"

# Define a function that uses the OpenAI API to generate a question and answer
def generate_question():
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a trivia question",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    question = response.choices[0].text.strip()
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Answer the following question: " + question + "\n\nAnswer:",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    answer = response.choices[0].text.strip()
    return question, answer

# Define the main function to run the game
def trivia_game():
    print("Welcome to the trivia game powered by OpenAI!")
    score = 0
    while True:
        question, answer = generate_question()
        print("Question:", question)
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            score += 1
            print("Correct! Your score is now", score)
        else:
            print("Incorrect. The correct answer is", answer)
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break
    print("Thanks for playing! Your final score is", score)

# Call the main function to run the game
if __name__ == "__main__":
    trivia_game()

