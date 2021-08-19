// TODO: 최소, 최대
package step_by_step.step5

fun main() {
    val n = readLine()!!.toInt()
    val list = readLine()!!.split(" ").map { it.toInt() }
    println("${list.minOrNull()} ${list.maxOrNull()}")
}