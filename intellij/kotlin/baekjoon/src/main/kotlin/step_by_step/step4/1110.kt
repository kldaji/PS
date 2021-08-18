// TODO: 더하기 사이클
package step_by_step.step4

import java.util.*

fun main() {
    val scan = Scanner(System.`in`)
    val n = scan.nextInt()
    var temp = n
    var cnt = 0
    while(true) {
        val ten = temp % 10
        val one = ((temp / 10) + (temp % 10)) % 10
        temp = ten*10 + one
        cnt++
        if (temp == n) break
    }
    println(cnt)
}