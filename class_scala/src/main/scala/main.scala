// scala v2.13.6
import scala.collection.mutable.ArrayBuffer
import scala.util.control.BreakControl
import scala.util.control.Breaks._

import scala.io.StdIn.readLine

class Naturales(var n: Int=2){
  var arr = ArrayBuffer.range(0, 102)  
  
  def extract:Unit={
    if(n <= 100){
      arr.remove(n)
     println(s"2nd step: int $n removed") 
    }
    else{
      println("Not in the range [0, 100]")
    }
  }
  def calc:Unit={
    var aux = -1
    for(a <- arr){
      if(a-1 != aux){
        println(s"3rd step: The missing number is: $n ")
        break()
      }
      else{
        aux += 1
      }
    }
  }

}

println("1st step: input a natural number from 0 to 100")
var n = readLine()
val nat = new Naturales(9)
println(nat.n)  // prints n
nat.extract // prints n
println(nat.calc)  // prints n
