def score_function_recommendation(Q, V):
  score0 = 0.0
  score1 = 0.0
  sum_score = 0.0
  boost = 1.0
  if match('genres') and match("adult") and not match('title'):
    aggregate_max("total max_rating", "rating")
    aggregate_avg("total avg_rating", "rating")
    aggregate_min("total min_rating", "rating")
    aggregate_max("total max_popularity", "popularity")
    aggregate_avg("total avg_popularity", "popularity")
    
    score1 = rarity_sum('genres')
    score1 += 20.0

    if match('belongs_to_collection'):
      boost = 2.0

    if match('production_companies'):
      score1 += rarity_sum('production_companies')
      
    if V["rating"] >= 7.0:
        aggregate_count("count movies with rating >= 7.0")
        aggregate_avg("avg revenue for rating >= 7.0", "revenue")
        score0 += 10.0
    elif V["rating"] >= 6.5:
        score0 += 6.0
    elif V["rating"] < 4.5:
        score0 -= 2.0
    score1 = max(score0, score1)

    boost = 1.0
    if match('belongs_to_collection'):
        boost = 2.0

    if V["budget"] >= 1000000:
        aggregate_avg("avg revenue for movies with budget >= 1m", "revenue")
        score0 += 5.0

    sum_score = boost * (score0 + score1)

    if V["runtime_days"] > 200:
      aggregate_avg("avg revenue for movies with runtime_days > 200d", "revenue")
      sum_score = sum_score + 8

    return boost * sum_score
