use hex::FromHex;
use image;

struct FibonacciGen
{
    fibnm1: i64,
    fibn: i64,
}

impl FibonacciGen
{
    fn new() -> Self
    {
        Self
        {
            fibnm1: 0,
            fibn: 1,
        }
    }
    fn next(&mut self) -> i64
    {
        let ret = self.fibn + self.fibnm1;
        self.fibnm1 = self.fibn;
        self.fibn = ret;
        ret
    }
}

fn main() {
    // handle fibonacci stuff
    let mut evenfibs = Vec::<i64>::new();
    let mut oddfibs = Vec::<i64>::new();
    evenfibs.push(0);
    oddfibs.push(1);
    let mut fibgen = FibonacciGen::new();
    while evenfibs.len() < 9 || oddfibs.len() < 6
    {
        let t_val = fibgen.next();
        if t_val % 2 == 0
        {
            evenfibs.push(t_val)
        }
        else
        {
            oddfibs.push(t_val)
        }
        
    }
    let picwidth = evenfibs[8] / oddfibs[5];
    // load the pixels as a string
    let decoded = std::fs::read_to_string("../../Day_4/data/decoded.txt").
        expect("Failed to read file!");
    let bytes: Vec<u8> = Vec::<u8>::from_hex(decoded).expect("invalid hex!");
    let picheight = bytes.len() / (3 * picwidth as usize);
    image::save_buffer_with_format(
        "../data/image-rust.jpg",
        &bytes,
        picwidth as u32,
        picheight as u32,
        image::ColorType::Rgb8,
        image::ImageFormat::Jpeg).expect("Failed to save!"
    );
}
