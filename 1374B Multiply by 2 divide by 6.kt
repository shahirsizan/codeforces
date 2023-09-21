fun main() {
    val t = readln().toInt()
    repeat(t) {
        var n = readln().toInt()
        var moves = 0

        while (n > 1) {
            if (n % 6 == 0) {
                n /= 6
            } else {
                n *= 2
            }
            moves++
        }

        println(if (n == 1) moves else -1)
    }
}
