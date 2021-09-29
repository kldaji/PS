// TODO: 영화감독 숌
package step_by_step.step11

fun main() {
    val n = readLine()!!.toInt()
    var count = 0
    var num = 666
    while (true) {
        if ("666" in num.toString()) count++
        if (count == n) {
            println(num)
            break
        }
        num++
    }
}