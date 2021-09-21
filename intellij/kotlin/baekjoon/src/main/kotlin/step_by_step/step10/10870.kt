// TODO: 피보나치 수 5
package step_by_step.step10

fun fibo(n: Int): Int {
    if (n == 0) return 0
    if (n == 1) return 1
    if (n == 2) return 1
    return fibo(n - 1) + fibo(n - 2)
}

fun main() {
    println(fibo(readLine()!!.toInt()))
}