fun main() {
    val n = readln().toInt()
    val a = readln().split(" ").map { it.toLong() }
    val b = readln().split(" ").map { it.toLong() }

    val diffs = MutableList(n) { i -> a[i] - b[i] }
    diffs.sort()

    var count = 0L
    var i = 0
    var j = n - 1

    while (i < j) {
        if (diffs[i] + diffs[j] > 0) {
            count += j-i
            j--
        } else {
            i++
        }
    }

    println(count)
}
