// TODO: A+B - 5
package step_by_step.step4

import java.util.*

fun main() {
    val scan = Scanner(System.`in`)
    while (true) {
        val a = scan.nextInt()
        val b = scan.nextInt()
        if (a == 0 && b == 0) break
        println(a + b)
    }
}