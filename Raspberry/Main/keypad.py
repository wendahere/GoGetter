#Motor Control by Mr Wen Da, Change points to var, need to deduct points. GPIO for LED color and Motor control
# pin 2&6 used for fan5v,gnd
import time

def elseif(number):
        if ( number =="1" ):
            print("Column 1") #GPIO Motor Control
        
        elif ( number == "2"):
            print("Column 2")
        
        elif ( number == "3"):
            print("Column 3")
        
        elif ( number == "4"):
            print("Column 4")

        elif ( number == "5"):
            print("Column 5")
        

    
def switch(points):
    select = str(input("Enter Letter Followed by Number: ")) #Input Keypad, letter then number and press enter
    letter = select[0]
    number = select[1]

    
    if ( letter== 'A' and points>=100 ):
        print("Row A")
        #LEDRowA()
        elseif(number)

        
    elif ( letter== 'B' and points>=60):
        print("Row B")
        #LEDRowB()
        elseif(number)


    elif ( letter== 'C' and points>=40):
        print("Row C")
        #LEDRowC()
        elseif(number)
        
    elif (points<40):
        print ("Insufficient Points")
        
    else:
        print ("Invalid Selection")
        

while __name__ == "__main__":
    points=100
    switch(points)
    time.sleep(1)
    
    
#40,60,100 points
#def switch_col(col):
#    switcher = {
#        1: "Check pts, if enough, minus and dispense 1",
#        2: "Check pts, if enough, minus and dispense 2",
#        3: "Check pts, if enough, minus and dispense 3",
#        4: "Check pts, if enough, minus and dispense 4",
#        5: "Check pts, if enough, minus and dispense 5"
#    }
#    return switcher.get(col,"Invalid Selection")

#def keypad():
    
#    select = str(input("Enter Letter Followed by Number: "))
#    return{select}

