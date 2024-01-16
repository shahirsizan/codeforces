import kotlin.math.ceil

fun calculateFloorNumber(apartmentNumber: Int, apartmentsPerFloor: Int): Int {
    if (apartmentNumber <= 2) {
        return 1
    } else {
        val apartmentsAboveFirstFloor = apartmentNumber - 2
        val floorNumber = ceil(apartmentsAboveFirstFloor.toDouble() / apartmentsPerFloor.toDouble()).toInt() + 1
        return floorNumber
    }
}
fun main() {
    val testCases = readln().toInt()
    repeat(testCases) {
        val (apartmentNumber, apartmentsPerFloor) = readln().split(" ").map { it.toInt() }
        val floorNumber = calculateFloorNumber(apartmentNumber, apartmentsPerFloor)
        println(floorNumber)
    }
}

