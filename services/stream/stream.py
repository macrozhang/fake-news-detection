import sys
import os
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession

from utils import preprocessor

"""
This is use for create streaming of text from txt files that creating dynamically 
from files.py code. This spark streaming will execute in each 1 seconds and It'll
show number of words count from each files dynamically
"""

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

    predictions = clf.predict(data=cleaned_df)

    cleaned_df['Y'] = predictions




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