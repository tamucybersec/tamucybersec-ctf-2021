from z3 import *
import re

checks = """
 static Boolean check_0(String paramString) {
    return Boolean.valueOf((paramString.charAt(1) == (2 + paramString.charAt(0)) % 256));
  }
  
  static Boolean check_1(String paramString) {
    return Boolean.valueOf((paramString.charAt(12) == (4 + paramString.charAt(9)) % 256));
  }
  
  static Boolean check_2(String paramString) {
    return Boolean.valueOf((paramString.charAt(11) == (248 + paramString.charAt(14)) % 256));
  }
  
  static Boolean check_3(String paramString) {
    return Boolean.valueOf((paramString.charAt(8) == (9 + paramString.charAt(13)) % 256));
  }
  
  static Boolean check_4(String paramString) {
    return Boolean.valueOf((paramString.charAt(5) == (18 + paramString.charAt(1)) % 256));
  }
  
  static Boolean check_5(String paramString) {
    return Boolean.valueOf((paramString.charAt(9) == (193 + paramString.charAt(11)) % 256));
  }
  
  static Boolean check_6(String paramString) {
    return Boolean.valueOf((paramString.charAt(5) == (74 + paramString.charAt(6)) % 256));
  }
  
  static Boolean check_7(String paramString) {
    return Boolean.valueOf((paramString.charAt(10) == (205 + paramString.charAt(2)) % 256));
  }
  
  static Boolean check_8(String paramString) {
    return Boolean.valueOf((paramString.charAt(8) == (1 + paramString.charAt(0)) % 256));
  }
  
  static Boolean check_9(String paramString) {
    return Boolean.valueOf((paramString.charAt(12) == (189 + paramString.charAt(14)) % 256));
  }
  
  static Boolean check_10(String paramString) {
    return Boolean.valueOf((paramString.charAt(12) == (3 + paramString.charAt(10)) % 256));
  }
  
  static Boolean check_11(String paramString) {
    return Boolean.valueOf((paramString.charAt(16) == (20 + paramString.charAt(1)) % 256));
  }
  
  static Boolean check_12(String paramString) {
    return Boolean.valueOf((paramString.charAt(16) == (22 + paramString.charAt(0)) % 256));
  }
  
  static Boolean check_13(String paramString) {
    return Boolean.valueOf((paramString.charAt(12) == (216 + paramString.charAt(13)) % 256));
  }
  
  static Boolean check_14(String paramString) {
    return Boolean.valueOf((paramString.charAt(10) == (3 + paramString.charAt(6)) % 256));
  }
  
  static Boolean check_15(String paramString) {
    return Boolean.valueOf((paramString.charAt(16) == (11 + paramString.charAt(11)) % 256));
  }
  
  static Boolean check_16(String paramString) {
    return Boolean.valueOf((paramString.charAt(3) == (6 + paramString.charAt(7)) % 256));
  }
  
  static Boolean check_17(String paramString) {
    return Boolean.valueOf((paramString.charAt(1) == (252 + paramString.charAt(4)) % 256));
  }
  
  static Boolean check_18(String paramString) {
    return Boolean.valueOf((paramString.charAt(6) == (201 + paramString.charAt(8)) % 256));
  }
  
  static Boolean check_19(String paramString) {
    return Boolean.valueOf((paramString.charAt(0) == (8 + paramString.charAt(13)) % 256));
  }
  
  static Boolean check_20(String paramString) {
    return Boolean.valueOf((paramString.charAt(5) == (14 + paramString.charAt(4)) % 256));
  }
  
  static Boolean check_21(String paramString) {
    return Boolean.valueOf((paramString.charAt(3) == (234 + paramString.charAt(5)) % 256));
  }
  
  static Boolean check_22(String paramString) {
    return Boolean.valueOf((paramString.charAt(4) == (58 + paramString.charAt(9)) % 256));
  }
  
  static Boolean check_23(String paramString) {
    return Boolean.valueOf((paramString.charAt(11) == (11 + paramString.charAt(2)) % 256));
  }
  
  static Boolean check_24(String paramString) {
    return Boolean.valueOf((paramString.charAt(4) == (6 + paramString.charAt(2)) % 256));
  }
  
  static Boolean check_25(String paramString) {
    return Boolean.valueOf((paramString.charAt(9) == (185 + paramString.charAt(14)) % 256));
  }
  
  static Boolean check_26(String paramString) {
    return Boolean.valueOf((paramString.charAt(15) == (204 + paramString.charAt(2)) % 256));
  }
  
  static Boolean check_27(String paramString) {
    return Boolean.valueOf((paramString.charAt(3) == (50 + paramString.charAt(15)) % 256));
  }
  
  static Boolean check_28(String paramString) {
    return Boolean.valueOf((paramString.charAt(15) == (185 + paramString.charAt(14)) % 256));
  }
  
  static Boolean check_29(String paramString) {
    return Boolean.valueOf((paramString.charAt(7) == (228 + paramString.charAt(5)) % 256));
  }
  
  static Boolean check_30(String paramString) {
    return Boolean.valueOf((paramString.charAt(7) == (44 + paramString.charAt(15)) % 256));
  }
  
  static Boolean check_31(String paramString) {
    return Boolean.valueOf((114 == paramString.charAt(11) % 256));
  }
"""

s = Solver()
vals = [Int("var_" + str(x)) for x in range(18)]


for i in re.findall("\(paramString.charAt\(([0-9]+)\) == \(([0-9]+) \+ paramString.charAt\(([0-9]+)\)\) \% 256\)", checks):
	lhs_index, add, rhs_index = (int(x) for x in i)
	s.add(vals[lhs_index] == (add + vals[rhs_index]) % 256)

for i in re.findall("\(([0-9]+) == paramString.charAt\(([0-9]+)\) \% 256\)", checks):
	eq, rhs_index = (int(x) for x in i)
	s.add(eq == vals[rhs_index])

print(s.check())


for i in vals:
	print(chr(s.model()[i].as_long() % 256),end="")