def modulateInputs(s):
    codeDict = {"0000": "11110","0001": "01001","0010": "10100", "0011": "10101",
            "0100": "01010", "0101": "01011", "0110": "01110", "0111": "01111",
            "1000": "10010", "1001": "10011", "1010": "10110", "1011": "10111",
            "1100": "11010", "1101": "11011", "1110": "11100", "1111": "11101"}
   
    error = "Error: Input must be in 4 bit binary"
    strBinary = s
    bin = {'0','1'}
    tset = set(strBinary)

    if len(strBinary)%4 == 0 and bin == tset or tset == {'0'} or tset == {'1'}:
        
        split_strings = []
        n  = 4
        for index in range(0, len(strBinary), n):
            split_strings.append(strBinary[index : index + n])
            
        list1 = []
        for e in split_strings:
            list1.append(codeDict.get(e))    
        
        str1 = ''.join(list1)
        return str1
    else:
        return error