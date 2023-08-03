# Movie Recommednation System Using Hyperspace Engine
This notebook demonstrates the use of Hyperspace engine to create a movie recommendation system, by first using classic search and then hybrid search, a combination of classic and vector searches, by combining  word embedding with metadata filtering. 

# The Datset
The data is taken from [MovieLens Latest Datasets](https://grouplens.org/datasets/movielens/latest/) and was downloaded from [Kaggle movie recommender system dataset ](https://www.kaggle.com/code/rounakbanik/movie-recommender-systems). The data includes 40954 valid movies. The data is in SQL format (table) and will be converted to NoSQL (documents) format. The data preprocessing is given in the notebook titles "MovieRecommendationDataPrep", available in this repository.


# The NoSQL Dataset Fields
The processed metadata includes the following fields:

1.   **adult** [boolean] - states if the movie is rated 18+
2.   **belongs_to_collection** [Keyword] - name of the collection that includes the movie. If the movie is not a part of a collection, value will be "None"
3. **budget** [integer] - The budget of the movie in USD
4. **genres** [list[Keyword]] - list of movie genres (i.e drama)
5. **id** [integer]] - unique id per movie
6. **original_language** [Keyword] - the original language in which the movie was produced
7. **popularity** [float] - the popularity of the movie, formulated as an unbounded score
8. **production_companies** [list[Keyword]] - list of production companies involved in the movie
9. **production_countries** [list[Keyword]] - list of all countries in which the movie was filmed
10. **rating** [float] - the movie IMDB weighted average rating  score
11. **release_date_unix_time** [int] - the movie release date in unix time
12. **revenue** [float] - the movie rvenue in [USD]
13. **runtime_days** [int] - the number cinema run time days
14. **spoken_languages** [list[Keyword]] - list of all languages spoken in the movie
15. **title** [Keyword] - the movie title
