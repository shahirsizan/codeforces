fun main() {
    val t = readln().toInt()
    repeat(t) {
        val n = readln().toInt()
        val candies = readln().split(" ").map { it.toInt() }
        var oneWeight = 0
        var twoWeight = 0

        for (weight in candies) {
            if (weight == 1) {
                oneWeight++
            } else {
                twoWeight++
            }
        }

        if (oneWeight%2 != 0) { // BEJOR SONGKHOK `1 CANDY` THAKLE EQUALLY DISTRIBUTE
                                // KORA JABE NA. TOTAL WEIGHT ALWAYS ODD HOBE
            println("NO")
        }
        else if((twoWeight%2 != 0 && oneWeight==0)){
                                // ASSUMING EVEN SONGKHOK `1 CANDY` ACHE.
                                // BEJOR SONGKHOK `2 CANDY` AND 0 TA `1 CANDY` THAKLEO
                                // HOBE NA. TAR MANE 2,4,6,8, EROKOM EVEN `1 CANDY` THAKTE HOBE
            println("NO")
        }
        else {                  // ASSUMING JEKONO SONGKHOK `2 CANDY` ACHE AND 2,4,6,8 EROKOM `1 CANDY` ACHE
            println("YES")
        }
    }
}
