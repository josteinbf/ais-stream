import dk.tbsalling.aismessages.AISInputStreamReader

object Main {

  def main(args: Array[String]): Unit = {

    val stream = new AISInputStreamReader(
      System.in,
      msg => println(msg),
    )
    stream.run
  }
}