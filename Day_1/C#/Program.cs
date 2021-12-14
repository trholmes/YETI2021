using System;
using System.Net;
using System.Text.RegularExpressions;

namespace C_comphash
{
    class Program {
        const string charpool = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
        const int pwd_length = 4;
        class strgen {
            int[] state;
            public strgen(){
                state = new int[pwd_length];           
            }
            public string next() {
                string ret = "";
                for(int i = 0; i < pwd_length; i++) {
                    ret += charpool[state[i] % 62];
                }
                for(int i = 0; i < pwd_length; i++){
                    if (state[i] < 62) {
                        state[i] += 1;
                        break;
                    } else {
                        state[i] = 0;
                    }
                }
                return ret;
            }
        }
        static void Main(string[] args) {
            // get the target hash from file
            string target_hash = System.IO.File.ReadAllText("../data/targethash.txt");
            Console.WriteLine(target_hash);

            // use this to generate possible strings
            strgen generator = new strgen();
            string t_string;

            // hashing object
            var MD5 = System.Security.Cryptography.MD5.Create();

            System.Text.StringBuilder sb = new System.Text.StringBuilder();
            byte[] t_bytes;
            byte[] hashed;
            // now compute hashes and test
            while(true){
                t_string = generator.next();
                t_bytes = System.Text.Encoding.ASCII.GetBytes(t_string);
                hashed = MD5.ComputeHash(t_bytes);

                // convert the hashed bytes into a string
                // splits the bytes into low and high nibbles
                for (int i = 0; i < hashed.Length; i++) {
                    sb.Append(hashed[i].ToString("x2"));
                }
                if (sb.ToString().Equals(target_hash)) {
                    break;
                }
                sb.Clear();
            }

            // echo what we found
            Console.WriteLine($"String with the given hash {target_hash} is {t_string}");
            // download the final url 
            WebClient client = new WebClient();
            string htmlstring = client.DownloadString($"https://tiny.utk.edu/{t_string}");
            System.IO.File.WriteAllText("page.html", htmlstring);

            // we know it's a gist based on the HTML we got, let's get the raw address
            Regex regex = new Regex("href=\"(.+raw.+?)\"", RegexOptions.Compiled | RegexOptions.IgnoreCase);
            string matchstr = "";
            foreach(Match match in regex.Matches(htmlstring))
            {
                matchstr += match.Groups[1].Value;
            }
            client.DownloadFile($"https://gist.github.com/{matchstr}", "FourVectorTest.csv");
        }
    }
}
