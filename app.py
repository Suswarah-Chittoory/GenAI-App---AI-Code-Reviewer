from openai import OpenAI
import streamlit as st


#Read the api key and setup an openai client
f = open("keys\.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key = key)

st.title("💬 Python Code Reviewer")

#Take user input
prompt = st.text_area("Enter your python code")

#Generate User Response when clicking the button
if st.button("Review") == True:
    response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = [
                    {
                        "role": "system", "content": """You are a helpful AI Assistant.
                                                        Please review the following Python code and provide feedback on any potential bugs, errors, or areas for improvement."""
                    },

                    {"role": "user", "content": prompt}


                    ]
    )
    #Print the response
    st.write(response.choices[0].message.content)