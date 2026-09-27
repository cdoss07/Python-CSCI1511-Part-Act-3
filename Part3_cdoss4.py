"This is for participation activity 3 and it adds a class onto Lab 1"



class UPCValidator:
    def __init__(self, barcode):
        self.barcode = barcode

    def validate(self):
        if len(self.barcode) !=12:
                print("INVALID UPC BARCODE")
        else:
            upc_core = self.barcode[:-1]
            upc_odd = 0
            upc_even = 0
            check_digit = int(self.barcode[-1])
            
            for x, place in enumerate(upc_core):
                digit = int(place)
                if x % 2 == 0:
                    upc_odd += digit
                else:
                    upc_even += digit
            upc_sum = (upc_odd * 3) + upc_even
            upc_mod = upc_sum % 10
            upc_valid = 10 - upc_mod
            if upc_valid == 10:
                upc_valid = 0
            report = f"The first 11 digits are '{upc_core}'\nThe check digit is '{check_digit}'\nCalculating...\nThe expected check digit is {upc_valid}."
            if upc_valid == check_digit:
                print(report +" This UPC is VALID.")
            else:
                print(report + " This UPC is INVALID.")

upc_input = input("Enter a 12 digit UPC-A Barcode ")

validator = UPCValidator(upc_input)

validator.validate()
        