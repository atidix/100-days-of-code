import pandas

data = pandas.read_csv("day-25/Squirrel_data.csv")

fur = data["Primary Fur Color"]
fur_counts = fur.value_counts()

df = fur_counts.reset_index()

df.rename(columns={'Primary Fur Color': 'Fur Color', 'count': 'Count'}, inplace=True)

df.to_csv('squirrel_fur_data.csv')
