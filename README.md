# AI Trivia Game & Chatbot

## Overview

This project is a **Python-based AI Trivia Game and Chatbot** using **OpenAI's GPT-3 API**. The AI-powered trivia game generates questions, evaluates answers, and tracks scores. The chatbot interacts with users by generating conversational responses.

## Features

### 🎮 AI Trivia Game (`ai_trivia_game.py`)

- Generates trivia questions using **OpenAI GPT-3**.
- Allows users to input answers and checks correctness.
- Tracks and displays the player's score.
- Gives users the option to play multiple rounds.

### 🤖 Chatbot (`chatbot.py`)

- Simulates **human-like conversations** using OpenAI’s API.
- Reads user input and generates responses dynamically.
- Runs continuously until the user says "bye".

## Installation

To set up and run this project, follow these steps:

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/AI-Trivia-Chatbot.git
cd AI-Trivia-Chatbot
```

### **2. Set Up a Virtual Environment (Optional, but Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### **3. Install Dependencies**

```bash
pip install openai
```

### **4. Set Your OpenAI API Key**

Before running the scripts, set your **OpenAI API key** as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key-here"  # On Mac/Linux
set OPENAI_API_KEY="your-api-key-here"     # On Windows
```

## Running the Application

### **🎮 Run the Trivia Game**

```bash
python ai_trivia_game.py
```

### **🤖 Run the Chatbot**

```bash
python chatbot.py
```

## Usage

### **🎮 AI Trivia Game**

- The game **generates a trivia question**.
- The user enters an answer.
- The game compares the user’s answer with **GPT-3’s response**.
- The score updates after each round.

**Example Output:**

```
AI Trivia Question: What is the capital of Japan?
Your answer: Tokyo
Correct!
Current Score: 1
Do you want to play again? (y/n): y
```

### **🤖 AI Chatbot**

- The chatbot **reads user input** and generates responses.
- The conversation continues until the user types "bye".

**Example Chat Output:**

```
You: Hello!
Chatbot: Hi there! How can I assist you today?
You: Tell me a joke.
Chatbot: Why don’t skeletons fight each other? Because they don’t have the guts!
You: Bye
Chatbot: Goodbye! Have a great day.
```

## License

This project is licensed under the **MIT License**.

## Contributions

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit and push your changes.
4. Open a pull request.

## Contact

For any questions or support, please open an issue on GitHub.

