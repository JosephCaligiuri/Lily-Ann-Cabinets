

class Halo: 

    def drive(motor, duty): # Motor: FL - Front Left, FR - Front Right, BL - Back Left, BR - Back Right | duty - motor speed, -1 to 1
        if motor == "FL" or "BL":
            print("Left")
            
        elif motor == "FR" or "BR":
            print("right")
        else:
            print("Motors Not Found")