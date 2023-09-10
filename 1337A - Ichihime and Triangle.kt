fun main() {
    val t = readln().toInt()

    repeat(t) {
        val (a, b, c, d) = readln().split(" ").map { it.toInt() }
        // x = b, y = c, and z = c
        // As in order to draw a triangle, the sum of two sides must be greater than the third side
        println("$b $c $c")
    }
}
