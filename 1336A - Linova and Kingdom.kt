import java.io.*
import java.util.*

// Definition of a TreeNode to store information about each node
data class TreeNode(
    var parent: Int = 0, var depthToRoot: Int = 0, var numChilds: Int = 0
)

// Main function
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    // Reading the number of total nodes and the number of industry cities
    val (totalNodes, industryCities) = readLine().trim().split(" ").map { it.toInt() }

    // Creating an adjacency list for the graph using LinkedLists
    val adjacencyList = Array(totalNodes + 1) { LinkedList<Int>() }

    // Creating an array to store information about each node
    val nodeInfo = Array(totalNodes + 1) { TreeNode() }

    // Reading the connections between cities and populating the adjacency list
    repeat(totalNodes - 1) {
        val (cityA, cityB) = readLine().trim().split(" ").map { it.toInt() }
        adjacencyList[cityA].add(cityB)
        adjacencyList[cityB].add(cityA)
    }

    // Depth-first search function to calculate the depth and parent of each node
    fun dfs(currentNode: Int, depth: Int, parent: Int) {
        nodeInfo[currentNode].run {
            this.depthToRoot = depth
            this.parent = parent
        }
        for (adjNode in adjacencyList[currentNode]) {
            if (adjNode != parent) {
                dfs(adjNode, depth + 1, currentNode)
            }
        }
    }

    // Another depth-first search function to calculate the number of child nodes for each node
    fun dfs2(currentNode: Int, parent: Int): Int {
        for (adjNode in adjacencyList[currentNode]) {
            if (adjNode != parent) {
                nodeInfo[currentNode].numChilds += dfs2(adjNode, currentNode)
            }
        }
        return nodeInfo[currentNode].numChilds + 1
    }

    // Using BufferedWriter to print the output
    BufferedWriter(OutputStreamWriter(System.out)).use { writer ->
        // Performing the two depth-first searches
        dfs(1, 0, 0)
        dfs2(1, 0)

        var happinessSum = 0L

        // Calculating the happiness sum for envoys based on the difference between depth and number of child nodes
        val happinessValues = IntArray(totalNodes) {
            nodeInfo[it + 1].depthToRoot - nodeInfo[it + 1].numChilds
        }.sortedArrayDescending()

        // Calculating the maximum happiness sum for envoys by selecting top industryCities values
        repeat(industryCities) {
            happinessSum += happinessValues[it]
        }

        // Writing the result to the output
        writer.write("$happinessSum")
        writer.flush()
    }
}
