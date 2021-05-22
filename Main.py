#Say Hello
print("Welcome to Love Calculator:)")
# Enter user names
name1 = input("enter your name :\n").lower()
name2 = input("enter their name:\n").lower()
# Do some calculations
t1 = name1.count("t")
t2 = name2.count("t")
r1 = name1.count("r")
r2 = name2.count("r")
u1 = name1.count("u")
u2 = name2.count("u")
e1 = name1.count("e")
e2 = name2.count("e")

l1 = name1.count("l")
l2 = name2.count("l")
o1 = name1.count("o")
o2 = name2.count("o")
v1 = name1.count("v")
v2 = name2.count("v")
e1 = name1.count("e")
e2 = name2.count("e")

t = t1 + t2
r = r1 + r2
u = u1 + u2
e = e1 + e2

l = l1 + l2
o = o1 + o2
v = v1 + v2
e = e1 + e2

left = t+r+u+e
right = l+o+v+e

# Print The results
score = int(f"{left}{right}")
if score < 10 and score > 90 :
    print(f"Your Score is {score}, you go together like cake and mentos.")
elif score > 40 and score < 50 :
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")