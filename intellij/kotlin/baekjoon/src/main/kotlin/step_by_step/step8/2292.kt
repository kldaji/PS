// TODO: 벌집
package step_by_step.step8

fun beeHouse(room: Int): Int {
    if (room == 1) return 1
    var n = 1
    while (3 * n * (n - 1) + 2 <= room) n++
    return n
}

fun main() {
    val room = readLine()!!.toInt()
    // 1 : 1
    // 2 ~ 7 : 2 (5)
    // 8 ~ 19 : 3 (11)
    // 20 ~ 37 : 4 (17)
    // 38 ~ 61 : 5 (23)
    // ... => 계차수열!!!
    // a(n) = a(1) + sum(b(1..(n-1)))
    // a(n) = 3n(n-1) + 2
    println(beeHouse(room))
}