// TODO: 한수
package step_by_step.step6

fun isHanSoo(x: Int): Boolean {
    var temp = x
    var prev = temp % 10
    temp /= 10
    var now = temp % 10
    temp /= 10
    val diff = now - prev
    while (temp > 0) {
        prev = now
        now = temp % 10
        temp /= 10
        if (now - prev != diff) return false
    }
    return true
}

fun main() {
    val n = readLine()!!.toInt()
    if (n < 100) {
        println(n)
    } else {
        var cnt = 99
        (100..n).forEach {
            if (isHanSoo(it)) cnt++
        }
        println(cnt)
    }

}