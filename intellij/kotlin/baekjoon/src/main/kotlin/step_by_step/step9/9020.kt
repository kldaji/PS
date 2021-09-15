// TODO: 골드바흐의 추축
package step_by_step.step9

fun eratosthenes4(numbers: Array<Boolean>) {
    (2..10000).forEach {
        var i = 2
        while (it * i <= 10000) {
            numbers[it * i] = false
            i++
        }
    }
}

fun main() {
    val numbers = Array(10001) { true }
    numbers[1] = false
    eratosthenes4(numbers)
    repeat(readLine()!!.toInt()) {
        val n = readLine()!!.toInt()
        val candidateList = mutableListOf<Candidate>()
        (2..n / 2).forEach {
            if (numbers[it] && numbers[n - it]) {
                candidateList.add(Candidate(it, n - it, n - it - it))
            }
        }
        val winner = candidateList.minByOrNull { it.diff }
        println(winner)
    }
}

data class Candidate(val num1: Int, val num2: Int, val diff: Int) {
    override fun toString(): String {
        return "$num1 $num2"
    }
}