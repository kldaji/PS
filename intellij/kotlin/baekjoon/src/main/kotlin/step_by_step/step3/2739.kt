// TODO: 구구단
package step_by_step.step3

import java.util.*

fun main() {
    val scan = Scanner(System.`in`)
    val num = scan.nextInt()
    for (i in 1..9) {
        println("$num * $i = ${num*i}")
    }
}