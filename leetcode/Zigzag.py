def convert(s: str, numRows: int):
    if numRows == 1: return s
    a = ""
    for i in range(numRows):
        for j in range(i,len(s),2*(numRows-1)):
            a+=s[j]
            if(i>0 and i<numRows-1 and j+2*(numRows-1)-2*i < len(s)):
                a+=s[j+2*(numRows-1)-2*i]
    return a

print(convert("PAYPALISHIRING",3))