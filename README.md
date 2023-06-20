About
=================================
This repository provides a sandbox that allows users to experiment with the HyperSpace engine. This code can be modified to run with any NoSQL or vector data, but in its current form it is designed to run over one the qdrant benchmark datasets,  https://github.com/qdrant/ann-filtering-benchmark-datasets#data 

Introduction
=================================
HyperSpace is a cloud-based hybrid search engine, powered by cloud FPGA hardware. HyperSpace sets new standards in query performance by allowing high-throughput searches with extremely low latency, typically measuring x10-x100 faster than industry benchmarks, and at reduced costs. 
HyperSpace allows vector search, noSQL database, or a combination of the two.
The HyperSpace engine query syntax is native Python with supported functionality for candidate generation and scoring for similarity and vector searches. 

Advantages of Using HyperSpace
=================================
1. Hybrid Search: HyperSearch engine allows combination of vector and noSQL databases, providing the best of both worlds. 
2. Simplicity and Ease of Use: HyperSpace adopts native Python syntax, facilitating a seamless transition and natural migration of existing codebases.
3. Comprehensive Search Capabilities: HyperSpace incorporates similarity search, vector search, dense searches, and hybrid searches within a single user interface.
4. Unparalleled Latency: HyperSpace offers x100-x10 lower latency when compared to industry benchmarks, allowing more complex logic in lower latency frames.
5. Cost Efficiency: By leveraging HyperSpace, users can significantly reduce machine time requirements and associated costs.
6. Advanced AI Possibilities: HyperSpace creates clear distinction between candidate generation and scoring. This, coupled with the engine's exceptionally low latency, creates a  potential for employing complex AI techniques that were previously impractical.

Workflow - initial setup
=================================
1. Install and set local environment
2. Update/Create Hyper config file
3. Create collection - on existing db - (see managing collection)
4. Ingest Data = Data Upload (not currently in correct order)
5. Defining and running queries

Workflow - Running Queries
=================================
1. Create query function (relevant only to similarity)
2. Create query object
3. Submit
4. Access Results
