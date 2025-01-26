﻿using CineComplex.Classes.Base;
using CineComplex.Interfaces;
using CineComplex.ViewModels;

namespace CineComplex.Views
{
    public class ManageTicketsView : AViewBase<ManageTicketsView>, IView
    {
        private int _choice = 0;
        public int Choice { get => _choice; set => _choice = value; }

        public List<string> MenuList
        {
            get;
            set;
        }

        public void View()
        {
            Instance.LoadMenuList();

            do//main loop
            {
                Console.Clear();
                Console.WriteLine("\t----- !!! Salam Hindusthan !!! -----");
                Console.WriteLine("================================================");

                Console.WriteLine(" Manage Tickets");
                Console.WriteLine("-------------------------------------------------");

                Console.WriteLine();

                Console.WriteLine("\nMenu : ");
                Console.WriteLine("---------------");

                foreach (string instr in ManageTicketsView.Instance.MenuList)
                {
                    Console.WriteLine(instr);
                }

                Console.Write("Enter Your Choice : ");


                int.TryParse(Console.ReadLine(), out _choice);
                switch (Choice)
                {
                    case 1:
                        break;

                    case 2:
                        break;

                    case 3:
                        break;

                    case 4:
                        break;

                    case 5:
                        break;

                    case 6:
                        break;

                    default:
                        Console.WriteLine("Please enter the valid Choice .....");
                        break;
                }
            } while (Choice!= Instance.MenuList.Count);
        }

        

        public void LoadMenuList()
        {
            Instance.MenuList = new List<string>() 
            { 
                "1. Book Ticket", 
                "2. Show Shows", 
                "3. Cancel Tickets", 
                "4. Previous Bookings", 
                "5. Account", 
                "6. Exit ", 
            };
        }
    }
}

