# Movie Recommender System (Streamlit, Python, Cosine Similarity, Dropbox)

This is a movie recommender web app built with **Streamlit**, **Python**, and **Cosine Similarity** using movie metadata (genres, keywords, cast, and crew). It fetches movie posters and recommends similar movies based on user selection.

## Features
- **Movie Recommendation**: Select a movie, and the app will recommend similar movies based on cosine similarity.
- **Real-Time Fetching of Posters**: Movie posters are fetched using the **TMDb API**.
- **Dropbox Integration**: Large model files (e.g., `similarity.pkl`) are downloaded dynamically from **Dropbox** for efficient deployment.
- **Preprocessing with Pandas**: Movie metadata is preprocessed using **Pandas** for better recommendations.

## Technologies Used
- **Streamlit** for building the web app
- **Python** for data processing and recommendation system
- **Scikit-Learn** for **Cosine Similarity** computation
- **TMDb API** for fetching movie posters
- **Dropbox** for hosting large files like `similarity.pkl`

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/movie-recommender-streamlit.git
    ```

2. Navigate to the project directory:
    ```bash
    cd movie-recommender-streamlit
    ```

3. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## File Structure

