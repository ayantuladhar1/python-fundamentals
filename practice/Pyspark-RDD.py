from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("BootcampApp") \
        .getOrCreate()

    rdd = spark.sparkContext.textFile("file:///home/takeo/test.txt")
    rdd2 = rdd.flatMap(lambda x: x.split(" ")) # using lambda every record are split by space
    rdd3 = rdd2.map(lambda x: (x, 1)) # adding key for records stored in x
    rdd4 = rdd3.filter(lambda x: 'wo' in x[0]) #filter using keywords
    rdd5 = rdd3.reduceByKey(lambda a, b: a + b) #reduceByKey
    rdd6 = rdd5.map(lambda x: (x[1], x[0])).sortByKey() #SortKey
    #To save the file
    #rdd6.saveAsTextFile("file:///home/takeo/wordCount1")


    print("From Print all from test.txt", rdd.collect()) #To Print text.txt
    print("From FlatMap", rdd2.collect()) #Print FlatMap
    print("From Map", rdd3.collect()) #Print Map
    print("From reduceByKey", rdd5.collect())
    print("From sortByKey",rdd6.collect())
    print("From Count", rdd6.count()) #To count elements in rdd6