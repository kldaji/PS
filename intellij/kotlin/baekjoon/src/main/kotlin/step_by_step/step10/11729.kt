// TODO: 하노이 탑 이동 순서
package step_by_step.step10

import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import kotlin.math.pow

fun hanoi(n: Int, a: Int, b: Int, c: Int, bw: BufferedWriter) {
    if (n == 1) {
        bw.write("$a $c\n")
        return
    }
    hanoi(n - 1, a, c, b, bw)
    bw.write("$a $c\n")
    hanoi(n - 1, b, a, c, bw)
}

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    val n = br.readLine().toInt()
    bw.write("${(2.0.pow(n.toDouble()) - 1).toInt()}\n")
    hanoi(n, 1, 2, 3, bw)
    bw.flush()
    bw.close()
}