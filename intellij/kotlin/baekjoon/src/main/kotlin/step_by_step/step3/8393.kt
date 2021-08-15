// TODO: 합
package step_by_step.step3

import java.util.*

fun main() {
    val scan = Scanner(System.`in`)
    val n = scan.nextInt()
    var sum = 0
    for (i in 1..n) {
        sum += i
    }
    println(sum)
}