# openai.Completion depreciated: https://stackoverflow.com/questions/77469966/openai-api-error-you-tried-to-access-openai-completion-but-this-is-no-longer
# davinci-003 depreciated: https://community.openai.com/t/text-davinci-003-deprecated/582617/4


import openai
import streamlit as st

# Also experiment with: gpt-4-turbo-preview


# Sidebar for API key input
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="openai_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

# Set the GPT-3 API key
openai.api_key = openai_api_key

# Main app
st.title("📄 Text Summarizer")

article_text = st.text_area("Enter your scientific texts to summarize")
output_size = st.radio(label="What kind of output do you want?", 
                       options=["To-The-Point", "Concise", "Detailed"])

if output_size == "To-The-Point":
    out_token = 50
elif output_size == "Concise":
    out_token = 128
else:
    out_token = 516

if len(article_text) > 100:
    if st.button("Generate Summary", type='primary'):
        # Use GPT-3 to generate a summary of the article
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt="Please summarize this scientific article for me in a few sentences: " + article_text,
            max_tokens=out_token,
            temperature=0.5
        )
        # Display the generated summary
        res = response.choices[0].text.strip()
        st.success(res)
        st.download_button('Download result', res)
else:
    st.warning("Not enough words to summarize!")
