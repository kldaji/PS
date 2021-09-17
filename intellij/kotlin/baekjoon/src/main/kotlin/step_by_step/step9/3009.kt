// TODO: 네번째 점
package step_by_step.step9

fun main() {
    var resultX = 0
    var resultY = 0
    repeat(3) {
        val (x, y) = readLine()!!.toString().split(" ").map { it.toInt() }
        resultX = resultX xor x
        resultY = resultY xor y
    }
    println("$resultX $resultY")
}