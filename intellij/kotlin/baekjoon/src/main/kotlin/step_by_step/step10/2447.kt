// TODO: 별 찍기 - 10
package step_by_step.step10

fun divide(arr: Array<Array<String>>, x: Int, y: Int, n: Int) {
    if (n == 1) {
        arr[x][y] = "*"
        return
    }
    divide(arr, x, y, n / 3)
    divide(arr, x, y + n / 3 * 1, n / 3)
    divide(arr, x, y + n / 3 * 2, n / 3)
    divide(arr, x +  n / 3 * 1, y, n / 3)
    divide(arr, x + n / 3 * 1, y +  n / 3 * 2, n / 3)
    divide(arr, x + n / 3 * 2, y + n / 3 * 0, n / 3)
    divide(arr, x + n / 3 * 2, y + n / 3 * 1, n / 3)
    divide(arr, x + n / 3 * 2, y + n /3 * 2, n / 3)
}

fun main() {
    val n = readLine()!!.toInt()
    val arr = Array(n) { Array(n) { " " } }
    divide(arr, 0, 0, n)
    for (i in 0 until n ) {
        for (j in 0 until n) {
            print(arr[i][j])
        }
        println()
    }
}