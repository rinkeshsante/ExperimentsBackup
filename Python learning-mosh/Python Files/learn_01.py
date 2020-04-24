# from the python mega course
# to run the entire code remove first ''' pair from code

# variables
'''var = 'hello'
print(var)'''


# numbers
'''age = int(input("enter age :"))
age = age + 20
print(age)'''


# strings
'''c= "hello there"
print(c)

r=c.replace("e",'i')
print(r)'''


# list
'''l = ["hi", 78, "j"]
print(l)
l.append(8)
print(l)'''


# touple
'''t = (6, "dgdh", 90.0)
print(t)
print(t[-1])'''


# dictionary has its own indexes
# key and value
'''d = {
    'name': 'john',
    'surname': 'smith'
    }
print(d)
print(d['name'])'''


# error handling / reducing
'''def divide(a, b):
    try:
        return a/b
    except: # or except ZeroDivisionError:
        return 'division by 0'

print(divide(7, 4))
print(divide(7, 0))'''


# function
'''

def minutes_to_hours(min=0):  # default value
    h = int(min/60)
    m = min % 60
    return h, m


print(minutes_to_hours(340))
print(minutes_to_hours())'''


# conditionals
'''
a = 5

if a < 5:
    print("less")
elif a > 5:
    print("greater")
else:
    print("equal")'''


# loops (for & while)
'''l = ["ekje",883,"jd"]

for x in l:
    print(x)

for x in range(1,15+1):
    print(x)'''

'''while True:
    ps= input('enter the password :')
    if ps == 'abc':
        print('welcome')
        break
    else:
        print('wrong password')

print("end")'''

'''l1=['james','pretty','anna']
l2=['gmail','hotmail','yaahumail','vivomail']

for i,j in zip(l1,l2):
    print(i,j)'''