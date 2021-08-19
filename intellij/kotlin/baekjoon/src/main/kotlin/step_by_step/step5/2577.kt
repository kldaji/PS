// TODO: 숫자의 개수
package step_by_step.step5

fun main() {
    var result = 1
    repeat(3) {
        result *= readLine()!!.toInt()
    }
    val arr = Array(10) { 0 }
    while (result > 0) {
        val index = result % 10
        arr[index]++
        result /= 10
    }
    arr.forEach {
        println(it)
    }
}