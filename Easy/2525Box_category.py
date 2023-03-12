def categorizeBox(self, length, width, height, mass):
        volume = length * width * height

        if((length>=10000 or width>=10000 or height>=10000 or volume>= 1000000000) and mass>=100):
            return "Both"
        elif(length>=10000 or width>=10000 or height>=10000 or volume>= 1000000000):
            return "Bulky"
        elif(mass>=100):
            return "Heavy"
        else:
            return "Neither"
        
        # Passed