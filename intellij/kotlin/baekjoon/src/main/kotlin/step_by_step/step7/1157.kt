// TODO: 단어 공부
package step_by_step.step7

import java.util.*

fun main() {
    val alpha = Array(26) { 0 }
    val word = readLine()!!.toString().uppercase(Locale.getDefault())
    word.forEach {
        alpha[it.code - 'A'.code]++
    }
    alpha.maxOrNull()
    val maxValue = alpha.maxByOrNull { it }
    val count = alpha.count {
        it == maxValue
    }
    if (count > 1) {
        println("?")
    } else {
        val answer = alpha.indexOf(maxValue)
        println("${(answer + 'A'.code).toChar()}")
    }
}

