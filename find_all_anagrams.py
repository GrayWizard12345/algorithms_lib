# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:

        
    
    def get_prime(self, letter):
        return self.primes[ord(letter) - self.a]
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or len(s) < len(p):
            return []
        
        res = list()
        l = len(p)
        
        self.a = ord('a')
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        p_hash = 1
        
        for i in p:
            p_hash *= self.primes[ord(i) - self.a]
        
        # print(p_hash)
        cur_hash = 1
        for i in range(l):
            cur_hash *= self.get_prime(s[i])
        
        for i in range(0, len(s) - l + 1):
            # print(cur_hash)
            if cur_hash == p_hash:
                res.append(i)
        
            cur_hash //= self.get_prime(s[i])
            if i+l < len(s):
                cur_hash *= self.get_prime(s[i+l])
        return res
