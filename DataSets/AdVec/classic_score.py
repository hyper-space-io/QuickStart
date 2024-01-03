def score_function_recommendation(params, doc):
    if match("bundle_id"):
        return 0.0
    score = 1.0

    if match("categories"):
        score+=rarity_sum("categories")
    
    if doc["ios"]:
        score *= 2



    return score
    
