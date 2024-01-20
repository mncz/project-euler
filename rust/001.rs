// Multiples of 3 or 5

fn main() {
    let mut count = 0u32;
    let mut _sum = 0u32;

    loop {
        if count == 999 {
            break;
        }

        count += 1;

        if count % 3 == 0 || count % 5 == 0 {
            _sum += count;
        }
    }

    println!("{}", _sum);
}
