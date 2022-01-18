import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("globalterrorismdb_0718dist.csv", encoding = "latin1")
print("\nDataset is :- \n",df.head())
print("\nShape of dataset :-",df.shape)

pd.pandas.set_option("display.max_columns", None)

#selecting important columns only
df = df[["iyear", "imonth", "country_txt", "region_txt", "provstate", "city", "latitude", "longitude", "location", "summary", "attacktype1_txt", "targtype1_txt", "gname", "motive", "weaptype1_txt", "nkill", "nwound", "addnotes"]]
print("\nSelected Datase :- \n",df.head())
print("\nShape of Dataset after selection columns :- ",df.shape)

#check null values in dataset
print("\nNull values in dataset :- \n",df.isnull().sum())

#fill the null values in kill and wound column and add new column that's casualty
df["nkill"] = df["nkill"].fillna(0)
df["nwound"] = df["nwound"].fillna(0)
df["casualty"] = df["nkill"] + df["nwound"]

#knowing about dataset
print("\nStatistical Terms in Datase :- \n",df.describe())


#1) first we check year wise attacks
#no of attacks in each year
attacks = df["iyear"].value_counts(dropna = False).sort_index().to_frame().reset_index().rename(columns= {"index": "Year", "Year": "Attacks"}).set_index("Year")
print("\nTotal attack in each year :- \n",attacks.head())

attacks.plot(kind = "bar", figsize = (15,6), fontsize = 13)
plt.title("Timeline of Attacks")
plt.xlabel("Years")
plt.ylabel("Number Of Attacks")
plt.show()

#no of kill per year
year_kill = df[["iyear", 'nkill']].groupby('iyear').sum()
print("\nTotal kill in each year :- \n",year_kill.head())

year_kill.plot(kind = "bar", figsize = (15, 6), fontsize = 13)
plt.title("Year wise kill")
plt.xlabel("Years")
plt.ylabel("'Number of Death")
plt.show()

#no of wound per year
year_wound = df[["iyear", 'nwound']].groupby("iyear").sum()
print("\nTotal wounded in each year :- \n",year_wound.head())

year_wound.plot(kind = "bar", figsize = (15, 6), fontsize = 13)
plt.title("Year wise wounded")
plt.xlabel("Years")
plt.ylabel('Number Of Wounded')
plt.show()

#no of casualties per year
year_casualty = df[["iyear", "casualty"]].groupby("iyear").sum()
print("\nTotal casualties in each year :- \n",year_casualty.head())

year_casualty.plot(kind = "bar", figsize = (15, 6), fontsize = 13)
plt.title("Year wise Casualties")
plt.xlabel("Years")
plt.ylabel("Number of Casualties")
plt.show()


#2) region wise check
#No of attack in each region
reg = pd.crosstab(df["iyear"], df["region_txt"])
print("\nTotal attack in each region :- \n",reg.head())

reg.plot(kind = "area", stacked = False, alpha = 0.5, figsize = (15, 6), fontsize = 13)
plt.title("Region wise attack")
plt.xlabel("Year")
plt.ylabel("Region")
plt.show()

#total terrorist attacks in each region
regt = reg.transpose()
regt["Total"] = regt.sum(axis=1)
ra = regt["Total"].sort_values()
print("\nTotal attack in each region :- \n",ra)

ra.plot(kind = "bar" , figsize = (15,6))
plt.title("Totol Number of attacks in each region from 1970-2017")
plt.xlabel("Region")
plt.ylabel("Number of attacks")
plt.show()

#total kill in each region
region_kill = df[["region_txt", "nkill"]].groupby("region_txt").sum()
print("\nTotal kill in each region :- \n",region_kill)

region_kill.plot(kind = "bar", figsize = (15, 6))
plt.title("Region wise Kill")
plt.xlabel("Region")
plt.ylabel("Number of Kill")
plt.show()

#total wounded in each region
region_wound = df[["region_txt", "nwound"]].groupby("region_txt").sum()
print("\nTotal wounded in each region :- \n",region_wound)

region_wound.plot(kind = "bar", figsize = (15, 6))
plt.title("Region wise Wound")
plt.xlabel("Region")
plt.ylabel("Number Of Wound")
plt.show()

#total casualties in each region
region_casualties = df[["region_txt", "casualty"]].groupby("region_txt").sum()
print("\nTotal casualties in each region :- \n",region_casualties)

region_casualties.plot(kind= "bar", figsize= (15,6))
plt.title("Region wise casualties")
plt.xlabel("Region")
plt.ylabel("Number of Casualties")
plt.show()


#3) country wise check
#total attack in each country
country = df["country_txt"].value_counts().head(10)
print("\nTotal attack in each country :- \n",country)

