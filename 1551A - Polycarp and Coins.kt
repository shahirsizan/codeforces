fun main() {
    val testCases = readln().toInt()

    repeat(testCases) {
        val n = readln().toInt()
        val groupSize = n / 3

        var firstGroupSize = groupSize
        var secondGroupSize = groupSize

        if (n % 3 == 0){
            println("$firstGroupSize $secondGroupSize")
        }
        else if (n % 3 <= 1){
            firstGroupSize++
            println("$firstGroupSize $secondGroupSize")
        }
        else if (n % 3 > 1){
            secondGroupSize++
            println("$firstGroupSize $secondGroupSize")
        }
    }
}
