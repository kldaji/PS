// TODO: 알파벳 찾기
package step_by_step.step7

fun alphaToInt(c: Char): Int {
    return c.code - 'a'.code
}

fun main() {
    val s = readLine()!!.toString()
    val array = Array(26) { -1 }
    s.forEachIndexed { index, c ->
        if (array[alphaToInt(c)] == -1) {
            array[alphaToInt(c)] = index
        }
    }
    println(array.joinToString(" "))
}

