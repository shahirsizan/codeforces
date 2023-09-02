fun main() {
    val testCases = readln().toInt()

    repeat(testCases) {
        val votes = readln().split(" ").map { it.toInt() }
        val additionalVotesNeeded = IntArray(3)

        for (i in 0 until 3) {
            val currentCandidateVotes = votes[i]
            val otherCandidatesMaxVotes = maxOf(votes[(i+1) % 3], votes[(i+2) % 3])

            if (currentCandidateVotes > otherCandidatesMaxVotes) {
                additionalVotesNeeded[i] = 0
            } else {
                additionalVotesNeeded[i] = otherCandidatesMaxVotes - currentCandidateVotes + 1
            }
        }

        println(additionalVotesNeeded.joinToString(" "))
    }
}
