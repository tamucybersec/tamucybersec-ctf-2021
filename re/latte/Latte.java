

import java.io.*;
public class Latte {
public static void main (String[] args) {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    try {
    String flag = br.readLine().trim();
        if (flag.length() == 17 && check_0(flag) && check_1(flag) && check_2(flag) && check_3(flag) && check_4(flag) && check_5(flag) && check_6(flag) && check_7(flag) && check_8(flag) && check_9(flag) && check_10(flag) && check_11(flag) && check_12(flag) && check_13(flag) && check_14(flag) && check_15(flag) && check_16(flag) && check_17(flag) && check_18(flag) && check_19(flag) && check_20(flag) && check_21(flag) && check_22(flag) && check_23(flag) && check_24(flag) && check_25(flag) && check_26(flag) && check_27(flag) && check_28(flag) && check_29(flag) && check_30(flag) && check_31(flag)) {
            System.out.println("That's correct!");
        } else {
            System.out.println("Sorry that isn't right :(");
        }
    } catch (IOException ioe) {
         System.out.println(ioe);
    }
}

static Boolean check_0(String flag) {return flag.charAt(1) == (2 + flag.charAt(0)) % 256;}
static Boolean check_1(String flag) {return flag.charAt(12) == (4 + flag.charAt(9)) % 256;}
static Boolean check_2(String flag) {return flag.charAt(11) == (248 + flag.charAt(14)) % 256;}
static Boolean check_3(String flag) {return flag.charAt(8) == (9 + flag.charAt(13)) % 256;}
static Boolean check_4(String flag) {return flag.charAt(5) == (18 + flag.charAt(1)) % 256;}
static Boolean check_5(String flag) {return flag.charAt(9) == (193 + flag.charAt(11)) % 256;}
static Boolean check_6(String flag) {return flag.charAt(5) == (74 + flag.charAt(6)) % 256;}
static Boolean check_7(String flag) {return flag.charAt(10) == (205 + flag.charAt(2)) % 256;}
static Boolean check_8(String flag) {return flag.charAt(8) == (1 + flag.charAt(0)) % 256;}
static Boolean check_9(String flag) {return flag.charAt(12) == (189 + flag.charAt(14)) % 256;}
static Boolean check_10(String flag) {return flag.charAt(12) == (3 + flag.charAt(10)) % 256;}
static Boolean check_11(String flag) {return flag.charAt(16) == (20 + flag.charAt(1)) % 256;}
static Boolean check_12(String flag) {return flag.charAt(16) == (22 + flag.charAt(0)) % 256;}
static Boolean check_13(String flag) {return flag.charAt(12) == (216 + flag.charAt(13)) % 256;}
static Boolean check_14(String flag) {return flag.charAt(10) == (3 + flag.charAt(6)) % 256;}
static Boolean check_15(String flag) {return flag.charAt(16) == (11 + flag.charAt(11)) % 256;}
static Boolean check_16(String flag) {return flag.charAt(3) == (6 + flag.charAt(7)) % 256;}
static Boolean check_17(String flag) {return flag.charAt(1) == (252 + flag.charAt(4)) % 256;}
static Boolean check_18(String flag) {return flag.charAt(6) == (201 + flag.charAt(8)) % 256;}
static Boolean check_19(String flag) {return flag.charAt(0) == (8 + flag.charAt(13)) % 256;}
static Boolean check_20(String flag) {return flag.charAt(5) == (14 + flag.charAt(4)) % 256;}
static Boolean check_21(String flag) {return flag.charAt(3) == (234 + flag.charAt(5)) % 256;}
static Boolean check_22(String flag) {return flag.charAt(4) == (58 + flag.charAt(9)) % 256;}
static Boolean check_23(String flag) {return flag.charAt(11) == (11 + flag.charAt(2)) % 256;}
static Boolean check_24(String flag) {return flag.charAt(4) == (6 + flag.charAt(2)) % 256;}
static Boolean check_25(String flag) {return flag.charAt(9) == (185 + flag.charAt(14)) % 256;}
static Boolean check_26(String flag) {return flag.charAt(15) == (204 + flag.charAt(2)) % 256;}
static Boolean check_27(String flag) {return flag.charAt(3) == (50 + flag.charAt(15)) % 256;}
static Boolean check_28(String flag) {return flag.charAt(15) == (185 + flag.charAt(14)) % 256;}
static Boolean check_29(String flag) {return flag.charAt(7) == (228 + flag.charAt(5)) % 256;}
static Boolean check_30(String flag) {return flag.charAt(7) == (44 + flag.charAt(15)) % 256;}
static Boolean check_31(String flag) {return 114 == (flag.charAt(11)) % 256;}

}
