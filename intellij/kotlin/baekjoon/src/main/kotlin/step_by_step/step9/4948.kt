// TODO: 베르트랑 공준
package step_by_step.step9

fun eratosthenes4(numbers: BooleanArray) {
    (2..123456 * 2).forEach {
        var i = 2
        while (it * i <= 123456 * 2) {
            numbers[it * i] = false
            i++
        }
    }
}

fun main() {
    val numbers = BooleanArray(123457 * 2) { true }
    numbers[1] = false
    eratosthenes4(numbers)
    do {
        val n = readLine()!!.toInt()
        if (n == 0) break
        var count = 0
        ((n + 1)..2 * n).forEach {
            if (numbers[it]) {
                count++
            }
        }
        println(count)
    } while (true)
}