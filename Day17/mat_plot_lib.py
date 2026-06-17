import matplotlib.pyplot as plt 

#create a first chart 
x = [1,2,3,4,5]
y = [10, 40, 45, 65, 80]

# #line chart 
plt.plot(x,y)
#displays the chart 
plt.show() 

#Customized Chart 
plt.figure(figsize=(4,3)) # figure size

plt.plot(x, y, color='red', marker='o', linestyle='--', linewidth=1, markersize=10)

plt.title("Heading of chart")
plt.xlabel("x-axis ")
plt.ylabel("y-axis ")

plt.show()

# data with multiple lines

x = [1,2,3,4,5]
subjects=['Maths','Science','Social','English','Nepali']
m1 = [82,83,45,48,90]
m2 = [75,56,56,86,42]

plt.plot(x, m1, label='Marks of student1') # ploting y1 data
plt.plot(x, m2, label='Marks of Student1') # ploting y2 data

plt.title("Marks Chart")
plt.xlabel("Marks")
plt.ylabel("Subjects")

plt.legend() # show legends
plt.show()


#Bar chart
x = ['A','B','C','D','E']
y = [30, 20, 55, 45, 65]

plt.bar(x,y)
plt.title('Bar Chart Example')
plt.show()

#histogram:  used for distribution analysis
import random
data = [random.randint(1, 20) for _ in range(500)]

plt.hist(data, bins=20) # histogram chart
plt.title("Histogram")
plt.show()

#piechart  : used to show part-to-whole relationships/data
data
categories = ['A','B','C','D','E']
sales = [10, 20, 55, 35, 45]

plt.pie(sales, labels=categories, autopct = '%1.1f%%', startangle=90)
plt.title("Pie Chart")
plt.show()

#Scatter Plot: used to find relationship btwn variables
#data
y1 = [10, 20, 25, 35, 45]
y2 = [20, 30, 35, 45, 55]

plt.scatter(y1, y2)
plt.title("Scatter Plot")
plt.show()

#SUB plots : used to show multiple charts in one figure

# data-1 - bar chart
categories = ['Mon','Tue','Wed','Thu','Fri']
sales = [10, 20, 55, 35, 45]

# data-2 - scatter plot
y1 = [10, 20, 25, 35, 45]
y2 = [20, 30, 35, 45, 55]

plt.figure(figsize=(10,4))

# first plot- bar chart
plt.subplot(1,2,1) # row, column, position
plt.bar(categories, sales)
plt.title("Daily Sales")
plt.xlabel("Week Days")
plt.ylabel("Sales")

# second plot- scatter chart
plt.subplot(1,2,2) # row, column, position
plt.scatter(y1, y2)
plt.title("User Data")
plt.xlabel("User1")
plt.ylabel("User2")

plt.show()


#Matplotlib and pandas-working with real data
import pandas as pd
# data
data = {
    'Students' : ['Kalyan', 'Ishan', 'Rohit', 'Sandeep'],
    'Marks' : [98, 75, 45, 86]
}

df = pd.DataFrame(data)
print(df)

plt.bar(df['Students'], df['Marks'])
plt.title("Matplotlib with Pandas Demonstration")
plt.xlabel("Name of Students")
plt.ylabel("Marks of Student")
plt.show()

#Save charts 
plt.savefig("pd_and_matplot.png")