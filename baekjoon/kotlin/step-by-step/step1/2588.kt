/*
 * 곱셈
 */
import java.util.*

fun main() {
    val input = Scanner(System.`in`)
    val num1 = input.nextInt()
    val num2 = input.nextInt()
    var temp = num2
    while(temp > 0) {
        println(num1 * (temp % 10))
        temp /= 10
    }
    println(num1 * num2)
}