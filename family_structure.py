# A file for all tests that depend on family structure

import tag_parse as tag
import age

people, families = tag.read_file('./proj02test.ged')

def fiveLessBirths(people, families):   # Determines whether more than five siblings were born on the same date
    children = []   # list which will store individual lists of children separated by family
    for id in families:
        children.append(families[id]['CHIL'])
    isValid = True
    for related_children in children:   # iterate through each set of siblings
        dict_of_dates = {}
        for child in related_children:   # iterate through each child among siblings, storing each unique birthdate as
            # key and iterating value for non unique date - US14
            try:
                dict_of_dates[people[child]['BIRT']] += 1
            except:
                dict_of_dates[people[child]['BIRT']] = 1
        for date in dict_of_dates:
            if dict_of_dates[date] > 5:   # check for number of coincident births
                isValid = False
    if not isValid:
        return "More than five siblings were born on the same day"


def fifteenLessSiblings(families):   # Tests that each family has less than fifteen siblings - US15
    isValid = True
    for family in families:
        if len(families[family]["CHIL"]) > 14:
            isValid = False
    if not isValid:
        return "A family contains more than fourteen siblings"


def parents_not_too_old(people, families):
    for family in families:
        motherid = family['WIFE']
        fatherid = family['HUSB']
        for child in family['CHIL']:
            if (age.get_age(motherid, people) - age.get_age(child, people) >= 60):
                return "ERROR: Mother is too old - ID: " + motherid
            if (age.get_age(fatherid, people) - age.get_age(child, people) >= 80):
                return "ERROR: Father is too old - ID: " + fatherid


def get_last_name(key, people):
    name = people[key]['NAME'][:-1]
    while (name[0] != "/"):
        name = name[1:]
    return name[1:]


def male_last_names_align(people, families):
    for family in families:
        male_ln = get_last_name(family['HUSB'],people)
        for child in family['CHIL']:
            if (people[child]['SEX'] == 'M'):
                if (get_last_name(child,people) != male_ln):
                    return "ERROR: Male child's last name does not match father's - ID: " + child


