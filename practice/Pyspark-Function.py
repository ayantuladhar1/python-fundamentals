from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

if __name__ == "__main__":
    spark = SparkSession.builder \
        .master("local[1]") \
        .appName("BootcampApp") \
        .getOrCreate()
#Select() Function
data = [("James","Smith","USA","CA"),
    ("Michael","Rose","USA","NY"),
    ("Robert","Williams","USA","CA"),
    ("Maria","Jones","USA","FL")
  ]
columns = ["firstname","lastname","country","state"]
df = spark.createDataFrame(data = data, schema = columns)
df.show(truncate=False)
df.select("firstname","lastname").show()
df.select(df.firstname,df.lastname).show()
df.select(df["firstname"],df["lastname"]).show()

#By using col() function
from pyspark.sql.functions import col
df.select(col("firstname"),col("lastname")).show()

#Select All
df.select("*").show()

#Select Single & Multiple Columns From PySpark
df.select("firstname","lastname").show()
df.select(df.firstname,df.lastname).show()
df.select(df["firstname"],df["lastname"]).show()

#By using col() function
from pyspark.sql.functions import col
df.select(col("firstname"),col("lastname")).show()

#Select All
df.select("*").show()