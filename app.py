import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    # Replace with your TMDb API key
    api_key = 'b4826f0e46bd2d17a760450da9235f85'
    # Fetch movie details from TMDb API
    movie_url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(movie_url)
#poster_path : "/6ojHgqtIR41O2qLKa7LFUVj0cZa.jpg"
    if response.status_code == 200:
        movie_data = response.json()
        poster_path = movie_data['poster_path']
        poster_url = f'https://image.tmdb.org/t/p/w500{poster_path}'
        print("Poster URL:", poster_url)
        return poster_url
    else:
        print("Failed to fetch movie data.")


def recommend_movies(movie_name):
    movie_index = movie[movie['title_x'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for j in movies_list:
        movie_id = movie.iloc[j[0]].movie_id
        recommended_movies.append(movie.iloc[j[0]].title_x)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movie = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')

selected_Movie_name  = st.selectbox(
    'Movie List',
    movie['title_x'].values)

if  st.button('Recommend'):
    recommendation,posters = recommend_movies(selected_Movie_name)

    col1,col2,col3,col4,col5 = st.columns (5)
    with col1:
        st.text(recommendation[0])
        st.image(posters[0])
        #st.image("https://image.tmdb.org/t/p/w500/6ojHgqtIR41O2qLKa7LFUVj0cZa.jpg")
    with col2:
        st.text(recommendation[1])
        st.image(posters[1])
        #st.image("https://image.tmdb.org/t/p/w500/6ojHgqtIR41O2qLKa7LFUVj0cZa.jpg")
    with col3:
        st.text(recommendation[2])
        #st.image("https://image.tmdb.org/t/p/w500/6ojHgqtIR41O2qLKa7LFUVj0cZa.jpg")
        st.image(posters[2])
    with col4:
        st.text(recommendation[3])
        #st.image("https://image.tmdb.org/t/p/w500/6ojHgqtIR41O2qLKa7LFUVj0cZa.jpg")
        st.image(posters[3])
    with col5:
        st.text(recommendation[4])
        #st.image("https://image.tmdb.org/t/p/w500/6ojHgqtIR41O2qLKa7LFUVj0cZa.jpg")
        st.image(posters[4])


    #for i in recommendation:
        #st.write(i)
