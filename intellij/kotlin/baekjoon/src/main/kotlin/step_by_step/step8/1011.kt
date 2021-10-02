// TODO: Fly me to the Alpha Centauri
package step_by_step.step8

import kotlin.math.*

fun main() {
    repeat(readLine()!!.toInt()) {
        var (x, y) = readLine()!!.toString().split(" ").map { it.toInt() }
        when (y - x) {
            1 -> println(1)
            2 -> println(2)
            3 -> println(3)
            else -> {
                val result = sqrt((y - x).toDouble())
                if (result <= round(result)) println((round(result) * 2 - 1).toInt())
                else println((round(result) * 2).toInt())
            }
        }
    }
}