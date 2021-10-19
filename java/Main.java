import java.util.Scanner;
import java.util.Random;

    public class Main {

    public static void main(String[] args) {

        while (true) {
            Scanner scan = new Scanner(System.in);
            int h, w, player_id, tick, n, p_id, x, y, param_1, param_2;
            String str, type;
            
            w = scan.nextInt();
            h = scan.nextInt();
            player_id = scan.nextInt();
            tick = scan.nextInt();
            str = scan.nextLine();
            
            System.err.println(h + "" + w + "" + player_id + "" + tick + "");

            for (int i = 0; i < h; i++) {
                str = scan.nextLine();
            }

            n = scan.nextInt();
            
            System.err.println("n:" + n);
            
            type = scan.nextLine();
            
            for (int i = 0; i < n; i++) {
                type = scan.next();
                p_id = scan.nextInt();
                x = scan.nextInt();
                y = scan.nextInt();
                param_1 = scan.nextInt();
                param_2 = scan.nextInt();
                System.err.println(type + "" + p_id + "" + x + "" + y + "" + param_1 + "" + param_2);
            }

            System.err.println("debug mode");

            String actions[] = {"left", "right", "up", "down", "bomb"};
            Random r = new Random();
            int random_index = r.nextInt(1000) % 5;
            System.out.println(actions[random_index]);
        }
    }

}




