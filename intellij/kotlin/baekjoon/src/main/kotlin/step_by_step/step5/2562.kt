// TODO: 최대
package step_by_step.step5

fun main() {
    var value = 0
    var index = 0
    for (i in 1..9) {
        val temp = readLine()!!.toInt()
        if (temp > value) {
            value = temp
            index = i
        }
    }
    println(value)
    println(index)
}