// TODO: 나머지
package step_by_step.step5

fun main() {
    val remainder = mutableSetOf<Int>()
    repeat(10) {
        val num = readLine()!!.toInt()
        remainder.add(num % 42)
    }
    println(remainder.size)
}