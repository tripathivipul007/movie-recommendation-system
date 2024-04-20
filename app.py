import pandas as pd
import streamlit as st
import pickle

# Load the movie dictionary from the pickle file
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))

# Convert the dictionary to a DataFrame
movies = pd.DataFrame(movies_dict)

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
    return recommended_movies

# Load the similarity matrix from the pickle file
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Define the file path to the downloaded image
background_image_path = 'moviebg.jpg'

# Display the background image without CSS styling
st.image(background_image_path, use_column_width=True)

# Set title and subtitle
st.title('Movie Recommender System')
st.subheader('Find similar movies based on your selection')

# Selectbox to choose a movie
selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

# Button to trigger recommendations
if st.button('Get Recommendations'):
    recommendations = recommend(selected_movie_name)
    if recommendations:
        st.subheader('Recommended Movies:')
        for i, movie in enumerate(recommendations, start=1):
            st.write(f"{i}. {movie}")
    else:
        st.write('No recommendations found for the selected movie.')
