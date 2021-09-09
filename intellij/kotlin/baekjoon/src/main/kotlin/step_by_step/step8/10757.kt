// TODO: 큰 수 A+B
package step_by_step.step8

fun main() {
    println(readLine()!!
        .split(" ")
        .map { it.toBigDecimal() }
        .reduce { acc, bigDecimal -> acc + bigDecimal }
    )
}