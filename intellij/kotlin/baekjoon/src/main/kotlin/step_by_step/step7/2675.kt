// TODO: 문자열 반복
package step_by_step.step7

fun repeatString(r: Int, c: Char): String {
    var str = ""
    repeat(r) {
        str += c
    }
    return str
}

fun main() {
    repeat(readLine()!!.toInt()) {
        val (R, S) = readLine()!!.toString().split(" ")
        var str = ""
        S.forEach {
            str += repeatString(R.toInt(), it)
        }
        println(str)
    }
}

