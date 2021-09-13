// TODO: 소수
package step_by_step.step9

fun eratosthenes3(numbers: BooleanArray, n: Int) {
    (2..n).forEach {
        var i = 2
        while (it * i <= n) {
            numbers[it * i] = false
            i++
        }
    }
}

fun main() {
    val numbers = BooleanArray(1000001) { true }
    numbers[1] = false
    val (m, n) = readLine()!!.toString().split(" ").map { it.toInt() }
    eratosthenes3(numbers, n)
    for (i in m..n){
        if (numbers[i]) {
            println(i)
        }
    }
}