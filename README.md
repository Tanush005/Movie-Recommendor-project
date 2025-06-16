
# 🎬BingeBuddy

A content-based movie recommendation system that suggests similar movies based on cosine similarity of movie features.



## Features

- Recommends 10 most similar movies based on user selection
- Clean, responsive UI with dark theme
- Fast recommendations using pre-computed similarity matrix
- Intuitive interface with movie selection dropdown

## How It Works

The recommendation system uses **content-based filtering** with **cosine similarity**:

1. **Data Processing**: 
   - Movie features (like genres, keywords, cast, crew) are combined into a single text representation
   - Text data is vectorized using TF-IDF (Term Frequency-Inverse Document Frequency)

2. **Similarity Calculation**:
   - Cosine similarity is computed between all movie vectors
   - The similarity matrix is pre-computed for faster recommendations

3. **Recommendation Engine**:
   - When a user selects a movie, the system finds the most similar movies based on the pre-computed similarity scores
   - Top 10 most similar movies (excluding the selected one) are returned

## Technologies Used

- Python
- Streamlit (for web interface)
- Scikit-learn (for TF-IDF and cosine similarity)
- Pandas (for data manipulation)
- Pickle (for storing pre-computed data)

## Dataset

The system uses a movie dataset containing:
- Movie titles
- Genres
- Keywords
- Cast information
- Crew information
- Other relevant features

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
