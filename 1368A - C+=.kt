fun main() {
    val t = readln().toInt()

    repeat(t) {
        val (a, b, n) = readln().split(" ").map { it.toLong() }

        var operations = 0
        var larger = maxOf(a, b)
        var smaller = minOf(a, b)

        while (larger <= n) {
            val temp = larger
            larger += smaller
            smaller = temp
            operations++
        }

        println(operations)
    }
}
