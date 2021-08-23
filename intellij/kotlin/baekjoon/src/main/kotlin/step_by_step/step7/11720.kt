// TODO: 숫자의 합
package step_by_step.step7

fun main() {
    val n = readLine()!!.toInt()
    val number = readLine()!!.toString()
        .split("")
        .filter { it.isNotEmpty() }
        .map { it.toInt() }
    println(number.reduce { acc, i -> acc + i })
}

// https://blog.leocat.kr/notes/2020/03/09/kotlin-reduce-and-fold