use std::collections::{HashMap, HashSet};
use std::io::{Error, Write};
fn vignere_encode(key: &str, plaintext: &str, alphabet: &str) -> String
{
    let mut map_to_int = HashMap::<&str, usize>::new();
    let mut map_from_int = HashMap::<usize, &str>::new();
    let mut ret: String = String::from("");
    for i in 0..alphabet.len()
    {
        map_to_int.insert(&alphabet[i..i+1], i);
        map_from_int.insert(i, &alphabet[i..i+1]);
    }
    for i in 0..plaintext.len()
    {
        let keyint = map_to_int.get(&key[i % key.len()..i % key.len() + 1]).unwrap();
        let charint = map_to_int.get(&plaintext[i..i + 1]).unwrap();
        let outidx = (keyint + charint) % alphabet.len();
        ret.push_str(map_from_int.get(&outidx).unwrap());
    }
    ret
}

fn vignere_decode(key: &str, ciphertext: &str, alphabet: &str) -> String
{
    let mut map_to_int = HashMap::<&str, usize>::new();
    let mut map_from_int = HashMap::<usize, &str>::new();
    let mut ret: String = String::from("");
    for i in 0..alphabet.len()
    {
        map_to_int.insert(&alphabet[i..i+1], i);
        map_from_int.insert(i, &alphabet[i..i+1]);
    }
    let alphlen = alphabet.len();
    let keylen = key.len();
    for i in 0..ciphertext.len()
    {
        let keyint = map_to_int.get(&key[i % keylen..i % keylen + 1]).unwrap();
        let charint = map_to_int.get(&ciphertext[i..i+1]).unwrap();
        let mut outidx = 0 as usize;
        if keyint < charint
        {
            outidx = (charint - keyint) % alphlen;
        }
        else
        {
            outidx = (alphlen - keyint + charint) % alphlen;
        }
        let add = map_from_int.get(&outidx).unwrap();
        ret.push_str(map_from_int.get(&outidx).unwrap());
    }
    ret
}

fn main() {
    println!("Running encode decode tests to ensure correct function!");
    let encode_test_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let encode_tests = [
        // key, plaintext, ciphertext
        ["ABCDABCDABCDABCDABCDABCDABCD", "cryptoisshortforcryptography", "CSASTPKVSIQUTGQUCSASTPIUAQJB"],
        ["LIONLIONLIONLIONLIONLIONLIONLIONLIO", "thequickbrownfoxjumpsoverthelazydog", "EPSDFQQXMZCJYNCKUCACDWJRCBVRWINLOWU"]
    ];
    let mut passed = true;
    for i in encode_tests{
        let encodetest = vignere_encode(&i[0], &i[1].to_uppercase(), &encode_test_alphabet);
        let decodetest = vignere_decode(&i[0], &i[2], &encode_test_alphabet).to_uppercase();
        if encodetest != i[2]{
            println!("encode fails for {}", &i[1]);
            passed = false;
        }
        if decodetest != i[1].to_uppercase(){
            println!("decode fails for {} expected {} but got {}", &i[2], &i[1], decodetest);
            passed = false;
        }
        if !passed
        {
            panic!("Failed encode decode test, aborting");
        }
    }
    println!("Passed!! Starting the real business here");
    let encoded = std::fs::read_to_string("../secretCode.txt").
        expect("Failed to read file!");
    // we know this from the other attempt
    let key = "BIJOU";
    let alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

    let mut outputfile = std::fs::File::create("../data/decoded.txt").expect("");
    println!("Encoding!");
    let outdat = vignere_encode(&key, &encoded.to_uppercase(), &alphabet);
    println!("Writing to file!");
    write!(outputfile, "{}", outdat);
    let hexlib: [String; 16] = [
        String::from('0'), String::from('1'), String::from('2'), String::from('3'), 
        String::from('4'), String::from('5'), String::from('6'), String::from('7'),
        String::from('8'), String::from('9'), String::from('A'), String::from('B'),
        String::from('C'), String::from('D'), String::from('E'), String::from('F')];
    let mut hexchars = HashSet::<String>::from(hexlib);
    let mut allhex = true;
    for i in 0..outdat.len()
    {
        if !hexchars.contains(&outdat[i..i+1])
        {
            println!("Found non hex character!");
            allhex = false;
            break;
        }
    }
    if allhex
    {
        println!("The encoded output is all hex")
    }
}
