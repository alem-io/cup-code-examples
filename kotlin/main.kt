import java.util.Scanner
import java.util.Random

fun main(args : Array<String>) {
    while (true) {
        val scan = Scanner(System.`in`)

        var str: String = scan.nextLine()

        var h: Int = str.split(" ")[1].toInt()

        for (i in 0..h-1) {
            var str: String = scan.nextLine()
        }

        var n: Int = scan.nextLine().toInt()
        
        for (i in 0..n-1) {
            var str: String = scan.nextLine()
        }

        System.err.println("debug mode")

        var actions: Array<String> = arrayOf("left", "right", "up", "down", "stay")
        var random_index: Int = (0..4).random()

        println(actions[random_index])
    }
}
