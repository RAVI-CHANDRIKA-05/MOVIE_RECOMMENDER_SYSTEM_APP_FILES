# <span style='color:Blue'> A MOVIE RECOMMENDER SYSTEM </span>
This repository contains code to build a moview recommender system
This system is build using streamlit on heroku.

An app is created for the benifit of users where 5 movies are suggested based on the selection. 

✨[Movie recommender system: Web App](https://movie-recommender-system-ravi.herokuapp.com/)<br>



Files to create a movie recommend-er system


## Why Do We Need Recommender Systems?
We live in “era of abundance”. For any product, there are always plethora of options to choose from. Recommender systems are utilized in a variety of areas including movies, music, news, books, research articles, search queries, social tags, and products in general. Recommender systems help businesses to suggest personalized content or products to a users. From a business standpoint, the more relevant products a user finds on the platform, the higher their engagement. This often results in increased revenue for the platform itself. Various sources say that as much as 35–40% of tech giants’ revenue comes from recommendations alone.

## Types of Recommender Systems
Machine learning algorithms in recommender systems typically fit into two categories: content-based systems and collaborative filtering systems. Modern recommender systems combine both approaches.
## A) Content-Based Movie Recommendation Systems
Content-based methods are based on the similarity of movie attributes. Using this type of recommender system, if a user watches one movie, similar movies are recommended. For example, if a user watches a comedy movie starring Adam Sandler, the system will recommend them movies in the same genre or starring the same actor, or both. 
## B) Collaborative Filtering Movie Recommendation Systems
With collaborative filtering, the system is based on past interactions between users and movies. With this in mind, the input for a collaborative filtering system is made up of past data of user interactions with the movies they watch. For example, if user A watches M1, M2, and M3, and user B watches M1, M3, M4, we recommend M1 and M3 to a similar user C. 

## The Dataset
For this project we will use a tmdb data for 5000 movies and use 'genres', 'id', 'keywords', 'title, 'overview', 'cast', 'crew' to build our model.

## Implementation
For this recommender system, I have used content-based filtering. I converted data of top 3 actors from cast, director from crew, genres, keywords, over view to tags. Then I used a cosine similarity function on tags to calculate the distance between the tags. Cosine similarity of 1 means high similarity and 0 means low similarity. It is a numeric quantity that denotes the similarity between two movies. Now this model will suggest five movies that are most similar to a particular movie which a user selects in the webapp. 
