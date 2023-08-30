fun main() {

    val t = readln().toInt()
    repeat(t) {

        val inputString = readln()
        var smallestChar = Char.MAX_VALUE

        for (ch in inputString) {
            smallestChar = minOf(smallestChar, ch)
        }

        val a = StringBuilder()
        val b = StringBuilder()
        var flag = false

        for (ch in inputString) {
            if (ch == smallestChar && !flag) {
                a.append(ch)
                flag = true
            } else {
                b.append(ch)
            }
        }

        println("$a $b")
    }
}
