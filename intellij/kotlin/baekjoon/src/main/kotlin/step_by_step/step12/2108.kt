// TODO: 통계학
package step_by_step.step12

import kotlin.math.roundToInt

fun getAverage(numberList: MutableList<Int>): Int = numberList.average().roundToInt()

fun getMid(numberList: MutableList<Int>): Int {
    val sortedList = numberList.sorted()
    val mid = numberList.size / 2
    return sortedList[mid]
}

fun getFreq(numberList: MutableList<Int>): Int {
    val freqMap = numberList.groupingBy { it }.eachCount()
    val maxValue = freqMap.maxOf { it.value }
    val maxFreqMap = freqMap.filter { it.value == maxValue }
    val mapKeys = maxFreqMap.keys.sorted()
    return if (mapKeys.size == 1) {
        mapKeys.first()
    } else {
        mapKeys[1]
    }
}

fun getRange(numberList: MutableList<Int>): Int {
    val maxValue = numberList.maxOf { it }
    val minValue = numberList.minOf { it }
    return maxValue - minValue
}

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val n = br.readLine().toInt()
    val numberList = mutableListOf<Int>()
    repeat(n) {
        numberList.add(br.readLine().toInt())
    }
    bw.write("${getAverage(numberList)}\n")
    bw.write("${getMid(numberList)}\n")
    bw.write("${getFreq(numberList)}\n")
    bw.write("${getRange(numberList)}\n")
    bw.close()
    br.close()
}