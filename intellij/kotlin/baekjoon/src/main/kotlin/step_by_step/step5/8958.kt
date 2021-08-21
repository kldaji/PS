// TODO: OX퀴즈
package step_by_step.step5

fun main() {
    val n = readLine()!!.toInt()
    repeat(n) {
        val scores = readLine()!!.toString()
        var sum = 0
        var count = 1
        scores.forEach {
            if (it == 'O') {
                sum += count
                count++
            } else { // X
                count = 1
            }
        }
        println(sum)
    }
}