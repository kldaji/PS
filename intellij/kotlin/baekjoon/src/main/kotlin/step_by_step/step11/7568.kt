// TODO: 덩치
package step_by_step.step11

data class Person(val height: Int, val weight: Int, var rank: Int = 1) {
    operator fun compareTo(other: Person): Int {
        return if (other.height > this.height && other.weight > this.weight) 1
        else 0
    }
}

fun main() {
    val n = readLine()!!.toInt()
    val personList = mutableListOf<Person>()
    repeat(n) {
        val (height, weight) = readLine()!!.toString().split(" ").map { it.toInt() }
        personList.add(Person(height, weight))
    }

    for (person in personList) {
        for (otherPerson in personList) {
            if (person != otherPerson && person.compareTo(otherPerson) == 1) {
                person.rank++
            }
        }
    }

    personList.forEach {
        print("${it.rank} ")
    }
}