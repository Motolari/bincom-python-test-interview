#APPLICANT NAME: TIRENIOLUWA MOTOLARI MALAOLU
#Thank you for this great opportunity.
#I used Visual Studio Code as my IDE.

import re #i used this to pull the days and colors out of the html table
import random #this is used for question 8
import statistics #i used this to calculate the statistcial calculations
from collections import Counter #i used this to get the colour frequencies


#loading and parsing the html code
html = open("colours_of_shirts.html").read()
rows = re.findall(r"<td>(MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY)</td>\s*<td>(.*?)</td>", html, re.S)

colours = [] #creating a list
for day, cell in rows: #for loop
    colours += [c.strip() for c in cell.split(",")] 

#cleaning the typos in the data given
fix = {"BLEW": "BLUE", "ARSH": "ASH"} #there was a typo on the website/html script,I then converted "blew" to "blue" and "arsh" to "Ash" as seen in this line of code.
colours = [fix.get(c, c) for c in colours] #this is to rebuilt the colours list with the typos I have corrected 

freq = Counter(colours) #this is so i can count each color in the list and get the frequency of each color
print("Frequencies:", dict(freq))

#Solving Question 1
# mean frequency, then the colour whose frequency is closest to it
mean_freq = sum(freq.values()) / len(freq) #this holds each colour and how many times it appeared, but the mean is 8.64 
mean_colour = min(freq, key=lambda c: abs(freq[c] - mean_freq)) #the mean is 8.64 and no colour holds this frequency, so I made this line of code pick out the colour that has th closest frequency to the mean
print("1. Mean frequency = %.2f, mean colour = %s" % (mean_freq, mean_colour))

#Solving Question 2
print("2. Most worn colour:", freq.most_common(1)[0][0]) #this is to find out which colour was worn the most.

#Solving Question 3
ranked = sorted(freq, key=lambda c: (freq[c], c)) #to find out the median colour, I first ranked the colours by frequency, then took the middle one
print("3. Median colour:", ranked[len(ranked) // 2], "| median frequency:", statistics.median(freq.values()))

#Solving Question 4
print("4. Variance:", statistics.pvariance(freq.values())) #finding the variance of the colour frequencies

#Solving Question 5
print("5. P(red) = %d/%d = %.4f" % (freq["RED"], len(colours), freq["RED"] / len(colours))) #finding the probability of red, I used the formula P(red) = frequency of red / total number of colours
# "%d/%d = %.4f" this just means The first %d gets freq["RED"], the number of times red appears, which is 9.
# The second %d gets len(colours), the total number of entries, which is 95.
# %.4f gets freq["RED"] / len(colours), which is 9 / 95 = 0.094736 and approxiamted to be shown as 0.0947.

#Solving Question 6
def save_to_db(): #Saving the colours and their frequencies in postgresql database
    #firstly, i installed postgre sql and launched it, then opened pg admin 4, where i named my database as "bincom test interview" and then connected to it.
    import psycopg2
    conn = psycopg2.connect(dbname="bincom test interview", user="postgres", password="bincom", host="localhost")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS colour_freq (colour VARCHAR(20) PRIMARY KEY, frequency INT)")
    for colour, count in freq.items():
        cur.execute("INSERT INTO colour_freq VALUES (%s, %s) ON CONFLICT (colour) DO UPDATE SET frequency = EXCLUDED.frequency",
                    (colour, count))
    conn.commit()
    conn.close()
    print("6. Saved to PostgreSQL") #the table has been created and the parameters have been saved to the postgre database.
try:
    save_to_db()
except Exception as e:
    print("6. DB save skipped:", e)

#Solving Question 7
def rsearch(lst, target, i=0): #a recursive searching algorithm to search for a number entered by a user in a list of numbers.
    if i == len(lst): 
        return -1
    if lst[i] == target:
        return i
    return rsearch(lst, target, i + 1)

nums = [4, 8, 15, 16, 23, 42] #list of number user will pick from to search for
n = int(input("7. Enter a number to search for between 4, 8, 15, 16, 23, 42: ")) # this is the prompt that will ask the user to enter a number to search for in the list of numbers above
pos = rsearch(nums, n)
print("   Found at index", pos) if pos != -1 else print("   Not found in", nums)

#Solving Question 8
# to generate a random 4 digit number of 0s and 1s and then convert the generated number to base 10.
binary = "".join(random.choice("01") for _ in range(4)) #the code generates a random 4 digit binary number here
print("8. Binary %s = %d in base 10" % (binary, int(binary, 2))) #this is where the conversion takes place

#Solving Question 9
#finding the sum of the first 50 fibonacci numbers
#i started this sum from 0
a, b, total = 0, 1, 0
for _ in range(50): #for loop
    total += a
    a, b = b, a + b
print("9. Sum of first 50 fibonacci numbers:", total)

#references
#these are the links I used as help for this python technical interview test
#https://www.tutorialspoint.com/python/index.htm
#https://www.youtube.com/watch?v=-GzyP0G4t88
#https://www.youtube.com/watch?v=4qH-7w5LZsA
#claude.com
#https://www.w3schools.com/

#Thank you and I hope to hear from you soon.

