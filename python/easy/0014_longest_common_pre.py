class Solution:
    """
    Solution via 2d array.

    The longest common prefix is necessarily restrictied by the length of the shortest word.
    So the first thing we do is find the shortest word and its length, then we loop through
    all the words, checking to see if each character of every word matches the corresponding
    character of the shortest word. Each time the characters all match, we increment the
    prefix length by 1. As soon as a single character from any word produces a mismatch with
    the shortest word, we stop counting, as we have found our maximum common prefix length, n.
    Now we can take any word and the first n characters will be the maximum common prefix.

    Time complexity: O(nm), n = number of words, m = length of shortest word
    Space complexity: O(nk), n = number of words, k = length of longest word
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        num_of_words = len(strs)
        if num_of_words == 1:
            return strs[0]

        min_word_len = len(strs[0])
        min_word_ind = 0
        for i in range(num_of_words):
            n = len(strs[i])
            if n < min_word_len:
                min_word_ind = i
                min_word_len = n

        if min_word_len == 0:
            return ""

        min_word = strs.pop(min_word_ind)
        max_pre = 0
        for i in range(min_word_len):
            for word in strs:
                if min_word[i] != word[max_pre]:
                    break
            else:
                max_pre += 1
                continue
            break

        result = ""
        for i in range(max_pre):
            result += min_word[i]
        return result