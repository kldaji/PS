// TODO: 그룹 단어 체커
package step_by_step.step7

fun checkGroupWord(c: Char, alpha: HashMap<Char, Boolean>): Boolean {
    return alpha.containsKey(c)
}

fun main() {
    var count = 0
    repeat(readLine()!!.toInt()) {
        val word = readLine()!!.toString()
        var index = 0
        val alphabet = hashMapOf<Char, Boolean>()
        var prev = word[index++]
        var flag = true
        alphabet[prev] = true

        while (index < word.length) {
            if (prev != word[index]) {
                prev = word[index]
                if (checkGroupWord(prev, alphabet)) {
                    flag = false
                    break
                }
                alphabet[prev] = true
            }
            index++
        }

        if (flag) count++
    }
    println(count)
}

