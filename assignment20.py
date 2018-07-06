# QUESTION 1

import pandas as pd
d={"name":pd.Series(["Smaily"]),
   "age":pd.Series([22]),"email_id":pd.Series(["smailybhatnagar@gmail.com"]),
    "mobile_no.":pd.Series([123456789])}
df=pd.DataFrame(d)
print(d)
df.loc[1]=["abc",23,"abc@gmail.com",123]
print(df)

#END


# QUESTION 2


df = pd.read_csv("p.csv")
#a
print(df.head(5))
#b
print(df.head(10))
#c
print(df['MinTemp'].describe())
print(df['MinTemp'].max())
print(df['MinTemp'].var())
print(df['RISK_MM'].describe())
print(df['RISK_MM'].mean())
#d
print(df.tail(5))
print(df['Location'])
print(df['Location'].describe)

# END




