#[no_mangle]
pub fn _g(s: u64) {
    match s {
        0 => _i(s + 1),
        2 => _e(s + 1),
        28 => _g(s + 1),
        29 => _3(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _i(s: u64) {
    match s {
        1 => _g(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _e(s: u64) {
    match s {
        3 => _m(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _m(s: u64) {
    match s {
        4 => _open_curly(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _open_curly(s: u64) {
    match s {
        5 => _1(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _1(s: u64) {
    match s {
        6 => __(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn __(s: u64) {
    match s {
        7 => _h(s + 1),
        12 => _y(s + 1),
        16 => _u(s + 1),
        21 => _4(s + 1),
        23 => _d(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _h(s: u64) {
    match s {
        8 => _0(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _0(s: u64) {
    match s {
        9 => _p(s + 1),
        14 => _u(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _p(s: u64) {
    match s {
        10 => _3(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _3(s: u64) {
    match s {
        11 => __(s + 1),
        19 => _d(s + 1),
        25 => _b(s + 1),
        30 => _r(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _y(s: u64) {
    match s {
        13 => _0(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _u(s: u64) {
    match s {
        15 => __(s + 1),
        17 => _s(s + 1),
        27 => _g(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _s(s: u64) {
    match s {
        18 => _3(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _d(s: u64) {
    match s {
        20 => __(s + 1),
        24 => _3(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _4(s: u64) {
    match s {
        22 => __(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _b(s: u64) {
    match s {
        26 => _u(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _r(s: u64) {
    match s {
        31 => _close_curly(s + 1),
        _ => unreachable!(),
    }
}
#[no_mangle]
pub fn _close_curly(s: u64) {
    done();
}

#[no_mangle]
pub fn done() {
    println!("Have a nice day!");
}
pub fn main() {
    _g(0);
}