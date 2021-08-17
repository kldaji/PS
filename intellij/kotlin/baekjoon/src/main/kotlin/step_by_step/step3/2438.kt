// TODO: 별 찍기 - 1
package step_by_step.step3

import java.util.*

fun main() {
    val scan = Scanner(System.`in`)
    val n = scan.nextInt()
    for (i in 1..n) {
        for (j in 1..i) {
            print("*")
        }
        println()
    }
}