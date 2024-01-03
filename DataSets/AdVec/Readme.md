# Application Search Using Hyperspace

This notebook demonstrates the use of Hyperspace engine to create a hybrid search in an App database. 
For more info, see the [Hyperspace documentation](https://docs.hyper-space.io/hyperspace-docs/getting-started/overview).
# The Dataset
The dataset includes 89330 documents with the following fields:
1. **id** [float] - unique identifier per application
2. **title** [Keyword] - Application name
3. **bundle_id** [keyword] - identifier of the App bundle, if such exists
4. **ios** [boolean] - Is the App an IOS App (True) or Android (False) 
5. **categories** [list[keyword]] - list of categories to which the App belongs
6. **content** [Keyword] - app description as text
7. **embedded_app** [list[float]] - text embedding of the app description. Text was embedded using the  Hugging face [bge-small-en model](https://huggingface.co/BAAI/bge-small-en)

The data was taken from [AdVec ML](https://demo.advecml.com/). The search engine was built in collabortation with [Argmax.io](https://www.linkedin.com/company/argmax/?originalSubdomain=il).
The data can be downloaded from the following links: [vectors](http://hyperspace-datasets.s3.amazonaws.com/context.jsonl)
