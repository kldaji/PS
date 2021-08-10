/*
 * 두 수 비교하기
 */

import java.util.*

fun main() {
    val input = Scanner(System.`in`)
    val A = input.nextInt()
    val B = input.nextInt()

    if (A > B) println(">")
    else if (A < B) println("<")
    else println("==")
}