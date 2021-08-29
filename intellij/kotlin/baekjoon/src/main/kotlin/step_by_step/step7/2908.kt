// TODO: 상수
package step_by_step.step7

fun main() {
    val (a, b) = readLine()!!.toString().split(" ")
    val c = Integer.parseInt(a.reversed())
    val d = Integer.parseInt(b.reversed())
    if (c > d) println(c)
    else println(d)
}

