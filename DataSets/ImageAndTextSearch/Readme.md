# Amazon Products Similarity Search Using Hyperspace

This notebook demonstrates the use of Hyperspace engine to create a multi vector search. 

For more info, see the [Hyperspace documentation](https://docs.hyper-space.io/hyperspace-docs/getting-started/overview).
# The Dataset
The datase includes 100,000 document, describing amazon products. The dataset documents include the following fields:


*   **id** [float] - unique identifier per product
*   **amznid** [keyword] - unique identifier by Amazon, per product
*   **title** [keyword] - the product title
*   **img_link** [keyword] - url to the product image
*   **img_clip** list[[float]] - embedding of the product image
*   **txt_clip** list[[float]] - embedding of the product description

The embedded vectors are of dimension 512.

The data can be downloaded from the following links: [text embedding](http://hyperspace-datasets.s3.amazonaws.com/text_clip_emb.npy), [image embedding](http://hyperspace-datasets.s3.amazonaws.com/img_clip_emb.npy), [Product Images](https://github.com/hyper-space-io/QuickStart/blob/main/DataSets/ImageAndTextSearch/product_images.parquet).
This notebook was built in collabortation with [Argmax.io](https://www.linkedin.com/company/argmax/?originalSubdomain=il).
