// TODO: A+B - 7
package step_by_step.step3

import java.util.*

fun main() {
    val scan = Scanner(System.`in`)
    val t = scan.nextInt()
    repeat(t) {
        val a = scan.nextInt()
        val b = scan.nextInt()
        println("Case #${it+1}: ${a+b}")
    }
}