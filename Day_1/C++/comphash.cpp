#include <openssl/md5.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <map>
#include <sstream>
#include <boost/format.hpp>

// how long is the hashed value?
const int pwd_length = 4;

// pool of characters for making guesses
const char *charpool = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

struct strgen
{
    int state[pwd_length];
    strgen(){
        for(int i = 0; i < pwd_length; i++) {
            state[i] = 0;
        }
    };

    std::string next() {
        std::string ret = "";
        for(int i = 0; i < pwd_length; i++) {
            ret += charpool[state[i] % 62];
        }
        for(int i = 0; i < pwd_length; i++){
            if (state[i] < 61) {
                state[i] += 1;
                break;
            } else {
                state[i] = 0;
            }
        }
        return ret;
    };
};

int main(void) {
    std::string targetstr;
    // get the target hash from the file
    { 
        std::ifstream ifs("../data/targethash.txt");
        targetstr.assign( (std::istreambuf_iterator<char>(ifs) ), 
                                    (std::istreambuf_iterator<char>()    ) );
        ifs.close();
    }
    
    // generator for combinations
    strgen generator = strgen();
    std::string t_str = generator.next();
    std::string first;
    for(int i = 0; i < pwd_length; i++){
        first.push_back(t_str[i]);
    }
    unsigned char hash[MD5_DIGEST_LENGTH];
    while(true){
        MD5((unsigned char *)t_str.c_str(), pwd_length, hash);
        // this lovely mess can be blamed on my compiler not recognizing std::format()
        std::string hashstr = (boost::format("%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x")%
            (int)hash[0]%(int)hash[1]%(int)hash[2]%(int)hash[3]%
            (int)hash[4]%(int)hash[5]%(int)hash[6]%(int)hash[7]%
            (int)hash[8]%(int)hash[9]%(int)hash[10]%(int)hash[11]%
            (int)hash[12]%(int)hash[13]%(int)hash[14]%(int)hash[15]).str();
        //std::cout << hashstr << std::endl;
        if (hashstr.compare(targetstr) == 0) {   
            break;
        }
        // do after the loop body so that we can store it before the initial loop
        t_str = generator.next();
        // a little bit of insurance to prevent infinite loops
        // could probably store this on the generator though
        if (t_str.compare(first) == 0) {
            std::cout << "failed to find hash" << std::endl;
            return -1;
        }
    }
       
    std::cout << "The string with the hash " << targetstr << " is " << t_str << std::endl;
    
}