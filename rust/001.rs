// Multiples of 3 or 5

fn main() {
    let mut _sum = 0u32;

    for i in 1..1000 {
        if i % 3 == 0 || i % 5 == 0 {
            _sum += i;
        }
    }

    println!("{}", _sum);
}
