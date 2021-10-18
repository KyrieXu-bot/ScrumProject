# -*- coding: utf-8 -*- 
# @Time : 9/26/2021 1:30 PM 
# @Author : Ethan
# @File : GedcomClass.py
# @Description : Generate Class like Person or family, including their functions

import datetime

def IsADayBeforeBDay(Data_A, Date_B):
    """
    Compare 2 dates, to see if A is before B
    :param Data_A: format should be [day, month, year], all are integers
    :param Date_B: same as above
    :return: whether A is before B
    """
    if not isDateValid(Data_A):
        print("Date A is invalid!")
        return False
    if not isDateValid(Date_B):
        print("Date B is invalid!")
        return False
    if Data_A[2] > Date_B[2]:
        return False
    if Data_A[2] == Date_B[2]:  # if 2 dates in same year
        if Data_A[1] > Date_B[1]:
            return False
    if Data_A[1] == Date_B[1]:  # if 2 date in same month
        if Data_A[0] > Date_B[0]:
            return False
    return True


def convertDate(date: str):
    if date == 'NA' or date == 'Y':
        return date
    else:
        temp = date.split(' ')
        if temp[0] == "about":  # about 1998-2-3
            return list(map(int, temp[1].split('-')))
        else:
            return list(map(int, temp[0].split('-')))


def isDateValid(date):
    if date == 'NA':
        return False
    else:
        return True


class Person:
    def __init__(self, first_name: str, last_name: str, age: int,
                 birth_date: str, marry_date: str, divorce_date: str, death_date: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        self.birth_date = convertDate(birth_date)
        self.marry_date = convertDate(marry_date)
        self.divorce_date = convertDate(divorce_date)
        self.death_date = convertDate(death_date)

    def showInfo(self):
        print("------------------------")
        print(self.first_name + '.' + self.last_name)
        print('birth date: ' + '-'.join([str(i) for i in self.birth_date]))
        print('marry date: ' + '-'.join([str(i) for i in self.marry_date]))
        print('divorce date: ' + '-'.join([str(i) for i in self.divorce_date]))
        print('death date: ' + '-'.join([str(i) for i in self.death_date]))

    def isBirthBeforeDeath(self):
        return IsADayBeforeBDay(self.birth_date, self.death_date)

    def isMarryBeforeDeath(self):
        return IsADayBeforeBDay(self.marry_date, self.death_date)

    def isDivorceBeforeDeath(self):
        return IsADayBeforeBDay(self.divorce_date, self.death_date)

    def isBirthBeforeMarriage(self):
        return IsADayBeforeBDay(self.birth_date, self.marry_date)

    def isMarriageBeforeDivorce(self):
        return IsADayBeforeBDay(self.marry_date, self.divorce_date)

    def isDatesBeforeCurrent(self):
        return IsADayBeforeBDay(self.birth_date, convertDate(datetime.datetime.now().strftime('%d-%m-%Y')))

    def isLessThan150YearOld(self):
        return True if self.age < 150 else False
        # after refactor, the age calculation is written as a function, and redundant variables are removed


