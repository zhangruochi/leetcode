import os

total  = sum(1 for dir in os.listdir(".") if str(dir)[0] >="0" and str(dir)[0] <= "9")
print("you have solved: {}".format(total))



