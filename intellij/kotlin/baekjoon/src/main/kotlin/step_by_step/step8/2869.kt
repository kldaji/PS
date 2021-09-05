// TODO: 달팽이는 올라가고 싶다
package step_by_step.step8

fun isWhole(value: Double): Boolean {
    return value - value.toInt() == 0.0
}
// Ref. https://stackoverflow.com/questions/45422290/checking-if-the-output-of-a-calculation-is-a-whole-number

fun main() {
    val (a, b, v) = readLine()!!.toString().split(" ").map { it.toInt() }
    val day = (v - a).toDouble() / (a - b)
    if (isWhole(day)) println((day + 1).toInt())
    else println((day + 2).toInt())
}