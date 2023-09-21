import kotlin.math.sqrt

fun main() {
    repeat(readln().toInt()) {
        val (n, k) = readln().split(" ").map { it.toInt() }
        val sqrtN = sqrt(n.toDouble()).toInt()

        var ans = n
        for (i in 1..sqrtN) {
            if (n % i == 0) {
                val j = n / i
                if (i <= k) ans = minOf(ans, j)
                if (j <= k) ans = minOf(ans, i)
            }
        }

        println(ans)
    }
}
