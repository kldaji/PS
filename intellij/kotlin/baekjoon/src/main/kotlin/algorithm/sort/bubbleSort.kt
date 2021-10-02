package algorithm.sort

fun bubbleSort(unsortedList: List<Int>): List<Int> {
    val bubbleSortList = unsortedList.toMutableList()
    for (i in 0 until bubbleSortList.size) { // i번 순회
        for (j in 1 until (bubbleSortList.size - i)) { // 뒤에서부터 i개는 이미 정렬됨.
            if (bubbleSortList[j - 1] > bubbleSortList[j]) { // swap
                val temp = bubbleSortList[j - 1]
                bubbleSortList[j - 1] = bubbleSortList[j]
                bubbleSortList[j] = temp
            }
        }
    }
    return bubbleSortList
}

fun main() {
    val testList = listOf(41, 34, 6, 16, 45, 12, 3, 5, 19)
    println(bubbleSort(testList))
}