object Solution {
    def containsDuplicate(nums: Array[Int]): Boolean = {
        var hset = Set.empty[Int]
        for (i <- nums){
            if (hset.contains(i)) {
                return true
            }
            else {hset = hset + i}
        }
        false
    }
}
