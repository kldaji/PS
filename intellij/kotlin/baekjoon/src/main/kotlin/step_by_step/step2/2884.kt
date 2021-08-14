// TODO: 알람 시계
package step_by_step.step2

import java.util.*

data class Clock(var h: Int, var m: Int) {
    override fun toString(): String {
        return "$h $m"
    }
}

fun fixAlarm(clock: Clock) {
    if (clock.m < 45) {
        if (clock.h == 0) {
            clock.h = 23
        }else {
            clock.h -= 1
        }
        clock.m += 15
    } else {
        clock.m -= 45
    }
}
fun main() {
    val scan = Scanner(System.`in`)
    val h = scan.nextInt()
    val m = scan.nextInt()
    var clock = Clock(h, m)
    fixAlarm(clock) // 얕은 복사
    println(clock)
}