import matplotlib.pyplot as plt 

language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

colors = ['red','orange','blue','pink','green','yellow']

explode = (0.1,0,0,0,0,0)

plt.pie(Popularity,explode=explode,labels=language,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago", bbox={'facecolor':'0.8', 'pad':5})

plt.show()