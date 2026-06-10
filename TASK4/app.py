import streamlit as st

st.set_page_config(page_title="Movie Recommendation System")

st.title("🎬 Movie Recommendation System")

movies = {
    "Action": [
        "John Wick",
        "Avengers Endgame",
        "Mad Max Fury Road"
    ],
    "Comedy": [
        "The Mask",
        "Home Alone",
        "Mr Bean's Holiday"
    ],
    "Sci-Fi": [
        "Interstellar",
        "Inception",
        "The Martian"
    ],
    "Horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle"
    ]
}

genre = st.selectbox(
    "Choose your favorite genre",
    list(movies.keys())
)

if st.button("Recommend Movies"):
    st.subheader("Recommended Movies")
    for movie in movies[genre]:
        st.write("✅", movie)
