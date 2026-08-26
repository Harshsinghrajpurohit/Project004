class Solution:
    def frequencySort(self, s: str) -> str:
        result=""
        freq_map={}
        for ch in s:
            freq_map[ch]=freq_map.get(ch,0)+1
        sorted_chars=sorted(freq_map.items(),key=lambda x:(-x[-1],x[0]))
        for ch,freq in sorted_chars:
            result=result+(ch*freq) 
        return result   