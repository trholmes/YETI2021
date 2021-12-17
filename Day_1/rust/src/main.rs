use md5::{Md5, Digest};

struct StrGen {
    state: Vec<i32>,
}

impl StrGen {
    fn new(statelength: u32) -> Self
    {
        let mut state = Vec::<i32>::new();
        for _i in 0..statelength {
            state.push(0);
        }
        Self {
            state,
        }
    }

    fn next(&mut self) -> String {
        let charpool = [
            "0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J",
            "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d",
            "e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
        let mut ret: String = String::from("");
        for i in 0..self.state.len() {
            ret.push_str(charpool[self.state[i] as usize]);
        }
        
        for i in 0..self.state.len(){
            if self.state[i as usize] < 61 {
                self.state[i as usize] += 1;
                break;
            } else {
                self.state[i as usize] = 0;
            }
        }
        ret
    }
}



fn main() {
    let targethash = std::fs::read_to_string("../data/targethash.txt").
        expect("Failed to read target hash file!");
    let targethash = targethash.trim();
    println!("{}", targethash); 
    let mut generator = StrGen::new(4);
    let mut run = true;
    let mut outstr: String = "".to_string();


    while run
    {
        let mut hasher = Md5::new();
        let t_string = generator.next();
        hasher.update(t_string.clone());
        let result = hasher.finalize();
        if format!("{:x}", result) == targethash
        {
            run = false;
            outstr.push_str(&t_string);
        }
    }
    println!("string with matching hash is {}", outstr)
}
