from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = (n + 1) // 2  # Length of the first half (including middle character if n is odd)
        
        # 1. Count character frequencies and validate palindrome feasibility
        counts = Counter(s)
        odd_char = ""
        half_counts = {}
        
        for char, count in counts.items():
            if count % 2 != 0:
                if odd_char:
                    return ""  # More than 1 odd character -> no palindromic permutation
                odd_char = char
            half_counts[char] = count // 2

        # Helper function to construct full palindrome from the prefix of length m
        def make_palindrome(first_half: list[str]) -> str:
            if n % 2 == 1:
                # first_half has length m = (n+1)//2, where the last character is odd_char
                prefix = "".join(first_half[:-1])
                return prefix + odd_char + prefix[::-1]
            else:
                half_str = "".join(first_half)
                return half_str + half_str[::-1]

        # Helper function to get remaining available characters sorted lexicographically
        def get_sorted_remaining(avail: dict[str, int]) -> list[str]:
            res = []
            for ch in sorted(avail.keys()):
                res.extend([ch] * avail[ch])
            return res

        # 2. Check if we can make the first half EQUAL to target[:m]
        can_match = True
        curr_avail = half_counts.copy()
        
        for i in range(m):
            ch = target[i]
            if n % 2 == 1 and i == m - 1:
                if ch != odd_char:
                    can_match = False
                    break
            else:
                if curr_avail.get(ch, 0) > 0:
                    curr_avail[ch] -= 1
                else:
                    can_match = False
                    break

        if can_match:
            cand = make_palindrome(list(target[:m]))
            if cand > target:
                return cand

        # 3. Try to diverge from target[:m] at index i (0 <= i < m) by choosing a strictly larger character
        for i in range(m - 1, -1, -1):
            avail = half_counts.copy()
            prefix = list(target[:i])
            
            valid_prefix = True
            for idx in range(i):
                ch = target[idx]
                if n % 2 == 1 and idx == m - 1:
                    if ch != odd_char:
                        valid_prefix = False
                        break
                else:
                    if avail.get(ch, 0) > 0:
                        avail[ch] -= 1
                    else:
                        valid_prefix = False
                        break
            
            if not valid_prefix:
                continue

            target_char = target[i]
            
            if n % 2 == 1 and i == m - 1:
                if odd_char > target_char:
                    prefix.append(odd_char)
                    cand = make_palindrome(prefix)
                    if cand > target:
                        return cand
            else:
                for ch in sorted(avail.keys()):
                    if ch > target_char and avail[ch] > 0:
                        avail[ch] -= 1
                        prefix.append(ch)
                        prefix.extend(get_sorted_remaining(avail))
                        if n % 2 == 1:
                            prefix.append(odd_char)
                        cand = make_palindrome(prefix)
                        if cand > target:
                            return cand

        return ""