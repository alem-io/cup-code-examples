using System;
using System.Collections.Generic;

class Demo {
   static void Main() {
      while (true) {
         string line;
      
         line = Console.ReadLine();
         int n = Convert.ToInt32(line.Split(' ')[0]);
         for (int i = 0; i < n; i++) {
            line = Console.ReadLine();
         }

         line = Console.ReadLine();
         int m = Convert.ToInt32(line);
         for (int i = 0; i < m; i++) {
            line = Console.ReadLine();
         }
         Console.Error.WriteLine("debug code");
         Console.WriteLine("{0}", "100 100 200 200");
      }
   }
}