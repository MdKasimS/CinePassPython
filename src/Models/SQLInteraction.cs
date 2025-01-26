using CineComplex.Classes;
using CineComplex.Classes.Base;
using CineComplex.Classes.SQL;
using Microsoft.Data.Sqlite;

namespace CineComplex.Models
{
    public class SQLInteraction : ABaseSingleton<SQLInteraction>
    {
        public static CineComplexDb Db { get; set; }
        public SQLInteraction()
        {

            //Movies = new Dictionary<int,Movie>();
            //Theatres = new Dictionary<int,Theatre>();
            //Customers = new Dictionary<int,Customer>();
            //Logins = new Dictionary<int,Credential>();
            //Shows = new Dictionary<int,Show>();
            //Bookings = new Dictionary<int,Booking>();

            string basePath = AppDomain.CurrentDomain.BaseDirectory;
            string dbPath = Path.Combine(basePath, "CineComplexDatabase.db");

           

            var connection = new SqliteConnection($"Data Source={dbPath}");
            try
            {
                connection.Open();

                Db = new CineComplexDb(connection);

                Db.Database.EnsureCreated();
                Db.SaveChanges(); // Example: Display all users

            }
            catch(Exception e)
            {
                Console.Clear();
                Console.WriteLine(e.Message);
                Console.ReadKey();
            }

            LoadBookings();
            LoadCustomers();
            LoadLogins();
            LoadMovies();
            LoadShows();
            LoadTheatres();
        }
        public void Init()
        {
            Console.WriteLine("Application Started...");
        }

        public void LoadMovies()
        {
            //This method must feth all movies from Movie.csv and add them to Movies collection.
            Console.WriteLine("This will fetch Movies");
        }

        public void LoadTheatres()
        {
            //This method must fetch all theatres details from the Theatres.csv file and add them to Theatres collection.
            Console.WriteLine("This will fetch Theatres");
        }
        public void LoadCustomers()
        {
            // This mehtod should fetch all the customer details form the Login.csv fiel and add them to customers collection.
            Console.WriteLine("This will fetch Customers");
        }
        public void LoadLogins()
        {
            // This method should fetch all the login details form the Login.csv file and aad them to the Logins collection.
            Console.WriteLine("This will fetch Logins");
        }
        public void LoadShows()
        {
            // This method should fetch all the shows details from the Shopws.csv fiel and add them to the Shows collection.
            Console.WriteLine("This will fetch Shows");
        }
        public void LoadBookings()
        {
            // This method should fetch all the bookings information and ad them to the Bookings Collection.
            Console.WriteLine("This will fetch Bookings");
        }
        public void AddMovie(Movie obj)
        {
            // if obj ==null throw Null Reference Exception
            // Exception Messsage - "Movie details can't be null."
        }
        public void AddTheatre(Theatre obj)
        {
            // if obj == null thriw Null Reference Exception
            // Exception message - "Theatre details can't be null."
        }
        public void AddCustomers(Customer obj)
        {

        }
        public void AddShows(Show obj)
        {

        }
        public void AddBookings(Booking obj)
        {

        }
        public void DeleteMovie(Movie obj)
        {

        }
        public void DeleteTheatre(Theatre obj)
        {

        }
        public void DeleteCustomers(Customer obj)
        {

        }
        public void DeleteShows(Show obj)
        {

        }
        public void DeleteBookings(Booking obj)
        {

        }
        public void UpdateMovie(Movie obj)
        {

        }
        public void UpdateTheatre(Theatre obj)
        {

        }
        public void UpdateCustomers(Customer obj)
        {

        }
        public void UpdateShows(Show obj)
        {

        }
        public void UpdateBookings(Booking obj)
        {

        }
        public void SearchMovie(Movie obj)
        {

        }
        public void SearchTheatre(Theatre obj)
        {

        }
        public void SearchCustomers(Customer obj)
        {

        }
        public void SearchShows(Show obj)
        {

        }
        public void SearchBookings(Booking obj)
        {

        }
    }
}