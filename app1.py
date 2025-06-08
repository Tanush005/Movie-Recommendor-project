import streamlit as st
import pickle

# Set page configuration and styling
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        zoom: 1;
    }
    .recommendation-item {
        display: flex;
        align-items: center;
        margin: 8px 0;
        font-size: 18px;
        font-weight: 500;
        padding: 15px;
        background-color: #1a1a1a;  /* Dark background */
        color: white !important;   /* White text */
        border-radius: 8px;
        border-left: 4px solid #ff6b6b;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .recommendation-poster {
        margin-right: 15px;
        width: 80px;
        border-radius: 4px;
    }
    .main-content {
        max-width: 800px;
        margin: 0 auto;
    }
    </style>
""", unsafe_allow_html=True)
# Main content wrapper
st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)

# Load data
try:
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    movies = pickle.load(open('movies.pkl', 'rb'))
    movie1 = pickle.load(open('movie1.pkl', 'rb'))
    movies_list = movies['title'].values
except FileNotFoundError as e:
    st.error(f"Error loading data files: {e}")
    st.stop()

# Recommendation Function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended = []
    for i in movies_list:
        movie_data = movie1.iloc[i[0]]
        recommended.append(movie_data['title'])
    return recommended

# UI Layout - Select box centered above button
st.markdown("<br>", unsafe_allow_html=True)

# Create a container for the select box and button
container = st.container()

with container:
    # Select box centered
    option = st.selectbox(
        "🎞️ Choose a movie",
        movies_list,
        help="Select a movie to get recommendations"
    )

    # Button centered below select box
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        recommend_button = st.button('🎯 Get Recommendations', use_container_width=True)

# Recommendations container (will appear above button when generated)
recommendations_container = st.empty()

if recommend_button:
    with st.spinner('🔍 Fetching recommendations...'):
        recommendations = recommend(option)

    # Display recommendations in the container above the button
    with recommendations_container.container():
        st.markdown("<br><h3 style='text-align: center; color: #ff6b6b;'>🎯 Top Recommendations for you:</h3>",
                    unsafe_allow_html=True)

        # Display each recommendation in a clean format
        for i, title in enumerate(recommendations, 1):
            st.markdown(
                f'<div class="recommendation-item"><strong>{i}. {title}</strong></div>',
                unsafe_allow_html=True
            )

# Close main content wrapper
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<br><br>
<hr style="border:1px solid gray; margin-top: 50px;">
<p style="text-align:center; color: #888;"> Built with ❤️ by Tanush </p>
""", unsafe_allow_html=True)