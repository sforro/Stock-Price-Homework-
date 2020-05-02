from matplotlib import pylab as plt
import pandas

df1 = pandas.read_csv("MCD.csv")
#print(df1.head())
# need to tell pandas that Date is an actual Date.
df1['Date'] = pandas.to_datetime(df1.Date)
#print(df1.head())

df2 = pandas.read_csv("WEN.csv")
# print(df2)
df2['Date'] = pandas.to_datetime(df2.Date)
indexes = []
values = []
dates = []

mean = df1["Close"].mean()
mean2 = df2["Close"].mean()


plt.figure("McDonald's vs Wendy's Stock Price Evolution")

plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=1, label="Stock price MCD, mean="+str(mean))

plt.plot(df2["Date"], df2["Close"], 'b-', linewidth=1, label="Stock price WEN, mean2="+str(mean2))


# put the values
for i in range(len(dates)):
    plt.text(dates[i], values[i], str(int(values[i])))
plt.xlabel("Dates")
plt.legend(loc="upper left")



plt.show()