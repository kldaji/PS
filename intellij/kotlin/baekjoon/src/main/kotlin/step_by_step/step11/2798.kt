// TODO: 블랙잭
package step_by_step.step11

import kotlin.math.max

fun main() {
    val (n, m) = readLine()!!.toString().split(" ").map { it.toInt() }
    val cardList = readLine()!!.toString().split(" ").map { it.toInt() }
    var maxValue = 0
    for (i in 0 until n - 2) {
        for (j in i + 1 until n - 1) {
            for (k in j + 1 until n) {
                val total = cardList[i] + cardList[j] + cardList[k]
                if (total <= m) {
                    maxValue = max(maxValue, total)
                }
            }
        }
    }
    println(maxValue)
}