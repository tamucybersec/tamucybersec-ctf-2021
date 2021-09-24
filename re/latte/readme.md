# latte

Hey I found this file when I was picking up my coffee this morning. It seems to take a flag and check if it's correct. Maybe you can do something with it?

hint: https://ericpony.github.io/z3py-tutorial/guide-examples.htm

## solution

### Java
This is clearly a .class file so putting it into JavaDecompiler we get the following code

```Java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Latte {
  public static void main(String[] paramArrayOfString) {
    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
    try {
      String str = bufferedReader.readLine().trim();
      if (str.length() == 18 && check_0(str).booleanValue() && check_1(str).booleanValue() && check_2(str).booleanValue() && check_3(str).booleanValue() && check_4(str).booleanValue() && check_5(str).booleanValue() && check_6(str).booleanValue() && check_7(str).booleanValue() && check_8(str).booleanValue() && check_9(str).booleanValue() && check_10(str).booleanValue() && check_11(str).booleanValue() && check_12(str).booleanValue() && check_13(str).booleanValue() && check_14(str).booleanValue() && check_15(str).booleanValue() && check_16(str).booleanValue() && check_17(str).booleanValue() && check_18(str).booleanValue() && check_19(str).booleanValue() && check_20(str).booleanValue() && check_21(str).booleanValue() && check_22(str).booleanValue() && check_23(str).booleanValue() && check_24(str).booleanValue() && check_25(str).booleanValue() && check_26(str).booleanValue() && check_27(str).booleanValue() && check_28(str).booleanValue() && check_29(str).booleanValue() && check_30(str).booleanValue() && check_31(str).booleanValue() && check_32(str).booleanValue() && check_33(str).booleanValue() && check_34(str).booleanValue() && check_35(str).booleanValue() && check_36(str).booleanValue()) {
        System.out.println("That's correct!");
      } else {
        System.out.println("Sorry that isn't right :(");
      } 
    } catch (IOException iOException) {
      System.out.println(iOException);
    } 
  }
  
  static Boolean check_0(String paramString) {
    return Boolean.valueOf((paramString.charAt(7) == (200 + paramString.charAt(2)) % 256));
  }
  
  static Boolean check_1(String paramString) {
    return Boolean.valueOf((paramString.charAt(2) == (10 + paramString.charAt(14)) % 256));
  }
  
  static Boolean check_2(String paramString) {
    return Boolean.valueOf((paramString.charAt(17) == (73 + paramString.charAt(11)) % 256));
  }
  
  static Boolean check_3(String paramString) {
    return Boolean.valueOf((paramString.charAt(12) == (10 + paramString.charAt(9)) % 256));
  }
  
  static Boolean check_4(String paramString) {
    return Boolean.valueOf((paramString.charAt(9) == (9 + paramString.charAt(14)) % 256));
  }
  
  static Boolean check_5(String paramString) {
    return Boolean.valueOf((paramString.charAt(7) == (180 + paramString.charAt(17)) % 256));
  }
  
  static Boolean check_6(String paramString) {
    return Boolean.valueOf((paramString.charAt(8) == (46 + paramString.charAt(7)) % 256));
  }
  
  static Boolean check_7(String paramString) {
    return Boolean.valueOf((paramString.charAt(12) == (65 + paramString.charAt(7)) % 256));
  }
  
  static Boolean check_8(String paramString) {
    return Boolean.valueOf((paramString.charAt(6) == (19 + paramString.charAt(9)) % 256));
  }
  
  static Boolean check_9(String paramString) {
    return Boolean.valueOf((paramString.charAt(14) == (253 + paramString.charAt(0)) % 256));
  }
  
  static Boolean check_10(String paramString) {
    return Boolean.valueOf((paramString.charAt(8) == (246 + paramString.charAt(2)) % 256));
  }
  
  static Boolean check_11(String paramString) {
    return Boolean.valueOf((paramString.charAt(13) == (196 + paramString.charAt(5)) % 256));
  }
  
  static Boolean check_12(String paramString) {
    return Boolean.valueOf((paramString.charAt(2) == (239 + paramString.charAt(15)) % 256));
  }
  
  static Boolean check_13(String paramString) {
    return Boolean.valueOf((paramString.charAt(5) == (66 + paramString.charAt(7)) % 256));
  }
  
  static Boolean check_14(String paramString) {
    return Boolean.valueOf((paramString.charAt(15) == (22 + paramString.charAt(3)) % 256));
  }
  
  static Boolean check_15(String paramString) {
    return Boolean.valueOf((paramString.charAt(8) == (46 + paramString.charAt(7)) % 256));
  }
  
  static Boolean check_16(String paramString) {
    return Boolean.valueOf((paramString.charAt(16) == (202 + paramString.charAt(2)) % 256));
  }
  
  static Boolean check_17(String paramString) {
    return Boolean.valueOf((paramString.charAt(0) == (240 + paramString.charAt(12)) % 256));
  }
  
  static Boolean check_18(String paramString) {
    return Boolean.valueOf((paramString.charAt(8) == (44 + paramString.charAt(10)) % 256));
  }
  
  static Boolean check_19(String paramString) {
    return Boolean.valueOf((paramString.charAt(5) == paramString.charAt(1) % 256));
  }
  
  static Boolean check_20(String paramString) {
    return Boolean.valueOf((paramString.charAt(7) == (183 + paramString.charAt(15)) % 256));
  }
  
  static Boolean check_21(String paramString) {
    return Boolean.valueOf((paramString.charAt(1) == (64 + paramString.charAt(10)) % 256));
  }
  
  static Boolean check_22(String paramString) {
    return Boolean.valueOf((paramString.charAt(4) == (3 + paramString.charAt(0)) % 256));
  }
  
  static Boolean check_23(String paramString) {
    return Boolean.valueOf((paramString.charAt(9) == (3 + paramString.charAt(4)) % 256));
  }
  
  static Boolean check_24(String paramString) {
    return Boolean.valueOf((paramString.charAt(6) == (1 + paramString.charAt(15)) % 256));
  }
  
  static Boolean check_25(String paramString) {
    return Boolean.valueOf((paramString.charAt(16) == (252 + paramString.charAt(13)) % 256));
  }
  
  static Boolean check_26(String paramString) {
    return Boolean.valueOf((paramString.charAt(16) == (207 + paramString.charAt(3)) % 256));
  }
  
  static Boolean check_27(String paramString) {
    return Boolean.valueOf((paramString.charAt(11) == (213 + paramString.charAt(8)) % 256));
  }
  
  static Boolean check_28(String paramString) {
    return Boolean.valueOf((paramString.charAt(4) == (242 + paramString.charAt(5)) % 256));
  }
  
  static Boolean check_29(String paramString) {
    return Boolean.valueOf((paramString.charAt(10) == (212 + paramString.charAt(8)) % 256));
  }
  
  static Boolean check_30(String paramString) {
    return Boolean.valueOf((paramString.charAt(0) == (254 + paramString.charAt(3)) % 256));
  }
  
  static Boolean check_31(String paramString) {
    return Boolean.valueOf((paramString.charAt(13) == (216 + paramString.charAt(14)) % 256));
  }
  
  static Boolean check_32(String paramString) {
    return Boolean.valueOf((paramString.charAt(8) == (43 + paramString.charAt(11)) % 256));
  }
  
  static Boolean check_33(String paramString) {
    return Boolean.valueOf((paramString.charAt(17) == (25 + paramString.charAt(3)) % 256));
  }
  
  static Boolean check_34(String paramString) {
    return Boolean.valueOf((paramString.charAt(6) == (72 + paramString.charAt(16)) % 256));
  }
  
  static Boolean check_35(String paramString) {
    return Boolean.valueOf((paramString.charAt(1) == (246 + paramString.charAt(17)) % 256));
  }
  
  static Boolean check_36(String paramString) {
    return Boolean.valueOf((114 == paramString.charAt(12) % 256));
  }
}
```

