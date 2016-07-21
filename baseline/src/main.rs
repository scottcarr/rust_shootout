mod mandelbrot;

fn main() {
        //let size = std::env::args_os().nth(1)
        //.and_then(|s| s.into_string().ok())
        //.and_then(|n| n.parse().ok())
        //.unwrap_or(1600);
        mandelbrot::mandelbrot(160000);
}
