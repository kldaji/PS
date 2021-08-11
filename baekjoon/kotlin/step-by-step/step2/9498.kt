/*
 * 시험 성적
 */

import java.util.*

fun main() {
    val input = Scanner(System.`in`)
    when (input.nextInt()) {
        in 90..100 -> println("A")
        in 80..89 -> println("B")
        in 70..79 -> println("C")
        in 60..69 -> println("D")
        else -> println("F")
    }
}