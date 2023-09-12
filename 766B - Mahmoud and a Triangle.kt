fun main() {
    val n = readln().toInt()
    val segments = readln().split(" ").map { it.toLong() }.sorted()

    for (i in 0..n-3) {
        if (segments[i] + segments[i + 1] > segments[i + 2]) {
            println("YES")
            return
        }
    }
    println("NO")
}
