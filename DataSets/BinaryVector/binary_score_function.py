
def some_sf(Q, V):
  score = 0.0
  if match("country"):
    score = 5.0
    if match("street"):
      score = 10.0
  return score
