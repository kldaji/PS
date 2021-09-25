// TODO: 분해합
package step_by_step.step11

fun disassemble(x: Int): Int {
    var number = x
    var total = x
    while (number > 0) {
        total += (number % 10)
        number /= 10
    }
    return total
}

fun main() {
    val n = readLine()!!.toInt()
    var flag = false
    for (i in 1..n) {
        if (disassemble(i) == n) {
            flag = true
            println(i)
            return
        }
    }
    if (!flag) println(0)
}