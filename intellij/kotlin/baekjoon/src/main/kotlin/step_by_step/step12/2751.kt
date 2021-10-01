// TODO: 수 정렬하기 2
package step_by_step.step12

import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    val mutableList = mutableListOf<Int>()
    val n = br.readLine().toInt()
    repeat(n) {
        val num = br.readLine().toInt()
        mutableList.add(num)
    }
    mutableList.sorted().forEach {
        bw.write(it.toString() + "\n")
    }
    bw.close()
    br.close()
}