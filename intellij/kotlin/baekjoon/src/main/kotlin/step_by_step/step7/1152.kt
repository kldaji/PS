// TODO: 단어의 개수
package step_by_step.step7

fun main() {
    val words = readLine()!!.split(" ").filter { it.isNotBlank() }
    println(words.size)
}

