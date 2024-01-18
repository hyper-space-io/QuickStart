import random


def gen_local_doc_subset(hyperspace_client, collection_name, doc_subset, max_doc_index, subset_doc_count) :

    # building subset document dictionary
    for i in range(subset_doc_count) :
        random_integer = random.randint(1, max_doc_index)
        doc_temp = hyperspace_client.get_document(collection_name, str(random_integer))
        doc_subset.append(doc_temp)

    return doc_subset



# building rundom query document (supperposition of fields from the subset documents
# each pass will create another query_doc

def gen_query_doc(config, doc_subset, subset_doc_count ) :
    # assume global "config", "doc_subset", "subset_doc_count"
    query_doc = {}


    for field in config["configuration"].keys():
        random_subset_doc_index = random.randint(0, subset_doc_count-1)
    
        if field in doc_subset[random_subset_doc_index] :
            # I assume that if field exist, then not null
            query_doc[field] = doc_subset[random_subset_doc_index][field]
        else :
            # "Field not in document "
            query_doc[field] = None
            
    if 0 :
        print("Current query document :\n")
        sfunc.pprint(query_doc)
        print()
    
    return query_doc

