fun main() {
    val t = readln().toInt()

    repeat(t) {
        val n = readln().toInt()
        val a = readln().split(" ").map { it.toInt() }
        var sett = a.toSet()
        val lengthh = sett.size

        println(lengthh)
    }
}
