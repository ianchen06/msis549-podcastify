import streamlit as st
import requests
import newspaper

st.set_page_config(page_title="Podcastify", page_icon="🎧", layout="wide")

col1, col2 = st.columns(2)
with col1:
  st.title("🎧 Podcastify")
  st.header("Too busy to read📖? Just listen with Podcastify🎧.")
  st.write("Enter the URL of an article to generate a podcast.")
  url = st.text_input("Enter URL")

with col2:
   st.image("./image.png")

data = {
  "summary": "The article discusses the technical workings of in-context learning in large language models (LLMs) and seeks a non-anthropomorphic explanation of its effectiveness. Commenters debate whether LLMs are truly 'intelligent' or just statistical models responding to token patterns. The primary theory is that in-context examples help fine-tune the attention mechanism to focus on relevant tokens, enhancing the model's output accuracy. This is achieved without actual learning, as the model parameters remain unchanged but are better aligned with the expected output through the examples provided.",
  "keywords": ["in-context learning", "large language models"]
}

if url:
    content = newspaper.article(url)

    st.header("Summary")

    st.write(data['summary'])

    st.write("Keywords: ", ", ".join(data['keywords']))

    with st.expander("Original Content"):
        st.write(content.text)