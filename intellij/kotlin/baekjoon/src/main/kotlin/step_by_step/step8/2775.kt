// TODO: 부녀회장이 될테야
package step_by_step.step8

fun getResident(floor: Int, room: Int): Int {
    if (floor == 0) return room
    return (1..room).reduce { acc, i -> acc + getResident(floor - 1, i) }
}

fun main() {
    repeat(readLine()!!.toInt()) {
        val a = readLine()!!.toInt()
        val b = readLine()!!.toInt()
        println(getResident(a, b))
    }
}