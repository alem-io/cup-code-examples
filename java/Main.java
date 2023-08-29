import java.util.Scanner;
import java.util.Random;

    public class Main {

    public static void main(String[] args) {

        while (true) {
            Scanner scan = new Scanner(System.in);
            int n, m, player_id, tick, p_id, x, y, param_1, param_2;
            String str, type;

            n = scan.nextInt();
            player_id = scan.nextInt();
            tick = scan.nextInt();
            str = scan.nextLine();
            
            System.err.println(n + "" + player_id + "" + tick + "");

            for (int i = 0; i < n; i++) {
                str = scan.nextLine();
            }

            m = scan.nextInt();
            str = scan.nextLine();
            System.err.println("m:" + m);
            
            for (int i = 0; i < m; i++) {
                str = scan.nextLine();
            }

            System.err.println("debug mode");

            System.out.println("100 100 200 200");
        }
    }

}




