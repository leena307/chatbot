# # import streamlit as st
# # from openai import OpenAI

# # # Show title and description.
# # st.title("💬 Chatbot")
# # st.write(
# #     "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
# #     "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
# #     "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
# # )

# # # Ask user for their OpenAI API key via `st.text_input`.
# # # Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# # # via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
# # openai_api_key = st.text_input("OpenAI API Key", type="password")
# # if not openai_api_key:
# #     st.info("Please add your OpenAI API key to continue.", icon="🗝️")
# # else:

# #     # Create an OpenAI client.
# #     client = OpenAI(api_key=openai_api_key)

# #     # Create a session state variable to store the chat messages. This ensures that the
# #     # messages persist across reruns.
# #     if "messages" not in st.session_state:
# #         st.session_state.messages = []

# #     # Display the existing chat messages via `st.chat_message`.
# #     for message in st.session_state.messages:
# #         with st.chat_message(message["role"]):
# #             st.markdown(message["content"])

# #     # Create a chat input field to allow the user to enter a message. This will display
# #     # automatically at the bottom of the page.
# #     if prompt := st.chat_input("What is up?"):

# #         # Store and display the current prompt.
# #         st.session_state.messages.append({"role": "user", "content": prompt})
# #         with st.chat_message("user"):
# #             st.markdown(prompt)

# #         # Generate a response using the OpenAI API.
# #         stream = client.chat.completions.create(
# #             model="gpt-3.5-turbo",
# #             messages=[
# #                 {"role": m["role"], "content": m["content"]}
# #                 for m in st.session_state.messages
# #             ],
# #             stream=True,
# #         )

# #         # Stream the response to the chat using `st.write_stream`, then store it in 
# #         # session state.
# #         with st.chat_message("assistant"):
# #             response = st.write_stream(stream)
# #         st.session_state.messages.append({"role": "assistant", "content": response})

# import streamlit as st
# import google.generativeai as genai

# # Set your API key
# genai.configure(api_key="AIzaSyDCGolvypLlaYmXE0wtrIix3r1mys9k5-s")

# # Choose the Gemini model
# model = genai.GenerativeModel("models/gemini-1.5-pro-latest")

# def get_chat_response(prompt):
#   """Sends a prompt to the Gemini model and returns the response."""
#   response = model.generate_content(prompt)
#   return response.text

# def main():
#   st.title("Cognito Chatbot")

#   user_input = st.text_input("You:")

#   if user_input:
#     bot_response = get_chat_response(user_input)
#     st.text("Cognito: " + bot_response)

# if __name__ == "__main__":
#   main()



import streamlit as st
import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyDCGolvypLlaYmXE0wtrIix3r1mys9k5-s")

# Available Gemini models
available_models = ["models/gemini-1.5-pro-latest", "models/gemini-1.5-flash-latest"] 

def get_chat_response(prompt,  model):
  """Sends a prompt to the Gemini model and returns the response."""
  model_instance = genai.GenerativeModel(model) 
  response = model_instance.generate_content(prompt) 
  return response.text

def main():
  st.title("Merlin Magic") 

  # Model Selection
  selected_model = st.selectbox("Choose a Gemini Model:", available_models)

  # Parameter Controls
  temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.01)
  top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=0.9, step=0.01)

  user_input = st.text_input("You:")

  if user_input:
    bot_response = get_chat_response(user_input,  selected_model)
    st.text(" " + bot_response)

if __name__ == "__main__":
  main()
