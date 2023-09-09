fun main() {
    val t = readln().toInt()
    repeat(t) {
        val n = readln().toInt()
        val a = readln().split(" ").map { it.toInt() }.toMutableList()
        val b = readln().split(" ").map { it.toInt() }.toMutableList()

        // Swap elements in 'a' and 'b' if 'a[i]' is less than 'b[i]'
        for (i in 0..n-1) {
            if (a[i] < b[i]) {
                val temp = a[i]
                a[i] = b[i]
                b[i] = temp
            }
        }
        val maxA = a.maxOrNull()!!
        val maxB = b.maxOrNull()!!
        val result = maxA*maxB
        println(result)
    }
}
