import java.io.PrintWriter
val out: PrintWriter = PrintWriter(System.out)

fun main() {
    val t = readln().toInt()
    repeat(t) {
        val (numOfWeapons, enemyHealth) = readln().split(" ").map { it.toInt() }
        val weaponDamageList = readln().split(" ").map { it.toInt() }.sorted()

        val largestDamage = weaponDamageList[numOfWeapons - 1]
        val secondLargestDamage = weaponDamageList[numOfWeapons - 2]

        out.println(when {
            enemyHealth <= largestDamage -> 1
            enemyHealth <= largestDamage+secondLargestDamage -> 2
            enemyHealth % (largestDamage+secondLargestDamage) == 0 -> (enemyHealth / (largestDamage+secondLargestDamage)) * 2
            enemyHealth % (largestDamage+secondLargestDamage) <= largestDamage -> (enemyHealth / (largestDamage+secondLargestDamage)) * 2 + 1
            else -> (enemyHealth / (largestDamage+secondLargestDamage)) * 2 + 2
            // `else` = (enemyHealth % (largestDamage+secondLargestDamage)) > largestDamage
        })

    }
    out.flush()
}

// JAVA ER EISHOB NA LIKHLE TIME EXCEEDE ERROR ASHBE. 
