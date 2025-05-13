# ----------------------------------------firstapp.py---------------------------------------
import pyspark


def helloworld_pyspark():
    sc = pyspark.SparkContext("local[*]")

    txt = sc.textFile(
        "file://///Users/kishored/coding/python-coding/spark-trailers/samples_pyspark/copyright.txt"
    )
    print(txt.count())

    python_lines = txt.filter(lambda line: "python" in line.lower())
    print(python_lines.count())


"""
The entry-point of any PySpark program is a SparkContext object. This object allows you to connect to a Spark cluster and create RDDs. 
The local[*] string is a special string denoting that you’re using a local cluster, which is another way of saying you’re running in single-machine mode. 
The * tells Spark to create as many worker threads as logical cores on your machine.
"""
# ----------------------------------------firstapp.py---------------------------------------
"""
# Creating a SparkContext can be more involved when you’re using a cluster. 
# To connect to a Spark cluster, you might need to handle authentication and a few other pieces of information specific to your cluster

conf = pyspark.SparkConf()
conf.setMaster('spark://head_node:56887')
conf.set('spark.authenticate', True)
conf.set('spark.authenticate.secret', 'secret-key')
sc = SparkContext(conf=conf)

"""


def create_rdd():
    """The following code creates an iterator of 10,000 elements and then uses parallelize() to distribute that data into 2 partitions:"""
    big_list = range(10000)
    sc = pyspark.SparkContext("local[*]")
    rdd = sc.parallelize(big_list, 2)
    odds = rdd.filter(
        lambda x: x % 2 != 0
    )  # By using the RDD filter() method, that operation occurs in a distributed manner across several CPUs or computers
    print(odds.take(5))


if __name__ == "__main__":
    # helloworld_pyspark()
    create_rdd()
