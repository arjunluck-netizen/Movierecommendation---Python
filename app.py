import pickle
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

@st.cache_resource
def load_artifacts():
    with open("model/movies.pkl", "rb") as f:
        movies = pickle.load(f)
    with open("model/similarity.pkl", "rb") as f:
        similarity = pickle.load(f)
    return movies, similarity

movies, similarity = load_artifacts()

def recommend(movie, n=5):
    matches = movies[movies["title"].str.lower() == movie.lower()]
    if matches.empty:
        return []

    movie_index = matches.index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:n+1]

    return [
        {
            "title": movies.iloc[index]["title"],
            "score": float(score)
        }
        for index, score in movies_list
    ]

st.title("🎬 AI-Powered Movie Recommendation System")
st.write(
    "A content-based movie recommender built with Python, NLP, "
    "CountVectorizer and cosine similarity."
)

movie_options = sorted(movies["title"].dropna().unique())

selected_movie = st.selectbox(
    "Choose a movie you like:",
    movie_options
)

if st.button("🍿 Recommend Movies", use_container_width=True):
    results = recommend(selected_movie)

    st.subheader(f"Movies similar to {selected_movie}")

    if not results:
        st.warning("Movie not found.")
    else:
        for rank, item in enumerate(results, start=1):
            st.write(
                f"**{rank}. {item['title']}**  "
                f"(similarity: {item['score']:.2%})"
            )

st.divider()
st.caption("Dataset: TMDB 5000 Movie Dataset | Educational project")
