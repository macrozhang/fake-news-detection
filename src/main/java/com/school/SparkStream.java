package com.school;

import org.apache.commons.io.FileUtils;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.ml.feature.Word2Vec;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.RowFactory;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.types.*;
import org.apache.spark.streaming.Durations;
import org.apache.spark.streaming.api.java.JavaStreamingContext;

import java.io.File;
import java.util.*;

public class SparkStream {

	public static void main(String[] args) throws Exception {
		// Initialize the spark
		SparkSession spark = SparkSession
				.builder()
				.appName("Analysis")
				.master("local[2]")
				.getOrCreate();

		JavaStreamingContext jssc = new JavaStreamingContext(new JavaSparkContext(spark.sparkContext()), Durations.seconds(3));
		jssc.checkpoint(FileUtils.getTempDirectoryPath());

		
		
		// rddQueue.add(rdd);

		// Read all lines of the CSV file - 读取CSV文件所有行
		List<String> lines = FileUtils.readLines(new File("D:/AllCode/GitHub/FaNed/FaNed/fake-news-detection/data/combined_shuffled_data.csv"));

		// Train the Word2Vec model: title conversion to vector - 训练Word2Vec模型：标题转向量
		List<Row> data = new ArrayList<>();
		for (int i=1; i<lines.size();i++) { //第一行去掉是表头
			String ss[] = lines.get(i).split(",");
			int flag = 0;
			if (ss[5].equalsIgnoreCase("real")) {
				flag = 1;
			}
			data.add(RowFactory.create(Arrays.asList(ss[3].split(" ")),flag));
		}
		StructType schema = new StructType(new StructField[]{
				new StructField("text", new ArrayType(DataTypes.StringType, true), false, Metadata.empty()),
				new StructField("flag", DataTypes.IntegerType, false, Metadata.empty())
		});

		// Training decision tree model: vector + flag - 训练决策树模型：向量+flag
	
	}
}

