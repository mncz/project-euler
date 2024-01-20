// Largest Prime Factor

fn main() {
    let mut x = 600851475143u64;
    let mut i = 2u64;

    loop {
        if x <= 1 {
            break;
        }

        if x % i == 0 {
            x /= i;
        } else {
            i += 1;
        }
    }

    println!("{}", i);
}
