def roman_to_int(numeral):
    valid_chars = "IVXLCDM"
    for char in numeral:
      if char not in valid_chars:
         print("Invalid input. Use only 'I,V,X,L,C,D,M'" )
         return
         

        
    final_answer=0
    
    # Handle subtractive pairs first


    if "CM" in numeral:
        final_answer += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        final_answer += 400
        numeral = numeral.replace("CD", "")
    if "XC" in numeral:
        final_answer += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        final_answer += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        final_answer += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        final_answer +=4
        numeral = numeral.replace("IV", "")




    for i in numeral:
        

        if i == "M":
            final_answer+=1000
        if i == "D":
            final_answer+=500
        if i == "C":
            final_answer+=100
        if i == "L":
            final_answer+=50
        if i == "X":
            final_answer+=10
        if i == "V":
            final_answer+=5
        if i == "I":
            final_answer+=1 

    return final_answer

def main():
    roman_input = input("Enter Roman numeral: ").upper()
    final_answer = roman_to_int(roman_input)
    if final_answer is not None:
        print(f"The Roman numeral {roman_input} equals {final_answer}")

main()

