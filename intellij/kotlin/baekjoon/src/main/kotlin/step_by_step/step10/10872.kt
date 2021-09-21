// TODO: 팩토리얼
package step_by_step.step10

fun fact(n: Int): Int {
    if (n == 0) return 1
    if (n == 1) return 1
    return n * fact(n - 1)
}
fun main() {
    println(fact(readLine()!!.toInt()))
}