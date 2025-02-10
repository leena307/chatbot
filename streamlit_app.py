import streamlit as st
import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyDCGolvypLlaYmXE0wtrIix3r1mys9k5-s")

# Choose the Gemini model
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

def get_chat_response(prompt):
  """Sends a prompt to the Gemini model and returns the response."""
  response = model.generate_content(prompt)
  return response.text

def main():
  st.title("Cognito Chatbot")

  user_input = st.text_input("You:")

  if user_input:
    bot_response = get_chat_response(user_input)
    st.text("Cognito: " + bot_response)

if __name__ == "__main__":
  main()
