## Things to explore:

### 1. Test the track metrics API 

### 2. Test the monitoring API
- Difference between deployment and build
- Build notebook for monitoring models. Would it make sense to do this in prod though?
- Build dashboard with metric monitoring functionality. Can it be done??
- Does it work with PySpark also?

### 3. Test complexity of Lineage Graphs in Atlas
- Can you create more complex lineage graphs (similar to 4)
- How can you retrace back how a model was trained (e.g. which features were used)
- How can you quickly reproduce data that was used for a model for train/val/test
- what if I want to upsample or downsample my data? How can lineage help here
- does it work with pyspark df also? Spark df, Spark sql tables, or Spark SQL views and other assets also?
- does it work with S3 also? Define all dataset types
- do I need to keep a separate hive table for every dataset that I want to put in lineage?
- Will models remain in Atlas even after they are discarded in CML? What happens to Atlas lineage if I redeply the model?

### 4. All things yml file
- What are the entities that can be tracked
- Want to build complex graphs

### 5. Test complexity of Ranger Security features wrt ML entities
- How does Ranger security relate to CML security? Explore synergies
- Can we enforce access to specific columns or rows for data scientists (or data science teams)

### 6. Database Catalog
- What can we show here?
- Can this help with profiling data assets e.g. who worked on this dataset that was used as train/val/test set?
- Can we show who accessed data on datawarehousing side?

### 7. ML Ops in relation to Streaming, OpDB, DEX and CDW
- You can query the same hive managed tables from CDW and CML inlcuding Spark tables

### 8. Real Life scenario: build demo with real life scenario in which you need to roll back models
- roll back model (redeploy vs rebuild)
- launch experiments - can track metrics be used to help this also? E.g. monitor experiments??
- upsample and downsample
- Cost sensitive learning?? 
- Streamline experiments??
- Granular Ranger security - can we prepare secure datasets for data scientists in different groups?
- Topic list: record linkage? ml task requiring lots of changes? 

### 9. How to automate ML project creation
- Learn from Jeff's demos

### 10. Other ideas of questionable sense
- Can you store yaml file in SR? Would that help at all, maybe in streaming ML?
