fun main() {
    val t = readln().toInt()
    repeat(t) {
        val (h, m) = readln().split(' ').map { it.toInt() }
        val minutesBeforeNewYear = (23 - h) * 60 + (60 - m)
        println(minutesBeforeNewYear)
    }
}
