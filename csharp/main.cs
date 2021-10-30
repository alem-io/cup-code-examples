using System;
using System.Collections.Generic;

class Demo {
   static void Main() {
      while (true) {
         string line;
      
         line = Console.ReadLine();
         int h = Convert.ToInt32(line.Split(' ')[1]);
         for (int i = 0; i < h; i++) {
            line = Console.ReadLine();
         }

         line = Console.ReadLine();
         int n = Convert.ToInt32(line);
         for (int i = 0; i < n; i++) {
            line = Console.ReadLine();
            string[] values = line.Split(' ');

            string type = values[0];
            int p_id = Convert.ToInt32(values[1]), 
               x = Convert.ToInt32(values[2]),
               y = Convert.ToInt32(values[3]),
               param_1 = Convert.ToInt32(values[4]),
               param_2 = Convert.ToInt32(values[5]);
         }
         Console.Error.WriteLine("debug code");

         string[] actions = {"left", "right", "up", "down", "bomb"};
         Random rnd = new Random();
         int random_index  = rnd.Next(5);

         Console.WriteLine("{0}", actions[random_index]);
      }
   }
}