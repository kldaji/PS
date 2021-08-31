// TODO: 크로아티아 알파벳
package step_by_step.step7

fun main() {
    var count = 0
    val word = readLine()!!.toString()
    var index = 0

    // 알파벳이 2개로 이루어지는 경우가 많기 때문에
    // index range check 를 최소화 하려고 word.length - 1 까지 범위를 지정했다.
    while (index < word.length - 1) {
        val next = index + 1
        when (word[index]) {
            'c' -> {
                if (word[next] == '=') index++
                else if (word[next] == '-') index++
            }
            'd' -> {
                if (word[next] == 'z' && (next + 1) < word.length && word[next + 1] == '=') index += 2
                else if (word[next] == '-') index++
            }
            'l', 'n' -> if (word[next] == 'j') index++
            's', 'z' -> if (word[next] == '=') index++
            else -> {
                // nothing
            }
        }
        index++
        count++
    }

    // while 문에서 word.length - 1 까지 범위를 지정했기 때문에
    // 만약 마지막 alphabet 이 하나로 이루어지는 경우 count + 1 을 해주어야 한다.
    if (index == word.length - 1) {
        count++
    }

    println(count)
}

