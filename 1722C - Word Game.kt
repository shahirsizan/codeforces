fun main() {
    val t = readln().toInt()
    repeat(t) {
        val n = readln().toInt()
        val words = List(3) { readln().split(" ").toSet() }
        solve(words).joinToString(" ").also { println(it) }
    }
}

fun solve(wordSets: List<Set<String>>): List<Int> {
    val points = MutableList(3) { 0 }
    val allWords = wordSets[0].union(wordSets[1].union(wordSets[2]))
    for (word in allWords) {
        val indices_of_people_that_wrote_the_word: List<Int> = (0 until 3).filter { index -> word in wordSets[index] }
        when (indices_of_people_that_wrote_the_word.size) {
            1 -> 3
            2 -> 1
            else -> 0
        }.let { pt -> indices_of_people_that_wrote_the_word.forEach { i -> points[i] += pt } }
    }
    return points
}
