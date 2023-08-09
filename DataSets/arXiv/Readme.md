#  Academic paper hybrid search with Hyperspace
This notebook demonstrates the use of Hyper Space engine for a hybrid search.

# The Datset
The dataset is taken from [kaggle](https://www.kaggle.com/datasets/Cornell-University/arxiv) and includes a list of academic papers from arXiv, and their metadata.
We will use the combination of an embedded vector data and metadata, to create a hybrid search.

# The Dataset Fields
The metadata includes the following fields:


1. **id** [float] - unique id per paper
2. **title** [string] - paper title
3. **submitter** [string] - name of person who submitted the paper
4. **categories** [list[string]] - list of categories which include the paper
5. **label** [list[string]] - labels aplied to paper
6. **license** [string] - license type
7. **update_date_ts** [integer] - update time in unix format

We build a simple filtering function, which filters papers of the same category, gives bias to paper by same submitter an negative bias for papers without given license. We first select a paper as input for the query
