// TODO: 소수 찾기
package step_by_step.step9

fun eratosthenes(numbers: Array<Boolean>) {
    (2..1000).forEach {
        var i = 2
        while (it * i <= 1000) {
            numbers[it * i] = false
            i++
        }
    }
}

fun main() {
    val numbers = Array(1001) { true }
    numbers[1] = false
    eratosthenes(numbers)
    val n = readLine()!!.toInt()
    val inputNumberList = readLine()!!.toString()
        .split(" ")
        .map { it.toInt() }
        .filter { numbers[it] }
    println(inputNumberList.size)
}