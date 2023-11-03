class Solution():
    # sorting: compare the strings by sorting -> O(n**2)
    def is_anagram_sort(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_sorted = sorted(s)
        t_sorted = sorted(t)
        if s_sorted == t_sorted:
            return True
        return False

    # hashtable: store the occurence of each element in the string and compare -> O(n)
    def is_anagram_hashtable(self, s:str, t:str) -> bool:
        count_s = {}
        count_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        if count_s ==  count_t:
            return True
        return False

if __name__ == "__main__":
    s = input()
    t = input()
    main = Solution()
    print(main.is_anagram_hashtable(s, t))
