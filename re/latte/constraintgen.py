from random import getrandbits, sample, choice
from binascii import b2a_hex

from z3 import *
from typing import Union, Dict


def prove(solver: Solver, stmt: Union[BoolRef, bool]):
    res = solver.check(Not(stmt))
    return res.r == -1


def generate_relatives(pw: Dict[BitVecRef, BitVecVal]) -> [BoolRef]:
    avail = list(pw.keys())
    rels = []
    used = {}
    for elem in pw.keys():
        used[elem] = 0
    while not all(used[elem] > 2 for elem in pw.keys()):
        rel = sample(avail, 2)
        if all(used[elem] > 2 for elem in rel):  # remove too many redundants
            continue
        used[rel[0]] += 1
        used[rel[1]] += 1
        rels.append(rel[0] == simplify(rel[1] + (pw.get(rel[0]) - pw.get(rel[1]))))

    return rels


def squeeze(solver: Solver, pw: Dict[BitVecRef, BitVecVal]) -> int:
    avail = list(pw.keys())
    count = 0
    while not prove(solver, And([sym == val for sym, val in pw.items()])):
        count += 1
        pick = choice(avail)
        avail.remove(pick)
        solver.add(pick == pw.get(pick))

    return count

def generate(password: str):
    ctx = Context()
    solver = Solver(ctx=ctx)
    bvsort = BitVecSort(8, ctx)
    pw = {}
    for i, c in enumerate(password):
        pw[BitVec(f"flag.charAt({str(i)})", bvsort, ctx)] = BitVecVal(ord(c), bvsort, ctx)
    rels = generate_relatives(pw)
    solver.add(rels)
    squeezes = squeeze(solver, pw)
    with open('Latte.java', 'w') as source:


        source.write("\n")
        source.write("""
import java.io.*;
public class Latte {
public static void main (String[] args) {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    try {
    String flag = br.readLine().trim();
        if (flag.length() == %s && %s) {
            System.out.println("That's correct!");
        } else {
            System.out.println("Sorry that isn't right :(");
        }
    } catch (IOException ioe) {
         System.out.println(ioe);
    }
}
""" % (len(password), " && ".join([f"check_{x}(flag)" for x in range(len(solver.assertions()))])))

        source.write("\n")
        for i, assertion in enumerate(solver.assertions()):
            lhs, rhs = str(assertion).split(" == ")

            source.write(f"static Boolean check_{i}(String flag) {{return {lhs} == ({rhs}) % 256;}}\n")
        source.write("\n")
        source.write("}\n")
    return 0


if __name__ == '__main__':
    extra = b2a_hex(bytearray(getrandbits(8) for _ in range(15))).decode('ascii')
    password = r"gigem{1_h34r7_z3}"
    sys.exit(generate(password))

