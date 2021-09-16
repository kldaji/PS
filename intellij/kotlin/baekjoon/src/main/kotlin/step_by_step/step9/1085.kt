// TODO: 직사각형에서 탈출
package step_by_step.step9

fun main() {
    val (x, y, w, h) = readLine()!!.toString().split(" ").map { it.toInt() }
    println(listOf(x - 0, y - 0, w - x, h - y).minByOrNull { it })
}