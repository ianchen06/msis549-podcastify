import streamlit as st

st.title("🔎 Research")

st.write("Enter a topic and our crew of AI researchers will find the latest articles for you.")

topic = st.text_input("Enter a topic")

is_search = st.button("Search")

if topic and is_search:
    st.write("Here are the latest articles on", topic)

    st.write("1. [The article discusses the technical workings of in-context learning in large language models (LLMs) and seeks a non-anthropomorphic explanation of its effectiveness. Commenters debate whether LLMs are truly 'intelligent' or just statistical models responding to token patterns. The primary theory is that in-context examples help fine-tune the attention mechanism to focus on relevant tokens, enhancing the model's output accuracy. This is achieved without actual learning, as the model parameters remain unchanged but are better aligned with the expected output through the examples provided.](https://www.example.com)")

    st.write("2. [The article discusses the technical workings of in-context learning in large language models (LLMs) and seeks a non-anthropomorphic explanation of its effectiveness. Commenters debate whether LLMs are truly 'intelligent' or just statistical models responding to token patterns. The primary theory is that in-context examples help fine-tune the attention mechanism to focus on relevant tokens, enhancing the model's output accuracy. This is achieved without actual learning, as the model parameters remain unchanged but are better aligned with the expected output through the examples provided.](https://www.example.com)")

    st.write("3. [The article discusses the technical workings of in-context learning in large language models (LLMs) and seeks a non-anthropomorphic explanation of its effectiveness. Commenters debate whether LLMs are truly 'intelligent' or just statistical models responding to token patterns. The primary theory is that in-context examples help fine-tune the attention mechanism to focus on relevant tokens, enhancing the model's output accuracy. This is achieved without actual learning, as the model parameters remain unchanged but are better aligned with the expected output through the examples provided.](https://www.example.com)")