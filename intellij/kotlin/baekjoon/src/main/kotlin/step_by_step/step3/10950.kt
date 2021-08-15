// TODO: A+B - 3
package step_by_step.step3

import java.util.*

fun main() {
    val scan = Scanner(System.`in`)
    val tc = scan.nextInt()
    for (i in 1..tc) {
        val a = scan.nextInt()
        val b = scan.nextInt()
        println(a+b)
    }
}