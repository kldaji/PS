// TODO: 수 정렬하기
package step_by_step.step12

fun bubbleSort(mutableList: MutableList<Int>): List<Int> {
    val returnList = mutableList
    for (i in 0 until returnList.size) {
        for (j in i + 1 until returnList.size) {
            if (returnList[i] > returnList[j]) {
                val temp = returnList[i]
                returnList[i] = returnList[j]
                returnList[j] = temp
            }
        }
    }
    return returnList
}

fun insertSort(mutableList: MutableList<Int>): List<Int> {
    val returnList = mutableList
    for (i in 1 until returnList.size) {
        val key = returnList[i]
        var j = i - 1
        while (j >= 0 && returnList[j] > key) {
            returnList[j+1] = returnList[j]
            j--
        }
        returnList[j+1] = key
    }
    return returnList
}

fun main() {
    val mutableList = mutableListOf<Int>()
    val n = readLine()!!.toInt()
    repeat(n) {
        val num = readLine()!!.toInt()
        mutableList.add(num)
    }
    val sortedList = insertSort(mutableList)
    println(sortedList.joinToString("\n"))
}