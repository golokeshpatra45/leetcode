import scala.collection.mutable.{HashMap, ArrayBuffer}

object Solution {
    def groupAnagrams(strs: Array[String]): List[List[String]] = {
        var mapped = HashMap.empty[String,ArrayBuffer[String]]
        def sortString(s:Array[String])={
            // println(s)
            for (i <- s) {
                var reversedStr = i.toCharArray().sorted.mkString("")
                // println(reversedStr)
                if (mapped.contains(reversedStr)) {
                    mapped(reversedStr)+=i
                }
                else {
                    mapped(reversedStr)= ArrayBuffer(i)
                    }
            }
        }
        sortString(strs)
        // print(mapped)
        print(mapped.values.toList.map(_.toList))
        return mapped.values.toList.map(_.toList)
    }
}
