import sys

def modulateInputs(inputBinary):
    conv4B5Bdict = {"0000" : "11110", 
                    "0100" : "01010", 
                    "1000" : "10010", 
                    "1100" : "11010",
                    "0001" : "01001",
                    "0101" : "01011",
                    "1001" : "10011",
                    "1101" : "11011",
                    "0010" : "10100",
                    "0110" : "01110",
                    "1010" : "10110", 
                    "1110" : "11100",
                    "0011" : "10101", 
                    "0111" : "01111", 
                    "1011" : "10111", 
                    "1111" : "11101"}
    
    
    
    if len(inputBinary) % 4 != 0 or inputBinary == "":
        print("Error: Input must be in 4 bit binary")
        sys.exit()
        
    for digit in inputBinary:
        if digit != "1" and digit != "0":
            print("Error: Input must be in 4 bit binary")
            sys.exit()
            
    listOf4B = [inputBinary[i:i+4] for i in range(0, len(inputBinary), 4)]
    
    
    outputBinary = ""
    for nibble in listOf4B:
        outputBinary += conv4B5Bdict[nibble]
       
        
    
    return outputBinary
    
