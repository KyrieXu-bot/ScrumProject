# -*- coding: utf-8 -*- 
# @Time : 10/16/2021 1:51 AM 
# @Author : Ethan
# @File : GedcomMain.py
# @Description :

import GedcomProcess as ged

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
    for individual in individuals:
        individual.showInfo()

