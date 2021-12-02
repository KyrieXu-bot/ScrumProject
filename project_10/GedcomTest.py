# -*- coding: utf-8 -*- 
# @Time : 9/26/2021 12:31 AM
# @Author : Ethan
# @File : GedcomTest.py
# @Description : CX the class and its functions in GedcomClass.py

import unittest
import GedcomClass
import GedcomMain


class TestExtract(unittest.TestCase):
    # def testStoreBirthAndDeathDate(self):
    #     """
    #     Written by HZ
    #     :return:
    #     """
    #     person1 = GedcomClass.Person("I1", "F1", "Ethan", "Winters", 80, "1997-7-3", "1998-8-20", "2028-6-12",
    #                                  "1998-8-8")
    #     person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "2000-3-25", "1950-5-4",
    #                                  "2070-10-10")
    #     self.assertEqual(person1.birth_date, [3, 7, 1997])
    #     self.assertEqual(person1.death_date, [8, 8, 1998])
    #     self.assertEqual(person2.birth_date, [5, 6, 1945])
    #     self.assertEqual(person2.death_date, [10, 10, 2070])
    #
    # def testBirthBeforeMarry(self):
    #     """
    #     Written by HZ
    #     :return:
    #     """
    #     person1 = GedcomClass.Person("I1", "F1", "Ethan", "Winters", 80, "1997-7-3", "1998-8-20", "2028-6-12",
    #                                  "1998-8-8")
    #     person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "1900-3-25", "1950-5-4",
    #                                  "1925-10-10")
    #
    #     self.assertTrue(person1.isBirthBeforeMarry())
    #     self.assertFalse(person2.isBirthBeforeMarry())
    #
    # def testBirthBeforeDeath(self):
    #     """
    #     Written by HZ
    #     :return:
    #     """
    #     person1 = GedcomClass.Person("I1", "F1", "Ethan", "Winters", 80, "1997-7-3", "1998-8-20", "2028-6-12",
    #                                  "1998-8-8")
    #     person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "2000-3-25", "1950-5-4",
    #                                  "1900-10-10")
    #
    #     self.assertTrue(person1.isBirthBeforeDeath())
    #     self.assertFalse(person2.isBirthBeforeDeath())
    #
    # def testMarryBeforeDeath(self):
    #     """
    #     Written by FJ
    #     :return:
    #     """
    #     person1 = GedcomClass.Person("I1", "F1", "Orion", "White", 66, "929-5-18", "1955-2-27", "NA", "1995-9-7")
    #     person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 11, "2000-3-25", "2070-5-4", "2049-10-10", "NA")
    #     print(person2.isMarryBeforeDeath())
    #     self.assertTrue(person1.isMarryBeforeDeath())
    #     self.assertFalse(person2.isMarryBeforeDeath())
    #
    # def testDivorceBeforeDeath(self):
    #     """
    #     Written by FJ
    #     :return:
    #     """
    #     person1 = GedcomClass.Person("I1", "F1", "Regulus", "White", 91, "1906-11-4", "1930-6-11", "1935-3-4",
    #                                  "1998-4-18")
    #     person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 22, "2000-3-25", "2070-5-4", "2049-10-10", "NA")
    #
    #     self.assertTrue(person1.isDivorceBeforeDeath())
    #     self.assertFalse(person2.isDivorceBeforeDeath())
    #
    # def testMarryBeforeDivorce(self):
    #     """
    #     Written by CX
    #     :return:
    #     """
    #     person1 = GedcomClass.Person("I1", "F1", "Regulus", "White", 91, "1906-11-4", "1930-6-11", "1935-3-4",
    #                                  "1998-4-18")
    #     person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 22, "2000-3-25", "2070-5-4", "2049-10-10", "NA")
    #
    #     self.assertTrue(person1.isMarryeBeforeDivorce())
    #     self.assertFalse(person2.isMarryeBeforeDivorce())
    #
    # def testDatesBeforeCurrent(self):
    #     """
    #     Written by CX
    #     :return:
    #     """
    #     person1 = GedcomClass.Person("I1", "F1", "Regulus", "White", 91, "1906-11-4", "1930-6-11", "1935-3-4",
    #                                  "1998-4-18")
    #     self.assertTrue(person1.isDatesBeforeCurrent())
    #
    # """
    # Sprint 2 Tests below
    # """
    #
    # def testIsLessThan150YearOld(self):
    #     """
    #     Written by HZ
    #     :return:
    #     """
    #     person1 = GedcomClass.Person("I1", "F1", "Regulus", "White", 91, "1800-11-4", "1930-6-11", "1935-3-4",
    #                                  "1998-4-18")
    #     self.assertTrue(person1.isLessThan150YearOld())
    #
    # def testIsBirthAfterParentsDeath(self):
    #     """
    #     Written by HZ
    #     :return:
    #     """
    #     individuals = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
    #                                       "1980-3-5", "1985-2-27", "NA", "1989-6-4"),
    #                    GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
    #                                       "1980-3-5", "1985-2-27", "NA", "1995-3-3"),
    #                    GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
    #                                       "1989-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
    #                    GedcomClass.Person("I4", "F1", "Ghost", "Isme", 15,
    #                                       "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                    GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
    #                                       "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                    ]
    #     families = [GedcomClass.Family("F1", "1985-2-27",
    #                                    "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
    #     self.assertTrue(GedcomMain.isBirthAfterParentsDeath(individuals, families))
    #
    # def testIsBirthAfterParentsMarriage(self):
    #     """
    #         Written by FJ
    #         :return:
    #     """
    #     individuals = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
    #                                       "1980-3-5", "1985-2-27", "NA", "1989-6-4"),
    #                    GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
    #                                       "1980-3-5", "1985-2-27", "NA", "1995-3-3"),
    #                    GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
    #                                       "1982-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
    #                    GedcomClass.Person("I4", "F1", "Ghost", "Isme", 15,
    #                                       "1988-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                    GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
    #                                       "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                    ]
    #     families = [GedcomClass.Family("F1", "1985-2-27",
    #                                    "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
    #     self.assertTrue(GedcomMain.isBirthAfterParentsMarriage(individuals, families))
    #
    # def testIsMarriageAfter14(self):
    #     """
    #         Written by FJ
    #         :return:
    #     """
    #     individuals = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
    #                                       "1980-3-5", "1985-2-27", "NA", "1989-6-4"),
    #                    GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
    #                                       "1980-3-5", "1985-2-27", "NA", "1995-3-3"),
    #                    ]
    #     families = [GedcomClass.Family("F1", "1985-2-27",
    #                                    "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
    #     self.assertTrue(GedcomMain.isMarriageAfter14(individuals, families))
    #
    # def testIsParentsNotTooOld(self):
    #     """
    #     Written by CX
    #     :return:
    #     """
    #     individuals = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
    #                                       "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
    #                    GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
    #                                       "1940-3-5", "1985-2-27", "NA", "1995-3-3"),
    #                    GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
    #                                       "1989-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
    #                    GedcomClass.Person("I4", "F1", "Ghost", "Isme", 15,
    #                                       "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                    GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
    #                                       "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                    ]
    #     families = [GedcomClass.Family("F1", "1985-2-27",
    #                                    "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
    #     self.assertTrue(GedcomMain.isParentsNotTooOld(individuals, families))
    #
    # def testIsThereBigamy(self):
    #     """
    #     Written by CX
    #     :return:
    #     """
    #     families1 = [GedcomClass.Family("F1", "1985-2-27",
    #                                     "1986-2-27", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4']),
    #                  GedcomClass.Family("F2", "1987-2-27",
    #                                     "NA", "I1", "Father /Isme/", "I2", "Mother /Ash/", ['I5']),
    #                  ]
    #     families2 = [GedcomClass.Family("F1", "1985-2-27",
    #                                     "1995-2-27", "I1", "Father /Buck/", "I2", "Mother /Jenny/", ['I3', 'I4']),
    #                  GedcomClass.Family("F2", "1990-2-27",
    #                                     "2000-2-27", "I6", "Father /Bob/", "I2", "Mother /Jenny/", ['I5']),
    #                  ]
    #     self.assertFalse(GedcomMain.isThereBigamy(families1))
    #     self.assertTrue(GedcomMain.isThereBigamy(families2))
    #
    # """
    # Sprint 3 Tests below
    # """
    #
    # def testIsSiblingsLessThan15(self):
    #     """
    #     Written by HZ
    #     :return:
    #     """
    #     families1 = [GedcomClass.Family("F1", "1985-2-27",
    #                                     "1986-2-27", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4']),
    #                  GedcomClass.Family("F2", "1987-2-27",
    #                                     "NA", "I1", "Father /Isme/", "I2", "Mother /Ash/", ['I5']),
    #                  ]
    #     families2 = [GedcomClass.Family("F1", "1985-2-27",
    #                                     "1995-2-27", "I1",
    #                                     "Father /Buck/",
    #                                     "I2",
    #                                     "Mother /Jenny/",
    #                                     ['I3', 'I4', 'I8', 'I9', 'I3',
    #                                      'I4', 'I8', 'I9', 'I3', 'I4',
    #                                      'I8', 'I9', 'I3', 'I4', 'I8',
    #                                      'I9', 'I3', 'I4', 'I8', 'I9']),
    #                  GedcomClass.Family("F2", "1990-2-27",
    #                                     "2000-2-27", "I6", "Father /Bob/", "I2", "Mother /Jenny/", ['I5']),
    #                  ]
    #     self.assertTrue(GedcomMain.isSiblingsLessThan15(families1))
    #     self.assertFalse(GedcomMain.isSiblingsLessThan15(families2))
    #
    # def testIsThereDuplicateNameAndBirthDate(self):
    #     individuals1 = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
    #                                        "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
    #                     GedcomClass.Person("I4", "F1", "Father", "Isme", 15,
    #                                        "1920-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                     GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
    #                                        "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                     ]
    #     individuals2 = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
    #                                        "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
    #                     GedcomClass.Person("I4", "F1", "Whatever", "Isme", 15,
    #                                        "1920-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                     GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
    #                                        "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                     ]
    #     self.assertTrue(GedcomMain.isThereDuplicateNameAndBirthDate(individuals1))
    #     self.assertFalse(GedcomMain.isThereDuplicateNameAndBirthDate(individuals2))
    #
    # def testIsUniqueIDs(self):
    #     individualsTrue = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
    #                                           "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
    #                        GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
    #                                           "1940-3-5", "1985-2-27", "NA", "1995-3-3"),
    #                        GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
    #                                           "1989-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
    #                        GedcomClass.Person("I4", "F1", "Ghost", "Isme", 15,
    #                                           "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                        GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
    #                                           "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                        ]
    #     familiesTrue = [GedcomClass.Family("F1", "1985-2-27",
    #                                        "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5']),
    #                     GedcomClass.Family("F2", "1987-2-27",
    #                                        "NA", "I1", "Father /Isme/", "I2", "Mother /Ash/", ['I5'])
    #                     ]
    #     individualsFalse = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
    #                                            "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
    #                         GedcomClass.Person("I2", "F3", "Mother", "Isme", 15,
    #                                            "1940-3-5", "1985-2-27", "NA", "1995-3-3"),
    #                         GedcomClass.Person("I2", "F2", "Normal", "Isme", 15,
    #                                            "1989-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
    #                         GedcomClass.Person("I4", "F2", "Ghost", "Isme", 15,
    #                                            "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                         ]
    #     familiesFalse = [GedcomClass.Family("F1", "1985-2-27",
    #                                         "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5']),
    #                      GedcomClass.Family("F1", "1987-2-27",
    #                                         "NA", "I1", "Father /Isme/", "I2", "Mother /Ash/", ['I5'])
    #                      ]
    #     self.assertTrue(GedcomMain.isUniqueIDs(individualsTrue, familiesTrue))
    #     self.assertFalse(GedcomMain.isUniqueIDs(individualsFalse, familiesFalse))
    #     self.assertFalse(GedcomMain.isUniqueIDs(individualsTrue, familiesFalse))
    #
    # def testIsSiblingsSpacing(self):
    #     """
    #     Written by CX
    #     :return:
    #     """
    #     individuals = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
    #                                       "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
    #                    GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
    #                                       "1940-3-5", "1985-2-27", "NA", "1995-3-3"),
    #                    GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
    #                                       "1990-8-5", "2000-6-11", "2001-3-4", "2013-4-18"),
    #                    GedcomClass.Person("I4", "F1", "Ghost", "Isme", 15,
    #                                       "1990-8-6", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                    GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
    #                                       "1993-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
    #                    ]
    #     families = [GedcomClass.Family("F1", "1985-2-27",
    #                                    "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
    #     self.assertTrue(GedcomMain.SiblingsSpacing(individuals, families))
    #
    # def testlist_deceased_individual(self):
    #     """
    #     Written by FJ
    #     :return:
    #     """
    #     individuals = [GedcomClass.Person("I1", "F1", "Andy", "Smith", 15,
    #                                       "1980-3-5", "1999-2-27", "NA", "1989-6-4"),
    #                    GedcomClass.Person("I2", "F2", "San", "Zhang", 40,
    #                                       "1981-3-5", "1998-2-27", "NA", "NA")
    #                    ]
    #     self.assertTrue(GedcomMain.list_deceased_individual(individuals))
    #
    # def testmultiple_birth(self):
    #     """
    #     Written by FJ
    #     :return:
    #     """
    #     families = [GedcomClass.Family("F2", "1985-2-27", "NA",
    #                                    "I4", "Father /Isme/",
    #                                    "I3", "Mother /Isme/",
    #                                    ['I3', 'I4', 'I5']),
    #                 GedcomClass.Family("F7", "1985-3-6", "NA",
    #                                    "I5", "Father /Isme/",
    #                                    "I9", "Mother /Isme/",
    #                                    ['I1', 'I4', 'I6', 'I7']),
    #                 ]
    #     self.assertTrue(GedcomMain.multiple_birth(families))

    """
    Sprint 4 Below
    """

    # def testGetRecentBirths(self):
    #     """
    #     Written by HZ
    #     """
    #     individuals = [GedcomClass.Person("I1", "F1", "Andy", "Smith", 15,
    #                                       "2021-11-9", "1999-2-27", "NA", "1989-6-4"),
    #                    GedcomClass.Person("I2", "F2", "San", "Zhang", 40,
    #                                       "1981-3-5", "1998-2-27", "NA", "NA")
    #                    ]
    #     self.assertEqual(GedcomMain.getRecentBirths(individuals)[0].IID, 'I1')
    #
    # def testGetRecentDeaths(self):
    #     """
    #     Written by HZ
    #     """
    #     individuals = [GedcomClass.Person("I1", "F1", "Andy", "Smith", 15,
    #                                       "1985-2-27", "1999-2-27", "NA", "2021-11-25"),
    #                    GedcomClass.Person("I2", "F2", "San", "Zhang", 40,
    #                                       "1981-3-5", "1998-2-27", "NA", "NA")
    #                    ]
    #     self.assertEqual(GedcomMain.getRecentDeaths(individuals)[0].IID, 'I1')

    def testlist_living_single(self):
        """
        Written by FJ
        :return:
        """
        individuals = [GedcomClass.Person("I1", "F1", "Andy", "Smith", 15,
                                          "1980-3-5", "NA", "NA", "NA"),
                       GedcomClass.Person("I2", "F2", "San", "Zhang", 40,
                                          "1981-3-5", "NA", "NA", "NA")
                       ]
        self.assertTrue(GedcomMain.list_living_single(individuals))

    def testlist_name_and_age(self):
        """
        Written by FJ
        :return:
        """
        individuals = [GedcomClass.Person("I1", "F1", "Andy", "Smith", 15,
                                          "1980-3-5", "1999-2-27", "NA", "1989-6-4"),
                       GedcomClass.Person("I2", "F2", "San", "Zhang", 40,
                                          "1981-3-5", "1998-2-27", "NA", "NA")
                       ]
        self.assertTrue(GedcomMain.list_name_and_age(individuals))

    def testListLivingMarried(self):
        """
        Written by CX
        :return:
        """
        individuals1 = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
                                           "1920-3-5", "1985-2-27", "NA", "NA"),
                        GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
                                           "1940-3-5", "1985-2-27", "NA", "NA"),
                        GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
                                           "1990-8-5", "2000-6-11", "2001-3-4", "2013-4-18"),
                        GedcomClass.Person("I4", "F1", "Ghost", "Isme", 15,
                                           "1990-8-6", "1930-6-11", "1935-3-4", "1998-4-18"),
                        GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
                                           "1993-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        ]
        families1 = [GedcomClass.Family("F1", "1985-2-27",
                                        "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        individuals2 = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
                                           "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
                        GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
                                           "1940-3-5", "1985-2-27", "NA", "1989-1-1"),
                        GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
                                           "1990-8-5", "2000-6-11", "2001-3-4", "2013-4-18"),
                        GedcomClass.Person("I4", "F1", "Ghost", "Isme", 15,
                                           "1990-8-6", "1930-6-11", "1935-3-4", "1998-4-18"),
                        GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
                                           "1993-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        ]
        families2 = [GedcomClass.Family("F1", "1988-1-1",
                                        "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.listLivingMarried(individuals1, families1))
        self.assertFalse(GedcomMain.listLivingMarried(individuals2, families2))

    def testListOrphans(self):
        """
        Written by CX
        :return:
        """
        individuals1 = [GedcomClass.Person("I1", "F1", "Father", "Isme", 72,
                                           "1920-3-5", "1985-2-27", "NA", "1992-1-1"),
                        GedcomClass.Person("I2", "F1", "Mother", "Isme", 52,
                                           "1940-3-5", "1985-2-27", "NA", "1992-1-1"),
                        GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
                                           "1990-8-5", "2000-6-11", "2001-3-4", "2013-4-18"),
                        GedcomClass.Person("I4", "F1", "Ghost", "Isme", 30,
                                           "1990-8-6", "1930-6-11", "1935-3-4", "NA"),
                        GedcomClass.Person("I5", "F1", "Monster", "Isme", 5,
                                           "1993-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        ]
        families1 = [GedcomClass.Family("F1", "1985-2-27",
                                        "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        individuals2 = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
                                           "1920-3-5", "1985-2-27", "NA", "NA"),
                        GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
                                           "1940-3-5", "1985-2-27", "NA", "1989-1-1"),
                        GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
                                           "1990-8-5", "2000-6-11", "2001-3-4", "2013-4-18"),
                        GedcomClass.Person("I4", "F1", "Ghost", "Isme", 15,
                                           "1990-8-6", "1930-6-11", "1935-3-4", "1998-4-18"),
                        GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
                                           "1993-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                        ]
        families2 = [GedcomClass.Family("F1", "1985-2-27",
                                        "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.listOrphans(individuals1, families1))
        self.assertFalse(GedcomMain.listOrphans(individuals2, families2))


if __name__ == '__main__':
    unittest.main()
