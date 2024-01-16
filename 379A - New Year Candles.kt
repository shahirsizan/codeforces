fun main() {
    var (a, b) = readln().split(" ").map { it.toInt() }
    var hours = a

    while (a >= b) {
        var newCandles = a / b
        hours += newCandles
        a = newCandles + a % b
    }

    println(hours)
}
