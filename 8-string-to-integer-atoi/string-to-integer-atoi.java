class Solution {
    public int myAtoi(String s) {
        String trimmedS = s.trim();
        if (trimmedS.isEmpty()) {
            return 0;
        }
        char[] s1 = trimmedS.toCharArray();
        int index = 0;
        int sign = 1;
        long result = 0;
        final int INT_MAX = 2147483647;
        final int INT_MIN = -2147483648;

        if (s1[index] == '-') {
            sign = -1;
            index++;
        } else if (s1[index] == '+') {
            index++;
        }
        for (int i = index; i < s1.length; i++) 
        {
            char c = s1[i];

            if (c < '0' || c > '9') {
                break;
            }

            int digit = c - '0';

            if (sign == 1) {
                if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > 7)) {
                    return INT_MAX;
                }
            }

            if (sign == -1) {
                long limit = (long) INT_MAX + 1; // 2147483648L
                if (result > limit / 10 || (result == limit / 10 && digit > 8)) {
                    return INT_MIN;
                }
            }

            result = result * 10 + digit;
        }
       return (int) (sign * result);
    }
}