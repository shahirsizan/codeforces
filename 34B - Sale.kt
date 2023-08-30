fun main() {
    val (n, m) = readln().split(" ").map { it.toInt() }
    val prices = readln().split(" ").map { it.toInt() }.sorted()

    var moneyEarned = 0

    for (i in 0 until m) {
        if (prices[i] < 0) {
            moneyEarned += -prices[i]
        }
    }

    println(moneyEarned)
}
