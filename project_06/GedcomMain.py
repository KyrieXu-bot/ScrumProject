# -*- coding: utf-8 -*- 
# @Time : 10/16/2021 1:51 AM 
# @Author : Ethan
# @File : GedcomMain.py
# @Description :
from typing import List

import GedcomProcess as ged
from GedcomClass import Person
from GedcomClass import Family
import GedcomClass


def isBirthAfterParentsDeath(individual_list: List[Person], family_list: List[Family]):
    """
    Written by HZ
    """
    flag = 0
    for family in family_list:
        husband_death = ''
        wife_death = ''
        children_birth_date = []
        for individual in individual_list:  # find husband_death and wife_death by matching ID
            if family.husband_id == individual.IID:
                husband_death = individual.death_date
                continue
            if family.wife_id == individual.IID:
                wife_death = individual.death_date
        for child_id in family.children:  # find children's birth date by matching ID
            for individual in individual_list:
                if child_id == individual.IID:
                    children_birth_date.append(individual.birth_date)
        if husband_death == 'NA' and wife_death == 'NA':
            # if parents are both alive, definitely no such problem
            return False
        if husband_death != 'NA':
            husband_death[1] += 9
            if husband_death[1] > 12:
                husband_death[1] -= 12
                husband_death[2] += 1
            for i in range(len(children_birth_date)):
                if GedcomClass.isADayBeforeBDay(husband_death, children_birth_date[i]):
                    print("Individual " + family.children[i] +
                          " 's birthday is even late than 9 months after his/her father " + family.husband_id +
                          "'s death date!")
                    flag = 1
        if wife_death != 'NA':
            for i in range(len(children_birth_date)):
                if GedcomClass.isADayBeforeBDay(wife_death, children_birth_date[i]):
                    print("Individual " + family.children[i] +
                          " 's birthday is after his/her mother " + family.wife_id + "'s death date!")
                    flag = 1
    if flag == 0:
        return False
    else:
        return True


def isParentsNotTooOld(individual_list: List[Person], family_list: List[Family]):
    """
    Written by CX
    """
    flag = 0
    for family in family_list:
        husband_birth = ''
        wife_birth = ''
        children_birth_date = []
        for individual in individual_list:  # find husband_death and wife_death by matching ID
            if family.husband_id == individual.IID:
                husband_birth = individual.birth_date
                husband_birth[2] += 80
                continue
            if family.wife_id == individual.IID:
                wife_birth = individual.birth_date
                wife_birth[2] += 60
        for child_id in family.children:  # find children's birth date by matching ID
            for individual in individual_list:
                if child_id == individual.IID:
                    children_birth_date.append(individual.birth_date)
        for i in range(len(children_birth_date)):
            if GedcomClass.isADayBeforeBDay(children_birth_date[i], husband_birth) and GedcomClass.isADayBeforeBDay(children_birth_date[i], wife_birth):
                print("success")
                flag = 1
            else:
                print("error")
                print(husband_birth)
                print(wife_birth)
                flag = 0
        if flag == 1:
            return True
        else:
            return False

if __name__ == '__main__':
    original_ged_file_path = "White-Family.ged"
    preprocessed_file_path = "PreprocessedOutput.txt"
    valid_records_path = "ValidRecords.txt"
    pretty_table_path = "2Tables.txt"

    ged.getGEDCOM(original_ged_file_path, preprocessed_file_path)
    ged.getValidRecords(preprocessed_file_path, valid_records_path)
    indi_fami_dict_list = ged.getIndiFamiList(valid_records_path)
    ged.getTable(indi_fami_dict_list, pretty_table_path)

    individuals = ged.getIndividuals(indi_fami_dict_list)
    families = ged.getFamilies(indi_fami_dict_list)
    # for i in individuals:
    #     i.showInfo()
        # print("isBirthBeforeMarry: " + str(i.isBirthBeforeMarry()))
        # print("isBirthBeforeDeath: " + str(i.isBirthBeforeDeath()))
        # print("isMarryBeforeDeath: " + str(i.isMarryBeforeDeath()))
        # print("isDivorceBeforeDeath: " + str(i.isDivorceBeforeDeath()))
        # print("isMarryeBeforeDivorce: " + str(i.isMarryeBeforeDivorce()))
        # print("isDatesBeforeCurrent: " + str(i.isDatesBeforeCurrent()))
    # for i in families:
    #     i.showInfo()

    isBirthAfterParentsDeath(individuals, families)
    isParentsNotTooOld(individuals, families)

