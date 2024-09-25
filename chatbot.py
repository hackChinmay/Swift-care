import openai
import sqlite3
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up your OpenAI API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")
# Set up your OpenAI API key

def get_college_info(question):
    try:
        # Connect to your college database
        conn = sqlite3.connect('instance/college_info.db')
        cursor = conn.cursor()

        # Search for the relevant answer in the database
        cursor.execute("SELECT answer FROM info WHERE question LIKE ?", ('%' + question + '%',))
        result = cursor.fetchone()

        conn.close()  # Don't forget to close the connection

        if result:
            return result[0]
        else:
            return None
    except sqlite3.OperationalError as e:
        # If the table does not exist, log the error and return None
        print(f"Database error: {e}")
        return None

def chatbot(prompt):
    # Use the new ChatCompletion API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use 'gpt-4' if available
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    
    return response['choices'][0]['message']['content'].strip()

def college_chatbot(user_input):
    # Try fetching info from the college database
    college_response = get_college_info(user_input)
    
    if college_response:
        return college_response
    else:
        # If no info is found, ask OpenAI GPT for help
        return chatbot(user_input)
