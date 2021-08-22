// TODO: 셀프 넘버
package step_by_step.step6

fun d(n: Int): Int {
    var temp = n
    var result = temp
    while (temp > 0) {
        result += temp % 10
        temp /= 10
    }
    return result
}

fun main() {
    val setA = mutableSetOf<Int>()
    val setB = mutableSetOf<Int>()

    (1..10000).forEach {
        setA.add(it)
        setB.add(d(it))
    }

    setA.subtract(setB).forEach {
        println(it)
    }
}