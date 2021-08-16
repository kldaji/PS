// TODO: 빠른 A+B
package step_by_step.step3

import java.io.*

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    br.use { br ->
        bw.use { bw ->
            repeat(br.readLine().toInt()) {
                try {
                    val (a, b) = br.readLine().split(" ").map { it.toInt() }
                    bw.write((a + b).toString() + "\n")
                } catch(e: IOException) {
                    e.printStackTrace()
                }
            }
        }
    }
}