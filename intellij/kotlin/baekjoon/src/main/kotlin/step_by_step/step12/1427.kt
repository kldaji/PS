// TODO: 소트인사이드
package step_by_step.step12

fun main() {
    val br = System.`in`.bufferedReader()
    val bw = System.out.bufferedWriter()
    val digitList = br.readLine().split("").filter { it.isNotBlank() }.sorted().reversed()
    bw.write(digitList.joinToString(""))
    bw.close()
    br.close()
}