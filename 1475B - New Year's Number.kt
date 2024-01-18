fun main() {
    repeat(readln().toInt()) {
        val n = readln().toInt()
        val k2020 = n % 2020
        val k2021 = (n - k2020) / 2020
        if (k2020 <= k2021) {
            println("YES")
        } else {
            println("NO")
        }
    }
}
