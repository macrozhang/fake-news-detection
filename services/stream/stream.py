import sys
import os
import time
import uuid
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from catboost import CatBoostClassifier

from utils import preprocessor
from utils.db_utils import CassandraDb

from settings import DB_CONNECTION

"""
This is use for create streaming of text from txt files that creating dynamically 
from files.py code. This spark streaming will execute in each 1 seconds and It'll
show number of words count from each files dynamically
"""

print("DB is warming up...")
time.sleep(10)
db = CassandraDb([DB_CONNECTION], "9042")

keyspaceName = "fakenews"
tableName = "dataset"

db.create_keyspace(keyspaceName)
db.create_table(keyspaceName, tableName, {"id" : "uuid PRIMARY KEY","title": "text", "category" : "text", "prediction": "text"})

def readMyStream(rdd, spark):
  if not rdd.isEmpty():
    df = spark.read.json(rdd)

    print('Started the Process')
    print('Selection of Columns')

    df = df.select('id','news_url','title','tweet_ids', 'Y', 'category' )
    df.show()

    cleaned_df = preprocessor.clean_df(df)
    cleaned_df.head()

    clm = CatBoostClassifier()
    clm.load_model("models/weights/catboost", format='cbm')

    predictions = clm.predict(data=cleaned_df)

    cleaned_df['Y'] = predictions
    print(f"predictions : {predictions}")

    predicted_data = []
    for index, row in cleaned_df.iterrows():
        # print(row['c1'], row['c2'])
        predicted_data.append({
			"id" : uuid.uuid4(),
			"title": row['clean_title'], 
			"category": row['category'],
			"prediction": row['Y']})

    db.insert_batch_data(predicted_data, keyspaceName, tableName)





def main():
    sc = SparkContext(appName="PysparkStreaming")
    spark = SparkSession(sc)

    ssc = StreamingContext(sc, 1)   # Streaming will execute in each 1 seconds
    lines = ssc.textFileStream("/opt/application/NAS")

    lines.foreachRDD(lambda rdd: readMyStream(rdd, spark))

    ssc.start()
    print("Data streaming has just started...")

    ssc.awaitTermination()
    print("Data streaming has just ended:)")



if __name__ == "__main__":
    main()