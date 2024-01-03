#  Binary vector and metadata search with Hyperspace
This notebook demonstrates the use of Hyperspace engine for a hybrid search, which combines vector search of binary vectors and metadata filtering over their corresponding metadata.

# The Dataset
The dataset is randomly generated to include binary vectorS of dimension 800 and corresponding metadata.

## The Dataset Fields
The metadata includes the following fields:
1. **country** [string] - The Country in which the store is located
2. **city** [string] - The city in which the store is located
3. **street** [keyword] - The street in which the store is located
4. **zip_code** [integer] - The store zipcode
5. **open_now** [boolean] - Is the store open
6. **vertical** [keyword] - The store vertical (industry)
