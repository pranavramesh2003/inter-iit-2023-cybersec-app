

// 
// Decompiled by Procyon v0.5.36
// 

package passcheck;

public class PassCheck
{
    static final int[] lookup;
    
    public static char hash(final int n, final int n2) {
        return (char)(65 + ((n ^ n2) + n & n + n2) % 26);
    }
    
    public static void nuh() {
        System.out.println("Wrong password!");
    }
    
    public static void yuh() {
        System.out.println("Correct password!");
    }
    
    public static void check(final String s) {
        if (s.length() * 2 != PassCheck.lookup.length) {
            nuh();
            return;
        }
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) != hash(PassCheck.lookup[2 * i], PassCheck.lookup[2 * i + 1])) {
                nuh();
                return;
            }
        }
        yuh();
    }
    
    static {
        lookup = new int[] { 158, 152, 106, 153, 44, 139, 54, 67, 169, 156, 159, 192, 243, 88, 96, 189, 225, 33, 79, 3, 248, 100, 145, 14, 76, 126, 141, 224, 64, 74, 86, 55, 220, 49, 150, 71, 187, 22, 40, 162 };
    }
}

