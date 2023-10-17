# define a class with an initialize 
# set of parameters 

#import sys 
import sys 

class PolarBear:
    # a class for geometric shapes 

    def __init__(self, arm_length , leg_length, neyes, has_tail, is_furry):
        self.arm_length   = arm_length 
        self.leg_length   = leg_length
        self.num_eyes   = neyes
        self.has_tail   = has_tail
        self.is_furry   = is_furry


    def Describe(self):
        print(f"Arm Length: = {self.arm_length} meters")
        print(f"Leg Length: = {self.leg_length} meters")
        print(f"Number of eyes = {self.num_eyes}")
        print(f"Has tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is furry: {'Yes' if self.is_furry else 'No'}")

def main():
    bear = PolarBear(0.7, 1.2, 2, True, True)
    bear.Describe()

if __name__ == "__main__":
    main()
