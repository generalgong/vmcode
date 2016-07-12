import org.apache.spark.SparkContext._
import org.apache.spark.{SparkConf, SparkContext}

object gongPR{

  def showWarning() {
    System.err.println(
      """WARN: This is a naive implementation of PageRank and is given as an example!
        |Please use the PageRank implementation found in org.apache.spark.graphx.lib.PageRank
        |for more conventional use.
      """.stripMargin)
  }

  def main(args: Array[String]) {
    if (args.length < 1) {
      System.err.println("Usage: SparkPageRank <file> <iter>")
      System.exit(1)
    }
    showWarning()

    val sparkConf = new SparkConf().setAppName("gongPageRank").setMaster("local[2]")
    val iters = if (args.length > 1) args(1).toInt else 10
    val ctx = new SparkContext(sparkConf)
    val lines = ctx.textFile(args(0), 1)

    val links = lines.map{ s =>
      val parts = s.split("\\s+")
      (parts.head, parts.tail)
    }.sortBy(_._1).cache()
    //Array((B,CompactBuffer(D)), (D,CompactBuffer(B)), (A,CompactBuffer(B)), (C,CompactBuffer(A)))
    val pageSize = lines.count()
    var ranks = links.mapValues(v => 1.0 /pageSize).sortBy(_._1)
    //Array((B,1.0), (D,1.0), (A,1.0), (C,1.0))

    for (i <- 1 to iters) {
      val contribs = links.join(ranks).values.flatMap{ case (urls, rank) =>
        val size = urls.size
        urls.map(url => (url, rank / size))
      }
      //Array[(String, Double)] = Array((D,1.0), (B,1.0), (B,1.0), (A,1.0))
      ranks = contribs.reduceByKey(_ + _).mapValues(0.15 + 0.85 * _)
    }

    val output = ranks.collect()
    //Array[(String, Double)] = Array((B,1.8499999999999999), (D,1.0), (A,1.0))
    output.foreach(tup => println(tup._1 + "gong: has rank: " + tup._2 + "."))

    ctx.stop()
  }
}
