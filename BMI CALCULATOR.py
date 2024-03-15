##BMI CALCULATOR

Height= float(input("Enter weight in Kg:"))
Weight= float(input("Enter height in Meter:")) ##as integers they are not as precise as floats

   
BMI= Weight / (Height**2)
print("Your BMI is:",BMI)

if BMI <= 18.5:
        print("You are underweight.")

elif BMI <=25:
        print("You have normal weight.")    

elif BMI <=29:
        print("You are overweight.")
        
else:
        print("Obese")