country.plot(kind = "bar", figsize = (15, 6))
plt.title("Country wise attack")
plt.xlabel("Countries")
plt.ylabel("Number Of attacks")
plt.show()

#total kill in each country
country_kill = df[["country_txt", "nkill"]].groupby("country_txt").sum().sort_values(by = "nkill", ascending= False)
print("\nTotal Kill in each country :- \n",country_kill.head(10))

country_kill[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("Country wise kill")
plt.xlabel("Country")
plt.ylabel("Number of Kill")
plt.show()

#total wounded in each country
country_wounded = df[["country_txt", "nwound"]].groupby("country_txt").sum().sort_values(by = "nwound", ascending=False)
print("\nTotal wounded in each country :- \n",country_wounded.head(10))

country_wounded[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("Country Wise wounded")
plt.xlabel("Country")
plt.ylabel('Number Of wounded')
plt.show()

#total casualties in each country
country_casualty = df[["country_txt", "casualty"]].groupby("country_txt").sum().sort_values(by = "casualty", ascending= False)
print("\nTotal casualties in each country :- \n",country_casualty.head(10))

country_casualty[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("Country wise casualties")
plt.xlabel("Country")
plt.ylabel("Number of Casualties")
plt.show()


#4) city  wise check
#Total attack in each city
city = df["city"].value_counts()
print("\nTotal attack in each city :- \n",city[1:11])

city[1:11].plot(kind = "bar", figsize = (15, 6))
plt.title("City wise attacks")
plt.xlabel("Cities")
plt.ylabel("Number Of attacks")
plt.show()

#Total kill in each city
city_kill = df[["city", "nkill"]].groupby("city").sum().sort_values(by = "nkill", ascending= False).drop("Unknown")
print("\nTotal kill in each city :- \n",city_kill.head(10))

city_kill[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("City wise kill")
plt.xlabel("Cities")
plt.ylabel("Number Of Kill")
plt.show()

#Total wounded in each city
city_wound =df[["city", 'nwound']].groupby("city").sum().sort_values(by = "nwound", ascending=False).drop("Unknown")
print("\nTotal wounded in each city :- \n",city_wound.head(10))

city_wound[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("City wise Wounded")
plt.xlabel("Cities")
plt.ylabel("Number Of Wounded")
plt.show()

#Total casualties in each city
city_casualty = df[["city", "casualty"]].groupby("city").sum().sort_values(by = "casualty", ascending= False).drop("Unknown")
print("\nTotal casualties in each city :- \n",city_casualty.head(10))

city_casualty[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("City wise casualties")
plt.xlabel("Cities")
plt.ylabel("Number of Casualties")
plt.show()


#5) Group wise check
#Total attack by each group
group = df["gname"].value_counts()[1:10]
print("\nTotal attack by each group :- \n",group)

group.plot(kind = "bar", figsize = (15, 6))
plt.title("Group wise Attacks")
plt.xlabel('Terrorist Group')
plt.ylabel('Number Of Attacks')
plt.show()

#Total kill by each group
group_kill = df[['gname', "nkill"]].groupby("gname").sum().sort_values(by = "nkill" , ascending= False).drop("Unknown")
print("\nTotal kill by each group :- \n",group_kill.head(10))

group_kill[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("Group wise kill")
plt.xlabel("Group")
plt.ylabel("Number Of kill")
plt.show()

#Total wounded by each group
group_wound = df[['gname', "nwound"]].groupby("gname").sum().sort_values(by = "nwound" , ascending= False).drop("Unknown")
print("\nTotal wounded by each group :- \n",group_wound.head(10))

group_wound[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("Group wise Wounded")
plt.xlabel("Group")
plt.ylabel("Number Of Wounded")
plt.show()

#Total casualties by each group
group_casualty = df[['gname', "casualty"]].groupby("gname").sum().sort_values(by = "casualty" , ascending= False).drop("Unknown")
print("\nTotal casualties by each group :- \n",group_casualty.head(10))

group_casualty[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("Group wise Casualty")
plt.xlabel("Group")
plt.ylabel("Number Of Casualty")
plt.show()

 
#6) attack type wise check
#Total attack by attack type
attack = df["attacktype1_txt"].value_counts()
print("\nTotal attack by attack type :- \n",attack)

attack.plot(kind = "bar", figsize = (15, 6))
plt.title("Types Of Attacks")
plt.xlabel("Attack Type")
plt.ylabel("Number Of Attack")
plt.show()

#Total casualties by attack type
attack_casualty = df[["attacktype1_txt", "casualty"]].groupby("attacktype1_txt").sum().sort_values(by = "casualty", ascending=False)
print("\nTotal casualties by attack type :- \n",attack_casualty)

attack_casualty.plot(kind = "bar", figsize = (15, 6))
plt.title("Casualties in each attack")
plt.xlabel("Attack Types")
plt.ylabel("Number of Casualties")
plt.show()

#Total kill by attack type
attack_kill = df[["attacktype1_txt", "nkill"]].groupby("attacktype1_txt").sum().sort_values(by = "nkill", ascending=False)
print("\nTotal kill by attack type :- \n",attack_kill)

attack_kill.plot(kind = "bar", figsize = (15, 6))
plt.title("kill in each attack")
plt.xlabel("Attack Types")
plt.ylabel("Number of kill")
plt.show()

#Total wounded by attack type
attack_wound = df[["attacktype1_txt", "nwound"]].groupby("attacktype1_txt").sum().sort_values(by = "nwound", ascending=False)
print("\nTotal wounded by attack type :- \n",attack_wound)

attack_wound.plot(kind = "bar", figsize = (15, 6))
plt.title("Wound in each attack")
plt.xlabel("Attack Types")
plt.ylabel("Number of Wound")
plt.show()


#7) Target type wise check
#Total attack by target type
target_attack = df["targtype1_txt"].value_counts()
print("\nTotal attack by target type :- \n",target_attack)

target_attack.plot(kind = "bar", figsize = (15, 6))
plt.title("Types of Targets")
plt.xlabel("Target Types")
plt.ylabel("Number of attacks")
plt.show()

#Total kill by target type
target_kill = df[["targtype1_txt", "nkill"]].groupby("targtype1_txt").sum().sort_values(by = "nkill", ascending=False)
print("\nTotal kill by target type :- \n",target_kill)

attack_kill.plot(kind = "bar", figsize = (15, 6))
plt.title("kill in each Target")
plt.xlabel("Target Types")
plt.ylabel("Number of kill")
plt.show()

#Total wounded by target type
target_kill = df[["targtype1_txt", "nwound"]].groupby("targtype1_txt").sum().sort_values(by = "nwound", ascending=False)
print("\nTotal wounded by target type :- \n",target_kill)

attack_kill.plot(kind = "bar", figsize = (15, 6))
plt.title("Wounded in each Target")
plt.xlabel("Target Types")
plt.ylabel("Number of wounded")
plt.show()

#Total casualties by target type
target_kill = df[["targtype1_txt", "casualty"]].groupby("targtype1_txt").sum().sort_values(by = "casualty", ascending=False)
print("\nTotal casualties by target type :- \n",target_kill)

attack_kill.plot(kind = "bar", figsize = (15, 6))
plt.title("casualty in each Target")
plt.xlabel("Target Types")
plt.ylabel("Number of casualty")
plt.show()


#8) Group + Country wise
#Sorting number of attacks
group_country = df[["gname", "country_txt"]].value_counts().drop("Unknown")
print("\nGroup + Country wise attack :- \n",group_country.head(10))

group_country[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("Countries with most attacks by a particular group")
plt.xlabel("Terrorist Group, Country")
plt.ylabel("Number OF attack")
plt.show()

#sorting by number of kill
group_country_kill = df[["gname", "country_txt", "nkill"]].groupby(["gname", "country_txt"], axis = 0).sum().sort_values(by = "nkill", ascending=False)
group_country_kill[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("Countries with most kill by a particular group")
plt.xlabel("Terrorist Group, Country")
plt.ylabel("Number OF attack")
plt.show()

#sorting by number of wounded
group_country_wounded = df[["gname", "country_txt", "nwound"]].groupby(["gname", "country_txt"], axis = 0).sum().sort_values(by = "nwound", ascending=False)
group_country_wounded[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("Countries with most wound by a particular group")
plt.xlabel("Terrorist Group, Country")
plt.ylabel("Number OF attack")
plt.show()

#sorting by number of casualties
group_country_casualties = df[["gname", "country_txt", "casualty"]].groupby(["gname", "country_txt"], axis = 0).sum().sort_values(by = "casualty", ascending=False)
group_country_casualties[:10].plot(kind = "bar", figsize = (15, 6))
plt.title("Countries with most casualties by a particular group")
plt.xlabel("Terrorist Group, Country")
plt.ylabel("Number OF attack")
plt.show()


#world-wide by terrorist attack
print("\nTotal number of kill due to terrorist attack are :- {}".format(df.loc[:, "nkill"].sum()))
print("Total number of wounded due to terrorist attack are :- {}".format(df.loc[:, "nwound"].sum()))
print("Total number of casualty due to terrorist attack are :- {}".format(df.loc[:, "casualty"].sum()))