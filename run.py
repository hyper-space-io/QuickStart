import numpy as np
import json
import search_master
from search_master import VectorDto

'''This code  demonstrates the use of Hyper Space hybrid search. The dataset is taken from [qdrant benchmarking 
sets]( https://github.com/qdrant/ann-filtering-benchmark-datasets#data) and includes a list of academic papers from 
arXiv, and their metadata. We will use the combination of an embedded vector data and metadata, to create a hybrid 
search. 

Setting up the Hyper Space environment
1. Download and install the client API
2. Create data config file
3. Connect to a server
4. Create collection
5. Ingest data
6. Run query
'''

# Set environment
conf = search_master.configuration.Configuration()
conf.host = 'https://search-master-demo.development.hyper-space.xyz'

hyperspace_client = search_master.SearchMasterApi(api_client=search_master.api_client.ApiClient(configuration=conf))
login_response = hyperspace_client.login({"username": username, "password": password})
api_client = search_master.api_client.ApiClient(configuration=conf,
                                                header_name='Authorization',
                                                header_value="Bearer " + login_response.token)

hyperspace_client = search_master.SearchMasterApi(api_client=api_client)

# Check server status
print(hyperspace_client.cluster_status())

# Create new collection
hyperspace_client = search_master.SearchMasterApi(api_client=api_client)
collection_name = 'collection name'
hyperspace_client.create_collection('config.json', collection_name)
hyperspace_client.cluster_status()

# load data
vecs = np.load('vectors.npy')
metadata_file = open('payloads.jsonl')

# ingest data in batches of 500
BATCH_SIZE = 500

batch = []
for i, (metadata_row, vec) in enumerate(zip(metadata_file, vecs)):
    row = {key: value for key, value in json.loads(metadata_row).items() if key in config["configuration"].keys()}
    row['categories'] = row['categories'].split()
    row['text_embedding'] = np.ndarray.tolist(vec)

    batch.append(VectorDto(str(i), row))

    if i % BATCH_SIZE == 0:
        response = hyperspace_client.add_batch(batch, collection_name)
        batch.clear()
        print(i, response)

hyperspace_client.commit(collection_name)

# select vector to match
input_vector = hyperspace_client.find_vector_by_id(collection_name, 26)
print(input_vector['title'], ",", input_vector['submitter'], ",", input_vector['categories'])

# Set query function
response = hyperspace_client.set_function('/ScoreFunctions/arXivScoreFunc',
                                          collection_name=collection_name,
                                          function_name='similarity_sf')
# Set query logic

query_with_knn = {
    'vector_Content': input_vector,
    'boost': {
        'query': 0.6,  # query score weight
        'vector_field': 1.2  # Vector field score weight
        # there are is no limitation on the amount of vector fields used
    }
}

# run the query
results = hyperspace_client.search_data(query_with_knn,
                                        size=5,  # max number of results
                                        function_name='similarity_sf',  # previously defined score function
                                        collection_name=collection_name)

# iterate over the results and print them
for i, result in enumerate(results['similarity']):
    vector_api_response = hyperspace_client.find_vector_by_id(vector_id=result['vector_id'],
                                                              collection_name=collection_name)
    print(i + 1, ". vector id:", result['vector_id'], ":", vector_api_response['title'], ",",
          vector_api_response['submitter'], ",", vector_api_response['categories'])
    print("\n")
