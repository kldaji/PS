// TODO: 평균
package step_by_step.step5

fun main() {
    val n = readLine()!!.toInt()
    val scores = readLine()!!.split(" ").map { it.toInt() }
    val highScore = scores.maxOrNull()!!.toDouble()
    val updatedScores = mutableListOf<Double>()
    scores.forEach {
        updatedScores.add((it.toDouble() / highScore!!) * 100.0)
    }
    println(updatedScores.sum() / n.toDouble())
}