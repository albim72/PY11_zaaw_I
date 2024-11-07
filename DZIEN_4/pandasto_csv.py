import pandas as pd

data = {
    'Name':['Alicja','Piotr','Tomasz','Jan','Nadia'],
    'Age':[25,60,94,12,55],
    'Score':[88.9,34.5,67.8,88,19.9]
}

df = pd.DataFrame(data)

outputfilename = 'persons.csv'

df.to_csv(outputfilename,index=False)

df.to_html('dane.html')
df.
dd = df.to_dict()


print("Zapisano!!")
print(dd)
