# import json

import streamlit as st
# import numpy as np
# import torchaudio
# import torch

# from ljspeech_tts import generate_podcast
# from libretts_tts import speak

st.title("🎧 Podcastify")

tab1, tab2 = st.tabs(["Solo", "Host & Guest"])

with tab1:
    text = st.text_area("Enter text to convert to speech", height=100, key="solo")

    with st.expander("Sample Transcript"):
        st.code("""
[
    {"speaker": "Host", "content": "Welcome back to our travel insights podcast. Today, we're going to dive into the exciting process of planning a trip to Japan."},
    {"speaker": "Guest", "content": "Thanks for having me! Japan is a fascinating destination with so much to offer, from its rich culture to its stunning landscapes."},
    {"speaker": "Host", "content": "Absolutely! Let's start with when is the best time to visit Japan?"},
    {"speaker": "Guest", "content": "Spring and fall are ideal because of the mild weather and beautiful cherry blossoms in spring or colorful leaves in fall."},
    {"speaker": "Host", "content": "Great advice! And what are some must-visit places for first-timers?"},
    {"speaker": "Guest", "content": "You can't miss Tokyo for its bustling city life, Kyoto for traditional temples, and Hokkaido for amazing natural scenery."},
    {"speaker": "Host", "content": "Sounds wonderful. Any tips on budgeting for the trip?"},
    {"speaker": "Guest", "content": "Plan ahead for transportation with options like the Japan Rail Pass and look for accommodations ranging from hotels to guesthouses to save money."},
    {"speaker": "Host", "content": "Thank you for all the great tips. It sounds like a trip to Japan needs thoughtful planning but offers incredible rewards."}
]
""")

    # wavs = []
    # if text:
    #     audio = generate_podcast(text)
    #     wavs.append(audio)

    #     wav = np.concatenate(wavs)
    #     torchaudio.save("output.wav", torch.from_numpy(wav).unsqueeze(0), 24000)
    #     st.audio("output.wav")

with tab2:
    text = st.text_area("Enter text to convert to speech", height=100, key="duo")

    # wavs = []
    # if text:
    #     data = json.loads(text)
    #     #audio = generate_podcast(text)

    #     for r in data:
    #         if r['speaker'] == "Host":
    #             audio = speak(r['content'], 0)
    #         elif r['speaker'] == "Guest":
    #             audio = speak(r['content'], 1)
    #         wavs.append(audio)

    #     wav = np.concatenate(wavs)
    #     torchaudio.save("output.wav", torch.from_numpy(wav).unsqueeze(0), 24000)
    #     st.audio("output.wav")