using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Factorial
{
    internal class LongDecimal
    {
        private static readonly int M = 1000000000;
        private static readonly int MM = 2000000000;
        private List<int> innerValues;
        private bool sign;
        private int listPointer;

        public LongDecimal(int value)
        {
            if (value >= 0)
            {
                this.sign = false;
                innerValues = new List<int>();
            }
            else
            {
                value = -value;
                this.sign = true;
                innerValues = new List<int>();
            }

            if (value >= MM)
            {
                innerValues.Add(value - MM);
                innerValues.Add(2);
            }
            else if (value >= M)
            {
                innerValues.Add(value - M);
                innerValues.Add(1);
            }
            else
            {
                innerValues.Add(value);
            }
        }
        public static bool operator ==(LongDecimal firstNumber, LongDecimal secondNumber)
        {
            int firstHead = 0;
            int secondHead = 0;
            int left=0;
            int right=0;
            bool isLeftOver = false;
            bool isRightOver = false;
            while (true)
            {
                
                try
                {
                    left = firstNumber.innerValues[firstHead];
                }
                catch { isLeftOver = true; }
                try
                {
                    right = secondNumber.innerValues[secondHead];
                }
                catch { isRightOver = true; }

                if (isLeftOver && !isRightOver)
                    return false;
                if (!isLeftOver && isRightOver)
                    return false;
                if (isLeftOver && isRightOver)
                    return true;
                if (left != right)
                    return false;
                firstHead++;
                secondHead++;
            }
        }
        public static bool operator !=(LongDecimal firstNumber, LongDecimal secondNumber)
        {
            int firstHead = 0;
            int secondHead = 0;
            int left = 0;
            int right = 0;
            bool isLeftOver = false;
            bool isRightOver = false;
            while (true)
            {
                try
                {
                    left = firstNumber.innerValues[firstHead];
                }
                catch { isLeftOver = true; }
                try
                {
                    right = secondNumber.innerValues[secondHead];
                }
                catch { isRightOver = true; }

                if (isLeftOver && !isRightOver)
                    return true;
                if (!isLeftOver && isRightOver)
                    return true;
                if (isLeftOver && isRightOver)
                    return false;
                if (left != right)
                    return true;
                firstHead++;
                secondHead++;
            }
        }
        public static LongDecimal operator +(LongDecimal fisrtNumber, LongDecimal secondNumber)
        {
            if(fisrtNumber.getSign() == secondNumber.getSign())
            {
                int sgn = fisrtNumber.getSign() ? -1 : 1;
                LongDecimal newDecimal = new LongDecimal(sgn);
                int overflow = 0;
                int left = 0, right = 0, sum = 0;
                int index = 0;
                while (index < fisrtNumber.innerValues.Count || index < secondNumber.innerValues.Count)
                {
                    try
                    {
                        left = fisrtNumber.innerValues[index];
                    }
                    catch { }
                    try
                    {
                        right = secondNumber.innerValues[index];
                    }
                    catch { }
                    sum = left + right + overflow;
                    overflow = 0;
                    if (sum >= MM)
                    {
                        overflow = 2;
                        sum -= MM;
                    }
                    else if (sum >= M)
                    {
                        overflow = 1;
                        sum -= M;
                    }
                    newDecimal.setValueAt(sum, index++);
                    left = right = sum = 0;
                }
                if (overflow > 0)
                {
                    newDecimal.setValueAt(overflow, index);
                }
                return newDecimal;
            }
            else if (fisrtNumber.getSign() == true &&  secondNumber.getSign() == false)
            {
                return new LongDecimal(-1);
            }
            else if (fisrtNumber.getSign() == false && secondNumber.getSign() == true)
            {
                return new LongDecimal(-1);
            }
            return new LongDecimal(-1);
        }
        private bool addValueTo(int val, int index)
        {
            //ujemne, zła pozycja, przepełnienie
            innerValues[index] += val;
            return true;
        }
        public int getValueAt(int index)
        {
            try
            {
                return innerValues[index];
            }
            catch (Exception e)
            {
                throw e;
            }
        }
        public void setValueAt(int value, int index)
        {
            while (innerValues.Count <= index)
            {
                innerValues.Add(0);
            }
            try
            {
                innerValues[index] = value;
            }
            catch (Exception e)
            {
                throw e;
            }
        }
        public override string ToString()
        {
            int ptr = innerValues.Count-1;
            string output = "";
            output += innerValues[ptr--].ToString();
            while (ptr >= 0)
            {
                output += innerValues[ptr--].ToString().PadLeft(9, '0');
            }
            return output;
        }
        public bool getSign()
        {
            return sign;
        }
    }
}
