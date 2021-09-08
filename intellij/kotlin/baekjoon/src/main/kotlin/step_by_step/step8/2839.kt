// TODO: 설탕 배달
package step_by_step.step8

fun main() {
    // dp[i] = i kg 담을 수 있는 최소 봉지 개수
    val dp = Array(5001) { Int.MAX_VALUE }
    dp[3] = 1
    dp[5] = 1
    val n = readLine()!!.toInt()
    if (n <= 5) {
        if (dp[n] == Int.MAX_VALUE) println(-1)
        else println(dp[n])
    } else {
        (6..n).forEach {
            if (dp[it - 3] != Int.MAX_VALUE) {
                dp[it] = kotlin.math.min(dp[it], dp[it - 3] + 1)
            }
            if (dp[it - 5] != Int.MAX_VALUE) {
                dp[it] = kotlin.math.min(dp[it], dp[it - 5] + 1)
            }
        }
        if (dp[n] == Int.MAX_VALUE) println(-1)
        else println(dp[n])
    }
}