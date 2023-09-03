fun main() {
    val (n, m, k) = readln().split(" ").map { it.toInt() }

    if (m >= n && k >= n) {
        println("Yes")
    } else {
        println("No")
    }
}
