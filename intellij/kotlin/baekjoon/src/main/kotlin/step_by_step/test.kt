package step_by_step

import kotlin.math.roundToInt

fun main() {
    val num1 = 1.5
    val num2 = 1.4
    val num3 = 1.50000001
    println(num1.roundToInt())
    println(num2.roundToInt())
    println(num3.roundToInt())
}