fun main() {
    val (a, b, s) = readln().split(" ").map { it.toLong() }
    val totalSteps = Math.abs(a) + Math.abs(b)

    //  `s` and `totalSteps` are of type Long, and the constant `0` is of type Int.
    //  Since Kotlin does not allow direct comparison between Long and Int
    //  without explicit casting, you'll encountered error if you just write `0`
    //  instead of `0L`

    if (s < totalSteps || (s - totalSteps) % 2 != 0L) {
        println("No")
    } else {
        println("Yes")
    }
}
