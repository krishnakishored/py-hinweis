import pandas as pd
import numpy as np

cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
                "Paris", "Vienna", "Bucharest", "Hamburg", 
                "Budapest", "Warsaw", "Barcelona", 
                "Munich", "Milan"],
        "population": [8615246, 3562166, 3165235, 2874038,
                        2273305, 1805681, 1803425, 1760433,
                        1754000, 1740119, 1602386, 1493900,
                        1350680],
        "country": ["England", "Germany", "Spain", "Italy",
                    "France", "Austria", "Romania", 
                    "Germany", "Hungary", "Poland", "Spain",
                    "Germany", "Italy"]}


def dataframes_1():
    years = range(2014,2018)
    shop1 = pd.Series([2409.14, 2941.01, 3496.83, 3119.55], index=years)
    shop2 = pd.Series([1203.45, 3441.62, 3007.83, 3619.53], index=years)
    shop3 = pd.Series([3412.12, 3491.16, 3457.19, 1963.10], index=years)
    shop1.name = "Zürich"
    shop2.name = "Winterthur"
    shop3.name = "Freiburg"

    shops_df = pd.concat([shop1, shop2, shop3],axis=1)
    print(shops_df) # dataframe
    print("------")
    cities = ["Zürich", "Winterthur", "Freiburg"]
    shops_df2 = pd.concat([shop1, shop2, shop3], axis=1)
    shops_df2.columns = cities 
    print(shops_df2)
    print(type(shops_df))

    city_frame = pd.DataFrame(cities)
    print(city_frame)
    '''Retrieve column name'''
    print(city_frame.columns.values) # ['name' 'population' 'country']
    '''Assign a custom index'''
    ordinals = ["first", "second", "third", "fourth",
            "fifth", "sixth", "seventh", "eigth",
            "ninth", "tenth", "eleventh", "twelvth",
            "thirteenth"]
    city_frame = pd.DataFrame(cities, index=ordinals)
    print(city_frame)


def dataframes_2():
    '''DataFrames from Dictionaries'''
                      
    '''Rearranging the order of columns'''
    city_frame = pd.DataFrame(cities,
                          columns=["name", 
                                   "country", 
                                   "population"])
    print(city_frame)

    city_frame.reindex(index=[0, 2, 4, 6,  8, 10, 12, 1, 3, 5, 7, 9, 11], 
                   columns=['country', 'name', 'population'])

    print(city_frame)


    city_frame.rename(columns={"name":"Nume", 
                           "country":"țară", 
                           "population":"populație"},
                 inplace=True)

    print(city_frame)                                    


def dataframes_3():
    # Existing Column as the Index of a DataFrame
    city_frame = pd.DataFrame(cities,
                          columns=["name", "population"],
                          index=cities["country"])

    print(city_frame)    
    # city_frame.set_index("population", inplace=True)
    # print(city_frame)   

    '''Label-Indexing on the Rows'''
    print(city_frame.loc["Germany"])
    print(city_frame.loc[["Germany", "France"]])
    print(city_frame.loc[city_frame.population>2000000])

    '''Sum and Cumulative Sum'''
    print(city_frame.sum())
    print(city_frame["population"].sum())
    print(city_frame["population"].cumsum())

def dataframes_4():
    '''Accessing the Columns of a DataFrame'''
    city_frame = pd.DataFrame(cities)
    print(city_frame['population']) # as a dictionary
    print(city_frame.population) # as an attribute
    print(type(city_frame.population), type(city_frame['population'])) # <class 'pandas.core.series.Series'> 
    '''Assigning New Values to a Column'''
    area = [1572, 891.85, 605.77, 1285, 
        105.4, 414.6, 228, 755, 
        525.2, 517, 101.9, 310.4, 
        181.8]
    # area could have been designed as a list, a Series, an array or a scalar   
    city_frame["area"] = area
    print(city_frame)
    '''Sorting DataFrames'''
    city_frame = city_frame.sort_values(by="area", ascending=False)
    print(city_frame)
    '''Inserting new columns into existing DataFrames'''
    city_frame = pd.DataFrame(cities, columns=["country", "population"], index=cities["name"])
    idx = 1
    city_frame.insert(loc=idx, column='area', value=area)
    print(city_frame)

    '''DataFrame from nested dictionaries'''
    growth = {"Switzerland": {"2010": 3.0, "2011": 1.8, "2012": 1.1, "2013": 1.9},
          "Germany": {"2010": 4.1, "2011": 3.6, "2012":	0.4, "2013": 0.1},
          "France": {"2010":2.0,  "2011":2.1, "2012": 0.3, "2013": 0.3},
          "Greece": {"2010":-5.4, "2011":-8.9, "2012":-6.6, "2013":	-3.3},
          "Italy": {"2010":1.7, "2011":	0.6, "2012":-2.3, "2013":-1.9}
          } 
    growth_frame = pd.DataFrame(growth)
    print(growth_frame)
    '''Transpose'''
    print(growth_frame.T)

    '''Filling a DataFrame with random values:'''
    names = ['Frank', 'Eve', 'Stella', 'Guido', 'Lara']
    index = ["January", "February", "March",
         "April", "May", "June",
         "July", "August", "September",
         "October", "November", "December"]
    df = pd.DataFrame((np.random.randn(12, 5)*1000).round(2),
                  columns=names,
                  index=index)
    print(df)


if __name__ == "__main__":
    # dataframes_1()
    # dataframes_2()
    # dataframes_3()
    dataframes_4()
