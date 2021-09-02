// TODO: 손익분기점
package step_by_step.step8

fun breakEvenPoint(fixed: Long, variable: Long, apportioned: Long): Long {
    if (variable >= apportioned) return -1
    return (fixed / (apportioned - variable)) + 1
}

fun main() {
    val (A, B, C) = readLine()!!.split(" ").map { it.toLong() }
    println(breakEvenPoint(A, B, C))
}