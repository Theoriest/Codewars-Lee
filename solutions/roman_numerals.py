class RomanNumerals:
    ones = {1:"I", 4:"IV", 5:"V", 9:"IX"}
    tens = {1:"X", 4:"XL", 5:"L", 9:"XC"}
    hundreds = {1:"C", 4:"CD", 5:"D", 9:"CM"}
    thousands = {1:"M"}

    @staticmethod
    def to_roman(val: int) -> str:
        # Base case to stop recursion
        if val <= 0 or val > 3999:
            return ''

        num_length = len(str(val))
        power = 10 ** (num_length - 1)  # e.g., length 3 -> 100
        digit = val // power            # Get the leading digit (e.g., 523 // 100 = 5)
        
        roman = ""

        # Match the digit to the correct numerals based on its place value
        match num_length:
            case 1:
                if digit < 4: roman += RomanNumerals.ones[1] * digit
                elif digit == 4: roman += RomanNumerals.ones[4]
                elif digit == 5: roman += RomanNumerals.ones[5]
                elif digit < 9: roman += RomanNumerals.ones[5] + RomanNumerals.ones[1] * (digit - 5)
                elif digit == 9: roman += RomanNumerals.ones[9]
            case 2:
                if digit < 4: roman += RomanNumerals.tens[1] * digit
                elif digit == 4: roman += RomanNumerals.tens[4]
                elif digit == 5: roman += RomanNumerals.tens[5]
                elif digit < 9: roman += RomanNumerals.tens[5] + RomanNumerals.tens[1] * (digit - 5)
                elif digit == 9: roman += RomanNumerals.tens[9]
            case 3:
                if digit < 4: roman += RomanNumerals.hundreds[1] * digit
                elif digit == 4: roman += RomanNumerals.hundreds[4]
                elif digit == 5: roman += RomanNumerals.hundreds[5]
                elif digit < 9: roman += RomanNumerals.hundreds[5] + RomanNumerals.hundreds[1] * (digit - 5)
                elif digit == 9: roman += RomanNumerals.hundreds[9]
            case 4:
                roman += RomanNumerals.thousands[1] * digit

        # Find what's left of the number
        remainder = val % power

        # Recursive call: Combine current numeral with the rest of the calculated numerals
        return roman + RomanNumerals.to_roman(remainder)