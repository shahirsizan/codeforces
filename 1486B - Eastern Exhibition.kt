fun main() {

    fun ans(x: List<Long>): Long {
        val sortedCoordinates = x.sorted()
        return sortedCoordinates[(sortedCoordinates.size/2)]  - sortedCoordinates[(sortedCoordinates.size-1)/2]  + 1
    }

    val t = readln().toInt()
    repeat(t) {
        val n = readln().toInt()
        val xCoordinates = mutableListOf<Long>()
        val yCoordinates = mutableListOf<Long>()

        repeat(n) {
            val (a, b) = readln().split(" ").map{ it.toLong() }
            xCoordinates.add(a)
            yCoordinates.add(b)
        }

        val result: Long = ans(xCoordinates) * ans(yCoordinates)
        println(result)
    }
}
