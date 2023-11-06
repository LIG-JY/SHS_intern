using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SinhanSec
{
    internal class OrderInfo
    {
        private long code;
        private long price;
        private long quantity;
        private bool TickerSaved = false;

        public long Code
        {
            get { return code; }
            set 
            {
                if (value < 0 || value > 500000)
                {
                    throw new ArgumentException("Quantity must be a positive value and under 500000");
                }
                code = value;
                TickerSaved = true;
            }
        }

        public long Price
        {
            get { return price; }
            set
            {
                if (value < 0)
                {
                    throw new ArgumentException("Quantity must be a positive value");
                }
                price = value; 
            }

        }

        public long Quantity
        {
            get { return quantity; }
            set 
            {
                if (value < 0)
                {
                    throw new ArgumentException("Quantity must be a positive value");
                }
                quantity = value;
            }
        }

        public bool IsTickerSaved()
        {
            return TickerSaved;
        }

        public OrderInfo()
        {
            // 생성자
        }
    }

}
