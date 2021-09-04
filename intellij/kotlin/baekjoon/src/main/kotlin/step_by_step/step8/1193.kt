// TODO: 분수찾기
package step_by_step.step8

fun spawnFountain(x: Int): String {
    if (x == 1) return "1/1"
    var n = 2
    while (2 * x > n * (n + 1)) n++
    val total = n * (n + 1) / 2
    val numerator = total - x + 1
    val denominator = x - total + n
    return if (n % 2 != 0) "$numerator/$denominator"
    else "$denominator/$numerator"
}

fun main() {
    val x = readLine()!!.toInt()
    // 분자
    // 1, 1 2, 3 2 1, 1 2 3 4, ...
    // 분모
    // 1, 2 1, 1 2 3, 4 3 2 1, ...
    // 1..n 합 = n(n+1)/2 (n >= 2)
    println(spawnFountain(x))
}