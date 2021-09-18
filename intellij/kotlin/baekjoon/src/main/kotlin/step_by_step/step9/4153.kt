// TODO: 직각삼각형
package step_by_step.step9

fun pythagoras(a: Int, b: Int, c: Int): Int {
    return if (a == 0 && b == 0 && c == 0) -1
    else if (a * a + b * b == c * c) 1
    else 0
}

fun main() {
    while (true) {
        val triangle = readLine()!!.toString().split(" ").map { it.toInt() }.sorted()
        when (pythagoras(triangle[0], triangle[1], triangle[2])) {
            1 -> println("right")
            0 -> println("wrong")
            -1 -> break
        }
    }

}