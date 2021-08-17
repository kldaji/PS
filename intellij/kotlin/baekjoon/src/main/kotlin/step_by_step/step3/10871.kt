// TODO: X보다 작은 수
package step_by_step.step3

//import java.util.*
//
//fun main() {
//    val scan = Scanner(System.`in`)
//    val n = scan.nextInt()
//    val x = scan.nextInt()
//    for (i in 1..n) {
//        val temp = scan.nextInt()
//        if (temp < x) {
//            println(temp)
//        }
//    }
//}

fun main() {
    val br = System.`in`.bufferedReader()
    val (n, x) = br.readLine().split(" ").map { it.toInt() }
    val seq = br.readLine().split(" ").map { it.toInt() }
    seq.forEach {
        if (it < x) {
            print("$it ")
        }
    }
    br.close()
}