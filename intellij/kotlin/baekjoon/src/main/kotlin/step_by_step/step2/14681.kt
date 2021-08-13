// TODO: 사분면 고르기
package step_by_step.step2

import java.util.*

// x != 0 && y != 0
fun quadrant(x: Int, y: Int): Int {
    if (x > 0  && y > 0) return 1
    if (x < 0 && y > 0) return 2
    if (x < 0 && y < 0) return 3
    if (x > 0 && y < 0) return 4
    return -1
}

fun main() {
    val scan = Scanner(System.`in`)
    val x = scan.nextInt()
    val y = scan.nextInt()
    println(quadrant(x, y))
}