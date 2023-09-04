fun main() {
    val t = readln().toInt()
    repeat(t) {
        val initialBalance = readln().toInt()
        var totalSpent = 0
        var currentBalance = initialBalance
        while (currentBalance >= 10) {
            val spent = currentBalance / 10 * 10
            totalSpent += spent
            val cashback = spent / 10
            currentBalance = currentBalance - spent + cashback
        }
        totalSpent += currentBalance
        println(totalSpent)
    }
}
