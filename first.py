import time


print("WELCOME TO PERSONALITY TEST")
print("*"*60)
name= input("Enter your name")
age=int(input("Enter your age"))
age2=age*12
city=input("City you live in:")
food=input("Your favourite food")
color=input("Your favorite color")
animal=input("Your spirit animal")
hobby=input("One thing you love doing:")
if age < 18:
    tribe="Young Explorer"
elif age >=18 & age <=30:
    tribe="Adventurer"
else: 
    tribe="Wise Owl"
code=name[:2].upper() + animal.title() + color.title()

print("generating your personality....")
print("*"*60)
time.sleep(5) 
print(f"You're from {city} , a place of dreams!")
print(f"You love {food} and enjoy doing {hobby}")
print(f"You vibe with the color {color} and your spirit animal is {animal}")
print(f"You've lived approximately {age2} months already")
print(f"You belong to the {tribe} tribe")
print(f"Your Secret Personality Code is:{code} ")