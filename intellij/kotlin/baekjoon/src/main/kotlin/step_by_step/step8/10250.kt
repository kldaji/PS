// TODO: ACM 호텔
package step_by_step.step8

fun findRoom(h: Int, w: Int, n: Int): Int {
    return if (n % h == 0) {
        h * 100 + n / h
    } else {
        n % h * 100 + n / h + 1
    }
}

fun main() {
    repeat(readLine()!!.toInt()) {
        val (h, w, n) = readLine()!!.toString().split(" ").map { it.toInt() }
        println(findRoom(h, w, n))
    }
}