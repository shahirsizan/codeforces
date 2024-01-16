fun main() {
    repeat(readln().toInt()) {
        val n = readln().toLong()
        var count = 0
        for (i in 1..9){
            var x : Long = i.toLong()
            var charX = i.toString()
            while(x <= n){
                count++
                var xString = x.toString()
                xString = xString + charX
                x = xString.toLong()
            }
        }
        println(count)
    }
}
