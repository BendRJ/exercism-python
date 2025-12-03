class PhoneNumber:
    def __init__(self, input_no: str):
        self.number = input_no # triggers number setter if specified

    @property
    def number(self):
        return self._number #getter
    
    @number.setter
    def number(self, value):
        """
        Setter for the initialized phone number. Does formatting and validation checks.
        """
        chars_to_remove = [" ", "-", ".", "(", ")"]
        cleaned = value.strip().strip("+")
        for char in chars_to_remove:
            cleaned = cleaned.replace(char, "")
        if any(char for char in cleaned if char in ("@",":","!")):
            raise ValueError("punctuations not permitted")
        if any(char for char in cleaned if not char.isdigit()):
            raise ValueError("letters not permitted")
        if len(cleaned) < 10: 
            raise ValueError("must not be fewer than 10 digits")
        if len(cleaned) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(cleaned) == 11 and not cleaned.startswith("1"):
            raise  ValueError("11 digits must start with 1")
        if len(cleaned) == 11 and cleaned.startswith("1"):
            cleaned = cleaned[1:]

        if cleaned[0] in "01":
            raise ValueError("area code cannot start with zero" if cleaned[0] == "0" else "area code cannot start with one")
        if cleaned[3] in "01":
            raise ValueError("exchange code cannot start with zero" if cleaned[3] == "0" else "exchange code cannot start with one")
        
        self._number = cleaned  # if the setter tried to set `self.number` it would call itself indefinitely; 'number' is NOT in __dict__ only '_number' is: {'_number': '2234567890'}
    
    def pretty(self):
        """
        Method to apply uniform format to given NANP phone number.
        """
        area_code = self._number[:3]
        exchange_code = self._number[3:6]
        residual = self._number[6:]

        return f"({area_code})-{exchange_code}-{residual}"
        
    @property
    def area_code(self):
        """
        Return area code of given NANP phone number.
        """
        return self._number[:3]

if __name__ == "__main__":
    test1 = PhoneNumber("12234567890")
    print(test1.__dict__)
    print(test1.number)
    print(test1.area_code)
    print(test1.pretty())