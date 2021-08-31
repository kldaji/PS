package step_by_step.step3
// 랜덤 텍스트 생성
private fun spawnRandomText(): String {
    val charPool: List<Char> = ('a'..'z') + ('A'..'Z') + ('0'..'9')
    var randomString = ""
    val num = kotlin.random.Random.nextInt(2, 6)
    randomString = (1..num)
        .map { i -> kotlin.random.Random.nextInt(0, charPool.size) }
        .map(charPool::get)
        .joinToString("")
    return randomString
}
fun main() {
    println(spawnRandomText())
}