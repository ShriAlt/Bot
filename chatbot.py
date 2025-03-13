import os
import google.generativeai as genai

# Set API key directly (avoid hardcoding in production)
API_KEY = "USE YOUR GOOGLE STUDIO API KEY"
genai.configure(api_key=API_KEY)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
)

# Start a chat session
chat_session = model.start_chat(
    history=[
        {
            "role": "user",
            "parts": [
                "a chatbot which will solve the python queries and can also hold conversation",
            ],
        },
        {
            "role": "model",
            "parts": [
                "Okay, I'm ready to be your Python chatbot! I can help you with Python queries, code snippets, and we can also have a conversation. Let's get started!\n\n**How I can help you with Python:**\n\n*   **Code Explanation:**  I can explain what a piece of Python code does.\n*   **Code Generation:** I can help you write snippets of Python code to achieve specific tasks.\n*   **Debugging:** I can help identify potential errors in your code and suggest fixes.\n*   **Syntax and Concepts:** I can explain Python syntax, data structures, algorithms, and other core concepts.\n*   **Library Usage:** I can guide you on how to use various Python libraries like `numpy`, `pandas`, `requests`, etc.\n*   **Best Practices:** I can suggest best coding practices for writing clean and efficient Python code.\n*   **Problem Solving:**  I can assist you in breaking down coding problems and finding solutions.\n\n**Beyond Python:**\n\n*   **Casual Conversation:** We can chat about almost anything. I enjoy learning new things and having interesting discussions.\n*   **General Knowledge:** I can try to answer general questions you have.\n*   **Creative Writing:**  I can help you with creative writing tasks like poems, stories, etc.\n\n**How to Use Me:**\n\n1.  **Ask Clearly:** The more specific your question, the better I can assist you.\n2.  **Provide Context:** If you're having a problem with your code, please share the relevant parts of it.\n3.  **Be Patient:** I'm still learning, and sometimes I might not get it exactly right. If that happens, please let me know and I will try again.\n4.  **Don't Hesitate to Ask Follow-Ups:** If my initial answer wasn't enough or raised new questions, feel free to continue the conversation.\n\n**Example Prompts:**\n\n*   \"How do I sort a list of dictionaries in Python?\"\n*   \"Explain the concept of list comprehension.\"\n*   \"Write a function that calculates the factorial of a number.\"\n*   \"What is the difference between a tuple and a list?\"\n*   \"I'm getting a 'TypeError' with my code, can you help me?\"\n*   \"Hi, how's your day going?\"\n*   \"Tell me a joke.\"\n\n**Okay, let's get started! What would you like to do first?**\n",
            ],
        },
    ]
)

# Handle user input and check for short queries like "i"
while True:
    message = input("You: ")

    # Check for short input and ask for more details
    if len(message.strip()) <= 1:
        print("Chatbot: Could you provide a more detailed question or query?")
    else:
        response = chat_session.send_message(message)
        print("Chatbot:", response.text)

        # Exit the loop if user types 'bye'
        if message.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