This is a perfect situation for Z3. **YES I FINALLY GET TO LEARN HOW TO USE IT CORRECTLY**

### Python
Just yeet that bitch into Z3 and... Oh we get bad numbers.
Add a few more constraints and here's the solution code

```Python
from z3 import *

s = Solver()

p = IntVector('p', 18)
for i in range(18):
    s.add(p[i] > 31)
    s.add(p[i] < 128)

s.add(p[0] == ord("b"))

s.add(p[7] == (200 + p[2])%256)
s.add(p[2] == (10 + p[14])%256)
s.add(p[17] == (73 + p[11])%256)
s.add(p[12] == (10 + p[9])%256)
s.add(p[9] == (9 + p[14])%256)
s.add(p[7] == (180 + p[17])%256)
s.add(p[8] == (46 + p[7])%256)
s.add(p[12] == (65 + p[7])%256)
s.add(p[6] == (19 + p[9])%256)
s.add(p[14] == (253 + p[0])%256)
s.add(p[8] == (246 + p[2])%256)
s.add(p[13] == (196 + p[5])%256)
s.add(p[2] == (239 + p[15])%256)
s.add(p[5] == (66 + p[7])%256)
s.add(p[15] == (22 + p[3])%256)
s.add(p[8] == (46 + p[7])%256)
s.add(p[16] == (202 + p[2])%256)
s.add(p[0] == (240 + p[12])%256)
s.add(p[8] == (44 + p[10])%256)
s.add(p[5] == (p[1])%256)
s.add(p[7] == (183 + p[15])%256)
s.add(p[1] == (64 + p[10])%256)
s.add(p[4] == (3 + p[0])%256)
s.add(p[9] == (3 + p[4])%256)
s.add(p[6] == (1 + p[15])%256)
s.add(p[16] == (252 + p[13])%256)
s.add(p[16] == (207 + p[3])%256)
s.add(p[11] == (213 + p[8])%256)
s.add(p[4] == (242 + p[5])%256)
s.add(p[10] == (212 + p[8])%256)
s.add(p[0] == (254 + p[3])%256)
s.add(p[13] == (216 + p[14])%256)
s.add(p[8] == (43 + p[11])%256)
s.add(p[17] == (25 + p[3])%256)
s.add(p[6] == (72 + p[16])%256)
s.add(p[1] == (246 + p[17])%256)

if s.check():
    m = s.model()
    for i in range(18):
        print(m[p[i]], end=" ")
```

Yeeting the output into CyberChef we get the flag : `bsides{1_h34r7_z3}`