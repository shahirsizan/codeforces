import kotlin.math.sqrt

fun isPrime(num: Int): Boolean {
    if (num <= 1) return false

    for (i in 2..sqrt(num.toDouble()).toInt()) {
        if (num % i == 0) {
            return false
        }
    }
    return true
}

fun main() {
    val (n,m) = readln().split(" ").map{it.toInt()}
    var nextPrime = n+1
    while (!isPrime(nextPrime)) {
        nextPrime++
    }

    if (nextPrime == m) {
        println("YES")
    } else {
        println("NO")
    }
}
