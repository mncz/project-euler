// Even Fibonacci Numbers

fn main() {
    let mut a = 1u32;
    let mut b = 1u32;
    let mut _sum = 0u32;
    
    loop {
        let c = a + b;
        a = b;
        b = c;

        if c > 4000000 {
            break;
        } else if c % 2 == 0 {
            _sum += c;
        }
    }

    println!("{}", _sum);
}
