# Fake news detection in online portals (FaNeD)
## Description:  
The data for this project will be collected as part of the project by utilizing open-source web-crawling engines + the BeuatifulSoup library for pulling out the textual content from the collected news entries. At least two different and well-known news portals will be analyzed. Texts analyzed will be in English and/or Hungarian. There will be a sentiment analysis and fake news processing stage(s). The collected news entries will be stored in Cassandra. 
+ Team size: 5
+ Mentored by: Tsegaye, Imre
+ Open-source technologies to be used: 
    - Cassandra
    - Spark (for batch analytics)
    - Flink (in real-time stream mining)
    - Docker
+ Batch processing:
    - Batch 1: Train/utilize a model for sentiment analytics.
    - Batch 2: Train a model for fake news detection.
+ Stream mining pipelines:
    - Pipeline 1: Develop a stream source and light-weight analytics for news portal A.
    - Pipeline 2: Develop a stream source and light-weight analytics for news portal B.
    - Pipeline 3: Develop a stream processing stage for sentiment analysis of incoming news streams.
    - Pipeline 4: Develop a stream processing stage for fake news detection which will be capable to flag potentially fake or low-quality news entries.
