
def similarity_sf(params, doc):
    score = 0.0
    
    if match('categories'):    
        if match('submitter'):
            score += 1
        
        if doc['license'] is None:
            score *= 0.2
        
        
    if match('title'):
        score = 0
        
    return score
