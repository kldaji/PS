/*
 * A+B, A-B, AxB, 사칙연산, 나머지 
 */

import java.util.*

fun main() {
    val input = Scanner(System.`in`)
    val A = input.nextInt()
    val B = input.nextInt()
    val C = input.nextInt()
    println((A+B)%C)
    println(((A%C) + (B%C))%C)
    println((A*B)%C)
    println(((A%C) * (B%C))%C)
}