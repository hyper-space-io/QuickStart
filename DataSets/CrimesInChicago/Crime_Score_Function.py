def similarity_sf(Q, V):
    score = 0.0
    
    if match('Description') and not match('Case Number'):
        score = rarity_max('Description')
        if geo_dist_match('Location',40):
            score += 5
        if match('District') and window_match('Date', 100, 40):
            score -= 5
    if match('Block'):
        score += rarity_max('Block')
    return score
