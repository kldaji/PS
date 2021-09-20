// TODO: 터렛
package step_by_step.step9

import kotlin.math.abs
import kotlin.math.sqrt
import kotlin.math.pow

fun getDistance(x1: Double, y1: Double, x2: Double, y2: Double): Double {
    return sqrt((x1 - x2).pow(2) + (y1 - y2).pow(2))
}

fun main() {
    // x1, y1, r1, x2, y2, r2
    repeat(readLine()!!.toInt()) {
        val info = readLine()!!.toString().split(" ").map { it.toInt() }
        val distance = getDistance(info[0].toDouble(), info[1].toDouble(), info[3].toDouble(), info[4].toDouble())
        if (distance == 0.0) {
            if (info[2] == info[5]) println(-1)
            else println(0)
        } else {
            if (distance > info[2] + info[5]) println(0)
            else if (distance < (abs(info[2] - info[5]).toDouble())) println(0)
            else if (distance == (info[2] + info[5]).toDouble()) println(1)
            else if (distance == (abs(info[2] - info[5]).toDouble())) println(1)
            else println(2)
        }
    }
}