
import json
from pprint import pprint
import inspect
from urllib.request import urlretrieve
import os
import zipfile


def print_results( results, collection_name ) :

    print("query run time   :", results["took_ms"], " ms")
    print("hits (candidates):", results["candidates"])

    # print(results.keys())
    for i, result in enumerate(results['similarity']):
        # vector_api_response = hyperspace_client.get_document(document_id=result['document_id'], collection_name=collection_name)
        print("%2d id %-10s score = %8.3f" % (i + 1, result['document_id'], result["score"]))
    print("="*33)
    if 'aggregations' in results :
        print("Aggregations :")
        pprint(results['aggregations'])
        
def set_score_function(hyperspace_client, func, collection_name, score_function_name='func'):
    source = inspect.getsource(func)
    with open('sf.py', 'w') as f:
        f.write(source)
    hyperspace_client.set_function('sf.py', collection_name, score_function_name)
    print('set_score_function : OK') # if I'm here, I'm OK

def download_data(url, file_name):
    """
    url (str): URL of the file to download.
    file_name (str): Local path where the file will be saved.
    """
    # Check if the file already exists and is not empty
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        print(f"The file {file_name} already exists and is not empty.")
    else:
        try:
            # Attempt to download the file from `url` and save it locally under `file_name`
            urlretrieve(url, file_name)
            # Check if the file was downloaded and is not empty
            if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
                print(f"Successfully downloaded {file_name}")
            else:
                print("Download failed or file is empty.")
                
        except Exception as e:
            print(f"An error occurred: {e}")

def unzip_file(path_to_zip_file):
    directory_to_extract_to = './'
    try:
        with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
            zip_ref.extractall(directory_to_extract_to)
        print(f'Success! Files have been extracted to {directory_to_extract_to}')

    except zipfile.BadZipFile:  # Handle a bad zip file
        print("Error: The file is a bad zip file. Unable to unzip.")
    except FileNotFoundError:  # Handle the file not being found
        print("Error: The file was not found. Please check the path.")
    except Exception as e:  # Handle other exceptions
        print(f"An error occurred: {e}")
        
        
        
def batch_ingest_data(hyperspace_client, dataset_path, max_doc_count, config, collection_name) :
    # global hyperspace_client
    with open(dataset_path) as metadata:
        BATCH_SIZE = 500

        batch = []
        for i, metadata_row in enumerate(metadata):
            row = {key: value for key, value in json.loads(metadata_row).items() if key in config["configuration"].keys()}
            row["ID"] = str(i)
            batch.append(dict(row))

            if i % BATCH_SIZE == 0:
                response = hyperspace_client.add_batch(batch, collection_name)
                batch.clear()
                print(i, response)
            
            if max_doc_count != 0 and i+1 == max_doc_count  :
                break
        if batch:
            response = hyperspace_client.add_batch(batch, collection_name)
            batch.clear()
            print(i, response)



print("here")
