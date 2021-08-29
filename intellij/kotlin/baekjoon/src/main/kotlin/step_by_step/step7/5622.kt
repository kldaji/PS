// TODO: 다이얼
package step_by_step.step7

fun calculateTime(c: Char): Int {
    return when (c) {
        'A', 'B', 'C' -> 3
        'D', 'E', 'F' -> 4
        'G', 'H', 'I' -> 5
        'J', 'K', 'L' -> 6
        'M', 'N', 'O' -> 7
        'P', 'Q', 'R', 'S' -> 8
        'T', 'U', 'V' -> 9
        'W', 'X', 'Y', 'Z' -> 10
        else -> -1
    }
}

fun main() {
    val dial = readLine()!!.toString()
    var answer = 0
    dial.forEach {
        answer += calculateTime(it)
    }
    println(answer)
}

