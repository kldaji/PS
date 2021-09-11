// TODO: 소인수분해
package step_by_step.step9

fun spawnPrimeFactor(n: Int): Int {
    var num = n
    var i = 2
    while (num % i != 0) {
        i++
    }
    return i
}

fun main() {
    var n = readLine()!!.toInt()
    if (n == 1) {
        return
    }
    while (n > 1) {
        val primFactor = spawnPrimeFactor(n)
        println(primFactor)
        n /= primFactor
    }
}