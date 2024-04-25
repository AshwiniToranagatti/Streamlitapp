import streamlit as st
import openai
import urllib3

urllib3.disable_warnings()
# Set up OpenAI API
openai.api_key = "sk-proj-ZHyDCIluXJu5RaWB1KyfT3BlbkFJCyN7H7N6UyWKf3Ck9PYY"

# Define Streamlit app
def main():
    st.title("PDF Chatbot")
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Process PDF file
        # You will need to implement the PDF processing logic here
        # Extract text from PDF and perform any necessary preprocessing
        
        # Chat interface
        user_input = st.text_input("You:", "")
        if st.button("Send"):
            try:
                # Call OpenAI API to generate response
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=user_input,
                    max_tokens=50
                )
                st.text_area("Bot:", response.choices[0].text.strip())
            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
