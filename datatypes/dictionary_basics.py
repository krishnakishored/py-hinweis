# https://python-course.eu/python3_dictionaries.php

def dict_basics_1():
    city_population = {"New York City":8550405, "Los Angeles":3971883, "Toronto":2731571, "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}
    print(city_population["New York City"])
    # print(city_population["Detroit"]) # KeyError
    city_population["Halifax"] = 390096 # adding an entry
    en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}
    print(en_de)
    de_fr = {"rot" : "rouge", "grün" : "vert", "blau" : "bleu", "gelb":"jaune"}
    print("The French word for red is: " + de_fr[en_de["red"]])

    '''
    Only immutable data types can be used as keys
    '''
    # dic = { [1,2,3]:"abc"} # TypeError: unhashable type: 'list'
    dic = { (1,2,3):"abc", 3.1415:"abc"} # tuples as keys are ok

    '''dictionary of dictionaries'''
    dictionaries = {"en_de" : en_de, "de_fr" : de_fr }
    print(dictionaries["de_fr"]["blau"])

    print(len(dictionaries)) # 2
    del city_population["New York City"]
    print(city_population)

    from morsecode import morse
    print(len(morse)) # 38
    print("a" in morse) # False
    print("A" in morse) # True


def dict_basics_2():
    capitals = {"Austria":"Vienna", "Switzerland":"Bern", "Germany":"Berlin", "Netherlands":"Amsterdam"}
    print(capitals.pop("Germany")) # Berlin
    # print(capitals.pop("Germany")) # KeyError: 'Germany'
    print(capitals)
    capital = capitals.pop("Germany", "München") # this pop() methods prevents KeyError
    print(capital) # München
    '''
    popitem() is a method of dict, which doesn't take any parameter 
    and removes and returns an arbitrary (key,value) pair as a 2-tuple. 
    '''
    (city, state) = capitals.popitem()
    print(city,state)
    '''
    Accessing non-existing keys
    '''
    locations = {"Toronto" : "Ontario", "Vancouver":"British Columbia"}
    if "Ottawa" in locations:
        print(locations["Toronto"])
    
    proj_language = {"proj1":"Python", "proj2":"Perl", "proj3":"Java"}    
    print(proj_language.get("proj4")) # None. doesn't raise keyError


def dict_basics_3():
    '''A dictionary can be copied with the method copy()'''
    words = {}
    words["cat"]="chat"
    words["house"] = "Haus"
    w = words.copy() # only a shallow copy but not deep copy
    print(w) # {'cat': 'chat', 'house': 'Haus'}
    w["cat"] = "Katze"
    print(w) # {'cat': 'Katze', 'house': 'Haus'}
    print(words) # {'cat': 'chat', 'house': 'Haus'}


    trainings = { "course1":{"title":"Python Training Course for Beginners", 
                         "location":"Frankfurt", 
                         "trainer":"Steve G. Snake"},
              "course2":{"title":"Intermediate Python Training",
                         "location":"Berlin",
                         "trainer":"Ella M. Charming"},
              "course3":{"title":"Python Text Processing Course",
                         "location":"München",
                         "trainer":"Monica A. Snowdon"}
              }

    trainings2 = trainings.copy()

    trainings["course2"]["title"] = "Perl Training Course for Beginners"
    # print(trainings2)
    # {'course1': {'title': 'Python Training Course for Beginners', 'location': 'Frankfurt', 'trainer': 'Steve G. Snake'}, 
    # 'course2': {'title': 'Perl Training Course for Beginners', 'location': 'Berlin', 'trainer': 'Ella M. Charming'},
    # 'course3': {'title': 'Python Text Processing Course', 'location': 'München', 'trainer': 'Monica A. Snowdon'}}

    trainings["course2"] = {"title":"Perl Seminar for Beginners",
                         "location":"Ulm",
                         "trainer":"James D. Morgan"}
    print(trainings2["course2"]) # {'title': 'Intermediate Python Training', 'location': 'Berlin', 'trainer': 'Ella M. Charming'}

    '''
    update() merges the keys and values of one dictionary into another, 
    overwriting values of the same key:
    '''
    knowledge = {"Frank": {"Perl"}, "Monica":{"C","C++"}}
    knowledge2 = {"Guido":{"Python"}, "Frank":{"Perl", "Python"}}
    print(knowledge) # {'Frank': {'Perl'}, 'Monica': {'C', 'C++'}}
    knowledge.update(knowledge2) # {'Frank': {'Perl', 'Python'}, 'Monica': {'C', 'C++'}, 'Guido': {'Python'}}
    print(knowledge)

    '''Iterating over a Dictionary'''
    d = {"a":123, "b":34, "c":304, "d":99}
    for key in d:
        print(key,end=" ")
    print("\n")
    for key in d.keys():
            print(key,d[key],end=" ") # accessing as d[key] is less efficient than iterating over d.values()

    print("\n")
    for value in d.values():
            print(value,end=" ")


def dict_basics_4():
    '''lists from dictionaries'''
    w = {"house":"Haus", "cat":"", "red":"rot"}
    items_view = w.items()
    print(items_view)  # dict_items([('house', 'Haus'), ('cat', ''), ('red', 'rot')])
    print(list(items_view)) # [('house', 'Haus'), ('cat', ''), ('red', 'rot')]
    values_view = w.values()
    print(list(values_view)) # ['Haus', '', 'rot']
    print(list(w.keys())) # ['house', 'cat', 'red']
            
    '''
    dictionaries from lists
    zip() - returns an iterator
    we have to wrap a list() casting function around the zip call to get a list 
    '''
    dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    countries = ["Italy", "Germany", "Spain", "USA"]
    country_specialities_iterator = zip(countries, dishes)
    print(country_specialities_iterator) # <zip object at 0x101b4c088>
    country_specialities = list(country_specialities_iterator)
    print(country_specialities) # [('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]
    print(dict(country_specialities)) # {'Italy': 'pizza', 'Germany': 'sauerkraut', 'Spain': 'paella', 'USA': 'hamburger'}

    # This can be done directly by applying dict to zip (efficient way):
    # print(dict(list(zip(countries,dishes)))) # {'Italy': 'pizza', 'Germany': 'sauerkraut', 'Spain': 'paella', 'USA': 'hamburger'}
    print(dict(zip(countries,dishes))) # {'Italy': 'pizza', 'Germany': 'sauerkraut', 'Spain': 'paella', 'USA': 'hamburger'}

    '''
    There is still one question concerning the function zip().
    What happens, if one of the two argument lists contains more elements than the other one? 
    It's easy to answer: The superfluous elements, which cannot be paired, will be ignored
    '''


    '''keep in mind that iterators exhaust themselves'''
    l1 = ["a","b","c"]
    l2 = [1,2,3]
    c = zip(l1,l2)
    z1 = list(c)
    z2 = list(c)
    print(z1) # [('a', 1), ('b', 2), ('c', 3)] 
    print(z2) # []

# https://www.hackerrank.com/challenges/finding-the-percentage/problem
def find_average_percentage():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # avg = 0
    # for mark in student_marks[query_name]:
    #     avg+=mark
    # avg =  avg/len(student_marks[query_name])
    #  print(f'{avg:.2f}') # 10.10
    query_scores = student_marks[query_name]
    # print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
    print(f'{sum(query_scores)/len(query_scores):.2f}')

    # Converting Between Strings and Lists


if __name__ == "__main__":
    # dict_basics_1()
    # dict_basics_2()
    # dict_basics_3()
    # dict_basics_4()
    find_average_percentage()
    
   
