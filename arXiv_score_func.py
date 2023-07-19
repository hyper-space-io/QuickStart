
def similarity_sf(Q, V):
    score = 0.0
    
    if match('categories'):
        
        # boost more recent stuff
        #if window_match('update_date_ts', '2d', '1d'):
        #    score += 3
        #if window_match('update_date_ts', '3d', '1d'):
        #    score += 1
 
         
        if match('submitter'):
            score += 1
        
        if Q['license'] is None:
            score *= 0.2
        
        
    if match('title'):
        score = 0
        
    return score
