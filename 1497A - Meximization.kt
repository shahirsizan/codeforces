fun main() {
    val t = readln().toInt()
    repeat(t) {
        val size = readln().toInt()
        val nums = readln().split(' ').map { it.toInt() }.sorted()

        val first = mutableSetOf<Int>()
        var end = ""

        for (i in 0 until size) {
            if (first.contains(nums[i])) {
                end += " ${nums[i]}"
            } else {
                first.add(nums[i])
            }
        }
        // THIS LOOP WILL FIRST CREATE A `SET` CONTAINING ALL THE UNIQUE ELEMENTS OF `NUMS`.
        // THEN IT WILL CREATE A `STRING` CONTAINING THE DUPLICATE ELEMENTS OF `NUMS`

        val result = first.joinToString(" ") + end
        // THIS WILL APPEND THE `STRING` TO THE `SET` RESULTING `SET+STRING`

        println(result)
    }
}
