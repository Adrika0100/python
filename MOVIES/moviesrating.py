import numpy as np
import pandas as pd

# Load the data from CSV files
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Merge the data based on 'movieId'
movie_ratings = pd.merge(ratings, movies, on='movieId')

# Calculate average ratings for each movie 
average_ratings = movie_ratings.groupby('title')['rating'].mean()

# Calculate the number of ratings for each movie
num_ratings = movie_ratings.groupby('title')['rating'].count()

# Create a DataFrame combining average rating and number of ratings
movie_info = pd.DataFrame({'Average Rating': average_ratings, 'Number of Ratings': num_ratings})

# Sort the movies based on average rating and number of ratings
top_rated_movies = movie_info.sort_values(by=['Average Rating', 'Number of Ratings'], ascending=False)

# Display the top-rated movies
print("Top 10 Movies (Pandas):")
print(top_rated_movies.head(10))

# perform some calculations
average_rating_numpy = np.mean(ratings['rating'])  # Calculate the overall average rating
max_rating_numpy = np.max(ratings['rating'])      # Find the maximum rating

print("\nOverall Average Rating :", average_rating_numpy)
print("Maximum Rating :", max_rating_numpy)
