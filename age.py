from datetime import timedelta, datetime

def calc_ages(people): #runs on whole dictionary
    today = datetime.now()
    for key in people:
        if('BIRT' in people[key].keys()):
            if(is_dead(key, people) == False):
                bday = datetime.strptime(people[key]['BIRT'], '%d %b %Y')
                people[key]['BIRT'] = datetime.strptime(people[key]['BIRT'], '%d %b %Y')
                people[key]['AGE'] = int((today - bday).days/365.2425)
            else:
                #if dead age is their last living age people[key]['AGE']
                age = death_age(key, people)
                if(age < 0): #death before birth
                    print("ERROR: Invalid death date, death before birth")
                else:
                    people[key]['AGE']= age
    return people

def is_dead(key, people): #by person
    if('DEAT' in people[key].keys()):
        return True
    else:
        return False

def get_age(key, people): #by person
    #not totally needed but it could make life easy maybe.  can also just do a ditct call
    return (people[key]['AGE'])


def death_age(key, people): #by person
    today = datetime.now()
    if('DEAT' in people[key].keys()):
        print(people[key]['DEAT'])
        dday = datetime.strptime(people[key]['DEAT'], '%d %b %Y')
        people[key]['DEAT'] = datetime.strptime(people[key]['DEAT'], '%d %b %Y')
        bday = datetime.strptime(people[key]['BIRT'], '%d %b %Y')
        people[key]['BIRT'] = datetime.strptime(people[key]['BIRT'], '%d %b %Y')
        d_age = int((dday-bday).days/365.2425)
        return(d_age)
        

def marr_and_div_ages(families, people): #runs on whole dictionary
    for key in families: 
        marr_date = datetime.strptime(families[key]['MARR'], '%d %b %Y')
        
        div_date = datetime.strptime(families[key]['DIV'], '%d %b %Y')
        print(marr_date)


        people[families[key]['HUSB']]['MARR_AGE'] = int((marr_date-people[families[key]['HUSB']]['BIRT']).days/365.2425)
        people[families[key]['HUSB']]['DIV_AGE'] = int((div_date-people[families[key]['HUSB']]['BIRT']).days/365.2425)
        people[families[key]['WIFE']]['MARR_AGE'] = int((marr_date-people[families[key]['WIFE']]['BIRT']).days/365.2425)
        people[families[key]['WIFE']]['DIV_AGE'] = int((div_date-people[families[key]['WIFE']]['BIRT']).days/365.2425)
    return(people)

def div_age():
    pass
#kc sprint 1 birth before marrage | birth before death

def check_birth_before_marr(key, people):
    if(people[key]['MARR_AGE'] < 0):
        people[key]['MARR_AGE'] = "INVALID"
        print("ERROR: Invalid Marrage date, married before birth")
    else:
        print("Marrage date valid")

def store_ages(families, people):
    people = calc_ages(people)
    people = marr_and_div_ages(families, people)
    return people