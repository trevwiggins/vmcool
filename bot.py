import os
import sys
from google import genai
from google.genai import types

def run_chatbot():
    # 1. Initialize the client.
    # It automatically picks up the GEMINI_API_KEY environment variable.
    try:
        client = genai.Client()
    except Exception as e:
        print(f"Error initializing client. Did you set your GEMINI_API_KEY? Details: {e}")
        sys.exit(1)

    # 2. Configure system instructions to give your chatbot a personality
    config = types.GenerateContentConfig(
        system_instruction="You are a helpful, witty, and concise AI assistant.",
        temperature=0.7,
    )

    # 3. Start a chat session using the recommended model for general text tasks
    # The chat object automatically handles the conversation history.
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=config
    )

    print("🤖 Gemini Chatbot Initialized! (Type 'quit' or 'exit' to stop)\n")

    # 4. Main conversation loop
    while True:
        try:
            user_input = input("You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit']:
                print("🤖 Chatbot: Goodbye!")
                break
                
            # Skip empty inputs
            if not user_input:
                continue

            # Send the message to the model
            print("🤖 Chatbot thinking...")
            response = chat.send_message(user_input)
            
            # Clean up the console line and print the response
            # '\033[A' moves the cursor up, '\033[K' clears the line
            sys.stdout.write("\033[A\033[K") 
            print(f"🤖 Chatbot: {response.text}\n")

        except KeyboardInterrupt:
            print("\n🤖 Chatbot: Conversation ended abruptly. Bye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}\n")

if __name__ == "__main__":
    run_chatbot()
