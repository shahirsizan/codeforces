fun main() {
    val n = readln().toInt()

    var height = 0
    var cubesRequired = 0
    var level = 1

    while (cubesRequired <= n) {
        cubesRequired += ( level * (level+1) ) / 2
        if (cubesRequired <= n) {
            height++
        }
        level++
    }

    println(height)
}
