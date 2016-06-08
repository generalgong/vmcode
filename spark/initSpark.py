from pyspark import SparkConf , SparkContext
#conf = SparkConf().setMaster("local").setAppName("My app")
#sc = sparkContext(conf = conf)
sc =SparkContext("local","WordCount")
lines = sc.parallelize(["pandas", "i like pandas"])
inputRdd = sc.textFile("/input/README.md")
print(inputRdd.first())
hadoopRdd = inputRdd.filter(lambda x: "Hadoop" in x)
sparkRdd = inputRdd.filter(lambda x: "spark" in x)
print("errorRdd has been created and the first Line is %s" % hadoopRdd.first())
hadoopSparkRdd = hadoopRdd.union(sparkRdd)
print("hadoopSparkRdd count %s " % hadoopSparkRdd.collect())

words = inputRdd.flatMap(lambda x: x.split(" "))
wordsCount = words.map(lambda x: (x , 1)).reduceByKey(lambda x,y:x +y)

print("words Count: %s " % wordsCount)

print("*********")

