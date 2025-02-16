
# import streamlit as st
# import google.generativeai as genai

# genai.configure(api_key="AIzaSyDCGolvypLlaYmXE0wtrIix3r1mys9k5-s")

# available_models = ["models/gemini-1.5-pro-latest", "models/gemini-1.5-flash-latest"] 

# def get_chat_response(prompt,  model):
#   """Sends a prompt to the Gemini model and returns the response."""
#   model_instance = genai.GenerativeModel(model) 
#   response = model_instance.generate_content(prompt) 
#   return response.text

# def main():
#   st.title("InfoGenie AI") 

#   # Model Selection
#   selected_model = st.selectbox("Choose a Gemini Model:", available_models)

#   # Parameter Controls
#   temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7, step=0.01)
#   top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=0.9, step=0.01)

#   user_input = st.text_input("You:")

#   if user_input:
#     bot_response = get_chat_response(user_input,  selected_model)
#     st.text("InfoGenie AI" + bot_response)

# if __name__ == "__main__":
#   main()

'''
Revised code updated BY LC

'''
import streamlit as st
import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyDCGolvypLlaYmXE0wtrIix3r1mys9k5-s")  

# Available Gemini models
available_models = ["models/gemini-1.5-pro-latest", "models/gemini-1.5-flash-latest"] 

def get_chat_response(prompt, model):
    """Sends a prompt to the Gemini model and returns the response."""
    model_instance = genai.GenerativeModel(model)

    # Gemini's generation config (no temperature or top_p directly)
    generation_config = genai.GenerationConfig(
        #  These are some of the parameters you *can* control.
        #  Experiment to see their effects.
        max_output_tokens=2048,  # Adjust as needed
        # stop_sequences=["\n"],  # Example: stop on a newline
    )

    response = model_instance.generate_content(
        prompt,
        generation_config=generation_config  # Use the config
    )
    return response.text

def main():
    st.title("InfoGenie AI")

    # Model Selection (simplified)
    selected_model = st.selectbox("Choose a Gemini Model:", available_models)

    user_input = st.text_area("You:", height=150) # Use text_area for longer input/output

    if user_input:
        with st.spinner("Generating response..."): 
            bot_response = get_chat_response(user_input, selected_model)
            st.markdown("InfoGenie AI:\n\n" + bot_response)  

if __name__ == "__main__":
    main()
