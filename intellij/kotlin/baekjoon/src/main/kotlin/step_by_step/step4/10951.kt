// TODO: A+B - 4
package step_by_step.step4

import java.util.*

fun main() {
    val scan = Scanner(System.`in`)
    while (scan.hasNextInt()) {
        val a = scan.nextInt()
        val b = scan.nextInt()
        println(a + b)
    }
}