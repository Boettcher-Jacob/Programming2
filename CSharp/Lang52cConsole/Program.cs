using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lang52cConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter Radius: ");
            int rad = int.Parse(Console.ReadLine());
            double diam = rad * 2;
            double circum = rad * 2 * 3.14159;
            Console.WriteLine("Diameter: " + Math.Round(diam,3));
            Console.WriteLine("Circumference: " + Math.Round(circum, 3));
            Console.ReadKey();
        }
    }
}
