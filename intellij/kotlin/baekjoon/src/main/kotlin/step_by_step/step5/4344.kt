// TODO: 평균은 넘겠지
package step_by_step.step5

fun main() {
    val c = readLine()!!.toInt()
    repeat(c) {
        val studentInfo = readLine()!!.split(" ").map { it.toInt() }
        val n = studentInfo[0]
        val average = studentInfo.drop(1).sum().toDouble() / n // 학생 수 제외
        val overAverage = studentInfo.drop(1).filter { it > average }.size
        val percentage = (overAverage.toDouble() / n) * 100
        println(String.format("%.3f%%", percentage))
    }
}