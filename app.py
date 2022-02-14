import streamlit as st
import pickle
import pandas as pd
import requests

st.title('Movie Recommender System')

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    list_of_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movie_names = []
    recommend_movie_posters = []
    for i in list_of_movies:
        movie_id = movies.iloc[i[0]].id
        recommend_movie_posters.append(fetch_poster(movie_id))
        # fetch poster from
        recommend_movie_names.append(movies.iloc[i[0]].title)
    return recommend_movie_names, recommend_movie_posters


movies = pickle.load(open('movies.pkl','rb'))

similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    'Select a Movie from drop down',
    movie_list)

st.write('You selected:', selected_movie)


if st.button('Show Recommend Movies'):
    recommended_movie_names, recommend_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommend_movie_posters[0])

    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommend_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommend_movie_posters[2])

    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommend_movie_posters[3])

    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommend_movie_posters[4])
