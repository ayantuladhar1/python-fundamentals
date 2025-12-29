from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

#Car Project

if __name__ == "__main__":
    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("BootcampApp") \
        .getOrCreate()

data = [("Ford Torino", 140, 3449, "US"),
        ("Chevrolet Monte Carlo", 150, 3761, "US"),
         ("BMW 2002", 113, 2234, "Europe")]

schema =  StructType([ \
    StructField("carr",StringType(),True), \
    StructField("horsepower",IntegerType(),True), \
    StructField("weight",IntegerType(),True), \
    StructField("origin", StringType(), True), \
  ])

df = spark.createDataFrame(data=data,schema=schema)

df1=(df.withColumn("AvgWeight", lit(200))
.withColumn("kilowatt_power", col("horsepower") * 1000)
.withColumnRenamed("carr","car"))

df1.show(truncate=False)
