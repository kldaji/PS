// TODO: 수 정렬하기 3
package step_by_step.step12

import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    val n = br.readLine().toInt()
    val baseArray = IntArray(10001)
    repeat(n) {
        baseArray[br.readLine().toInt()]++
    }
    for (i in baseArray.indices) {
        bw.write("$i\n".repeat(baseArray[i]))
    }
    bw.close()
    br.close()
}