class Solution {
public:
    int lengthOfLastWord(string s) {
        int count = 0; // Counter for the length of the current word
        int lastWordLength = 0; // Length of the last word found

        // Loop through the string character by character
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] != ' ') { 
                // If the current character is not a space, increment the count
                count++;
            } else if (count > 0) { 
                // If we encounter a space and count is not zero,
                // it means we have finished a word
                lastWordLength = count; // Update the length of the last word
                count = 0; // Reset the count for the next word
            }
        }
        
        // If the last word is not followed by a space, count will be the length of the last word
        if (count > 0) {
            lastWordLength = count;
        }

        return lastWordLength;
    }
};
