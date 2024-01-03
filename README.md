About
=================================
This repository is a sandbox for users to experiment with the Hyperspace search engine. The repository includes multiple datasets and corresponding notebooks, desgined for classic, vector and hybrid search.

Introduction
=================================
Hyperspace is a cloud-based hybrid search engine, powered by cloud FPGA hardware. Hyperspace sets new standards in query performance by allowing high-throughput searches with extremely low latency, typically measuring x10-x100 faster than industry benchmarks, and at reduced costs. 
Hyperspace allows vector search, similarity search, or a combination of the two.
The Hyperspace engine query syntax is native Python with supported functionality for candidate generation and scoring for similarity and vector searches. 

Hyperspace Advantages 
=================================
1. Hybrid Search: HyperSearch engine combines vector and similarity search within a single workframe, providing the best of both worlds. 
2. Simplicity and Ease of Use: Hyperspace  native Python syntax allows a seamless and natural migration of existing codebases.
3. Unparalleled Latency: Hyperspace offers x100-x10 lower latency than industry benchmarks, allowing more complex logic in lower latency.
4. Cost Efficiency: By leveraging Hyperspace, users can significantly reduce machine time requirements and associated costs.
5. Advanced AI Possibilities: Hyperspace separates candidate generation from scoring, combined withe the extremely low latency, this allows use of complex AI techniques that are commonly impractical.

Example Datasets
=================================
This repository includes various datasets and notebooks, aimed to demonstrate  the use of Hyperspace Engine. Currently, the following datasets are included:
1. [arXiv Papers Dataset](https://github.com/hyper-space-io/QuickStart/tree/main/DataSets/arXiv) -  The dataset is taken from [kaggle](https://www.kaggle.com/datasets/Cornell-University/arxiv/) and includes a list of academic papers from arXiv, and their metadata, and can be used for vector, classic or hybrid searches. Embedded with all-MiniLM-L6-v2, vec dim = 384.
2. [Crimes In Chicago Dataset](https://github.com/hyper-space-io/QuickStart/tree/main/DataSets/CrimesInChicago) - taken from [kaggle](https://www.kaggle.com/datasets/chicago/chicago-crime/), this dataset includes metadata and can be used to demonstrate classic search.
3. [Stores Dataset](https://github.com/hyper-space-io/QuickStart/tree/b0dbff8733d5fff64e6b4cfe26bb05720ef40073/DataSets/BinaryVector) - Randomly generated vectors of dimension 800, with corresopnding metadata that describes stores. The data can be used for vector, classic or hybrid search.
4. [Movies Dataset](https://github.com/hyper-space-io/QuickStart/tree/main/DataSets/MovieRecommendation) - The data is taken from [MovieLens Latest Datasets](https://grouplens.org/datasets/movielens/latest/). The data includes 45466 documents. 
The data can be used for vector, classic or hybrid search. Embedded with all-MiniLM-L6-v2, vec dim = 384.
5. [AdVec Apps Dataset](https://github.com/hyper-space-io/QuickStart/tree/main/DataSets/AdVec) The data is taken from [AdVec ML](https://demo.advecml.com/). The data includes 89330  documents.
The data can be used for vector, classic or hybrid search. Embedded with bge-small-en model, vec dim = 384.
6. [Amazon Products Matching](https://github.com/hyper-space-io/QuickStart/tree/main/DataSets/ImageAndTextSearch) 100K documents describing amazon products. Each document includes an embedded text and embedded inage vectors. The vectors were embedded using the [Clip ViT-B/32](https://github.com/openai/CLIP), with a dimension of 512.


