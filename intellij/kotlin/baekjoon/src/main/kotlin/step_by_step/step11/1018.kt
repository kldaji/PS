// TODO: 체스판 다시 칠하기
package step_by_step.step11

import kotlin.math.min

val masterBoard1 = listOf(
    "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"
)

val masterBoard2 = listOf(
    "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"
)

private fun compareToMaster1(board: List<String>, x: Int, y: Int): Int {
    var count = 0
    for (i in x..(x + 7)) {
        for (j in y..(y + 7)) {
            if (masterBoard1[i - x][j - y] != board[i][j]) count++
        }
    }
    return count
}

private fun compareToMaster2(board: List<String>, x: Int, y: Int): Int {
    var count = 0
    for (i in x..(x + 7)) {
        for (j in y..(y + 7)) {
            if (masterBoard2[i - x][j - y] != board[i][j]) count++
        }
    }
    return count
}

fun main() {
    var minValue = Integer.MAX_VALUE
    val (n, m) = readLine()!!.toString().split(" ").map { it.toInt() }
    val board = mutableListOf<String>()
    repeat(n) {
        board.add(readLine()!!.toString())
    }
    for (i in 0..(n - 8)) {
        for (j in 0..(m - 8)) {
            minValue = min(minValue, compareToMaster1(board, i, j))
            minValue = min(minValue, compareToMaster2(board, i, j))
        }
    }
    println(minValue)
}