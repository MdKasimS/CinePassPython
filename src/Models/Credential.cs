namespace CineComplex.Models
{
    public class Credential
    {
        private string? _loginId;
        private string? _password;
        //private string? _type;
        private string? _sessionTokenId;
        private static Credential? _instance;

        


        private Credential()
        {
        }

        public string? LoginId { get => _loginId; set => _loginId = value; }
        public string? Password { get => _password; set => _password = value; }
        public string? SessionTokenId { get => _sessionTokenId; set => _sessionTokenId = value; }
        public static Credential Instance
        {
            get
            {
                if (_instance == null)
                {
                    _instance = new Credential();
                }
                return _instance;

            }
        }

    }
}