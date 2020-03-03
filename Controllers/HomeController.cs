using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using WebApplication1.Models;

namespace WebApplication1.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            return View();
        }
        public IActionResult Menu()
        {
            string[] food_items = new string[20];
            string fileContents = System.IO.File.ReadAllText(@"C:\Users\theja\Desktop\a.txt");
            var i = 0;
            var k = 0;
            var day = 3;
            foreach (string dataLine in fileContents.Split('\n'))
            {
                food_items[i] = dataLine;
                i++;
            }
            i -= 1;
            int[] presentDay = new int[3];
            int[] pastDay = new int[3];
            int[] week = new int[21];
            string[] foodMenu = new string[21];
            presentDay = Match(food_items);
            week[0] = presentDay[0];
            week[1] = presentDay[1];
            week[2] = presentDay[2];
            while (day != 21)
            {
                pastDay = presentDay;
                presentDay = Match(food_items);
                while (presentDay[0] == presentDay[1] || presentDay[2] == presentDay[0] || presentDay[0] == pastDay[0] || presentDay[0] == pastDay[1] || presentDay[0] == pastDay[2])
                {
                    presentDay[0] += 1;
                    if (presentDay[0] > food_items.Length - 1)
                        presentDay[0] = 0;
                }
                week[day++] = presentDay[0];
                while (presentDay[0] == presentDay[1] || presentDay[2] == presentDay[1] || presentDay[1] == pastDay[0] || presentDay[1] == pastDay[1] || presentDay[1] == pastDay[2])
                {
                    presentDay[1] += 1;
                    if (presentDay[1] > food_items.Length - 1)
                        presentDay[1] = 0;
                }
                week[day++] = presentDay[1];
                while (presentDay[2] == presentDay[1] || presentDay[2] == presentDay[0] || presentDay[2] == pastDay[0] || presentDay[2] == pastDay[1] || presentDay[2] == pastDay[2])
                {
                    presentDay[2] += 1;
                    if (presentDay[2] > food_items.Length - 1)
                        presentDay[2] = 0;
                }
                week[day++] = presentDay[2];
            }
            foreach (int no in week)
            {
                foodMenu[k] = food_items[no];
                k++;
            }
            return View(foodMenu);
        }
        public int[] Match(string[] i)
        {
            Random rand = new Random();
            var x = rand.Next(i.Length);
            var y = rand.Next(i.Length);
            var z = rand.Next(i.Length);
            while (y == x)
                y = rand.Next(i.Length);
            while (y == z || x == z)
                z = rand.Next(i.Length);
            int[] week = new int[3];
            week[0] = x;
            week[1] = y;
            week[2] = z;
            return (week);
        }
        [HttpGet]
        public IActionResult Food(string new_food)
        {
            string[] food_items = new string[100];
            //string new_food = Request["new_data"];
            string line = new_food;
            string fileContents = System.IO.File.ReadAllText(@"C:\Users\theja\Desktop\a.txt");
            using (StreamWriter outputFile = new StreamWriter(@"C:\Users\theja\Desktop\a.txt", true))
                outputFile.WriteLine(line);

            return View("Food");
        }
        public IActionResult Example(string Name)
        {
            UserRLModel cos = new UserRLModel();
            string root = @"C:\Users\theja\Desktop\a.txt";
            string[] food_items = new string[20];
            string fileContents = System.IO.File.ReadAllText(@"C:\Users\theja\Desktop\a.txt");
            var i = 0;
            foreach (string dataLine in fileContents.Split('\n'))
            {
                food_items[i] = dataLine;
                i++;
            }
            using (StreamWriter sw = new StreamWriter(root, true))
            { 
                foreach(string st in food_items)
                    sw.WriteLine(i);
            };
            using (StreamWriter sw = new StreamWriter(root, true))
                sw.WriteLine(Name);
            return View();
        }
        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
