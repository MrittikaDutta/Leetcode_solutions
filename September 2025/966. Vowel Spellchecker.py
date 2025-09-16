class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(w):
            return ''.join('*' if c in 'aeiou' else c for c in w)

        # 1. Exact words
        exact = set(wordlist)

        # 2. Case-insensitive map
        case_map = {}
        for w in wordlist:
            lw = w.lower()
            if lw not in case_map:
                case_map[lw] = w

        # 3. Vowel-error map
        vowel_map = {}
        for w in wordlist:
            key = devowel(w.lower())
            if key not in vowel_map:
                vowel_map[key] = w

        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
                continue
            lq = q.lower()
            if lq in case_map:
                ans.append(case_map[lq])
                continue
            vq = devowel(lq)
            if vq in vowel_map:
                ans.append(vowel_map[vq])
                continue
            ans.append("")
        return ans
