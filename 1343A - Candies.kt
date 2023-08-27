fun main() {
    val t = readln().toInt()

    repeat(t) {
        val n = readln().toInt()
        var k = 3

        while (n % k != 0) {
            k += k + 1
        }

        val x = n / k
        println(x)
    }
}
