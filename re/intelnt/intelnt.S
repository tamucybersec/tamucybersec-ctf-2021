// Each block yields a number in t0.  Decode these as ASCII to get the flag as
// gigem{$FLAG}
// 82 73 83 67 86 -> R I S C V
// Very helpful: https://www.kvakil.me/venus/
// Flag is then gigem{riscv}

li t0, 164
srli t2, t0, 3
li t0, 21
add t1, t2, t0
slli t0, t1, 1

li t1, 1873
li t2, 301
and t0, t1, t2
xor t1, t0, t2
li t2 29
add t0, t1, t2

li t0, 86
li t1, 6
sub t2 t0, t1
li t0, 2
li t1, 0
li t3, 1
loop_start:
add t2, t2, t0
sub t0, t0, t3
bne t0, t1, loop_start
mv t0, t2

li t0, 406
srli t2, t0, 3
li t0, 2
div t1, t2, t0
li t0, 3
add t2, t1, t0
slli t1, t2, 1
li t0, 2
mul t2, t1, t0
li t1, 45
sub t0, t2, t1

li t0, 80
li t1, 43
xor t2, t0, t1
li t0, 86
srli t3, t0, 1
xor t1, t2, t3
li t2, 6
add t0, t1, t2
