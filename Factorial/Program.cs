using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Factorial
{
    class Program
    {
        static void Main(string[] args)
        {
            LongDecimal a = new LongDecimal(200);
            LongDecimal b = new LongDecimal(500);
            LongDecimal c = new LongDecimal(2000000200);
            LongDecimal d = new LongDecimal(2000100200);
            for (int i = 0; i < 100050; i++)
            {
                c += c;
                Console.Out.WriteLine(c);
            }

            Console.ReadLine();
        }
    }
}
