// TODO: 소수
package step_by_step.step9

fun eratosthenes2(numbers: Array<Boolean>) {
    (2..10000).forEach {
        var i = 2
        while (it * i <= 10000) {
            numbers[it * i] = false
            i++
        }
    }
}

fun main() {
    val numbers = Array(10001) { true }
    numbers[1] = false
    eratosthenes2(numbers)
    val m = readLine()!!.toInt()
    val n = readLine()!!.toInt()
    val primeNumberList = (m..n).filter { numbers[it] }
    if (primeNumberList.isEmpty()) {
        println(-1)
        return
    }
    println(primeNumberList.sum())
    println(primeNumberList.minOrNull())
}