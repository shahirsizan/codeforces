fun main() {
    val (n, k) = readln().split(" ").map { it.toInt() }
    val both = mutableListOf<Int>()
    val alice = mutableListOf<Int>()
    val bob = mutableListOf<Int>()

    repeat(n) {
        val a = readln().split(" ").map { it.toInt() }
        if (a[1] == 1 && a[2] == 1) {
            both.add(a[0])
        } else if (a[1] == 1) {
            alice.add(a[0])
        } else if (a[2] == 1) {
            bob.add(a[0])
        }
    }

    both.sort()
    alice.sort()
    bob.sort()

    val q = minOf(alice.size, bob.size)

    for (i in 0 until q) {
        both.add(alice[i] + bob[i])
    }

    both.sort()
    var min_time_required = 0
    var i = 0

    if (k > both.size) {
        println(-1)
    } else {
        while (i < k) {
            min_time_required += both[i]
            i++
        }
        println(min_time_required)
    }
}
