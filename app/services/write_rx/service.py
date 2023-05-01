import streamlit as st
import openai

# Replace with your OpenAI API key, or set it as an environment variable in your deployment settings
openai.api_key = st.secrets["OPENAI_API_KEY"]


# Define the OpenAI chat completion function
def generate_response(prompt):
    # Construct the chat messages for the API prompt
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that generates user stories based on the given information",
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]
    st.markdown("----")
    res_box = st.empty()
    report = []

    for resp in openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Using GPT-3's Davinci engine
        messages=messages,
        stream=True,
        temperature=0.2,
        presence_penalty=-2,
    ):
        # join method to concatenate the elements of the list
        # into a single string,
        # then strip out any empty strings
        if "content" in resp.choices[0].delta:
            report.append(resp.choices[0].delta.content)
            result = "".join(report).strip()
            # result = result.replace("\n", "")
            res_box.markdown(f"*{result}*")
