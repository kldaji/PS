// TODO: 윤년
package step_by_step.step2
import java.util.*

fun isLeapYear(year: Int): Boolean {
    return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
}

fun main() {
    return if (isLeapYear(Scanner(System.`in`).nextInt())) println(1)
    else println(0)
}