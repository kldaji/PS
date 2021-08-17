// TODO: 별 찍기 - 2
package step_by_step.step3

import java.util.*

fun main() {
    val scan = Scanner(System.`in`)
    val n = scan.nextInt()
    for (i in 1..n) {
        for(j in n-i downTo 1) {
            print(" ")
        }
        for (j in 1..i) {
            print("*")
        }
        println()
    }
}