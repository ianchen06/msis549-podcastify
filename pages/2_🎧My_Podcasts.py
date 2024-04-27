import streamlit as st

num_days = 7

st.title("🎧 MyPodcasts")

podcasts = [
    {"title": "Code and Coffee: Morning Thoughts on Tech and Trends", "date": "2024-04-27"},
    {"title": "Asanas Abroad: Exploring Yoga Retreats Around the Globe", "date": "2024-04-26"},
    {"title": "Onsen Escapades: Soaking in the Serenity of Japan’s Hot Springs", "date": "2024-04-25"},
]

for p in podcasts:
    st.header(p["title"])
    st.write(f"{p['date']}")
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("./mic.png")
    with col2:
        st.audio(f'./podcasts/{p["date"]}.wav', format='audio/wav')
        st.write(f"Description: This podcast covers the latest trends in AI, from machine learning to business ideas.")
        st.write(f"Duration: 2:20 minutes")
        st.write(f"Speakers: Host & Guest")
        st.write(f"Topics: Machine Learning, AI, Large Language Models")
        st.write(f"Transcript: [Download](#)")
        st.write(f"Audio: [Listen](#)")
        st.write(f"Share: [Twitter](#) [Facebook](#) [LinkedIn](#)")


