import streamlit as st
import pickle
import pandas as pd
import requests
import os

# Streamlit page configuration (this must be called as the first Streamlit command)
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Constants
TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
POSTER_BASE_URL = "https://image.tmdb.org/t/p/w500/"
PLACEHOLDER_POSTER = "https://via.placeholder.com/500x750?text=Poster+Not+Available"
DROPBOX_URL = "https://www.dropbox.com/scl/fi/sn6l6lsej3hocytuebokv/similarity.pkl?rlkey=w9upnehw0uicpdmi9kbrlimup&st=q13as7wn&dl=1"
LOCAL_SIMILARITY_PATH = 'similarity.pkl'

# Fetch movie poster
def fetch_poster(movie_id):
    """Fetches the poster for a given movie using TMDb API."""
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        response = requests.get(url)
        data = response.json()
        poster_path = data.get('poster_path')
        return POSTER_BASE_URL + poster_path if poster_path else PLACEHOLDER_POSTER
    except Exception as e:
        st.error(f"Error fetching poster: {e}")
        return PLACEHOLDER_POSTER

# Recommend movies
def recommend(movie):
    """Recommends movies and fetches their posters."""
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_posters

# Download similarity.pkl from Dropbox
def download_similarity():
    """Downloads the similarity.pkl file from Dropbox if it does not exist locally."""
    if not os.path.exists(LOCAL_SIMILARITY_PATH):
        try:
            st.info("Downloading similarity.pkl from Dropbox...")
            response = requests.get(DROPBOX_URL)
            if response.status_code == 200:
                with open(LOCAL_SIMILARITY_PATH, 'wb') as f:
                    f.write(response.content)
                st.success(f"File downloaded successfully to {LOCAL_SIMILARITY_PATH}")
            else:
                st.error("Failed to download similarity.pkl from Dropbox")
        except Exception as e:
            st.error(f"Error downloading file: {e}")

# Load pre-trained data
download_similarity()  # Ensure similarity.pkl is downloaded

# Load movies data (adjust the path if needed)
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open(LOCAL_SIMILARITY_PATH, 'rb'))
movies = pd.DataFrame(movies_dict)

# Streamlit app UI
st.title("🎬 Movie Recommender System")
st.markdown(
    """
    Find your next favorite movie! Select a movie you like, and we'll recommend similar ones.
    """
)

# Movie selection
selected_movie_name = st.selectbox(
    "Select a movie:",
    movies['title'].values,
    help="Choose a movie to get recommendations based on your selection."
)

if st.button("Get Recommendations 🎥"):
    recommendations, posters = recommend(selected_movie_name)
    st.markdown("### Recommended Movies")
    
    # Display recommendations in a grid
    cols = st.columns(5, gap="medium")
    for col, movie, poster in zip(cols, recommendations, posters):
        with col:
            st.image(poster, caption=movie, use_container_width=True)
