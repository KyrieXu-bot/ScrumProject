# -*- coding: utf-8 -*- 
# @Time : 9/26/2021 12:31 AM
# @Author : Ethan
# @File : GedcomTest.py
# @Description : CX the class and its functions in GedcomClass.py

import unittest
import GedcomClass
import GedcomMain


class TestExtract(unittest.TestCase):
    def testStoreBirthAndDeathDate(self):
        """
        Written by HZ
        :return:
        """
        person1 = GedcomClass.Person("I1", "F1", "Ethan", "Winters", 80, "1997-7-3", "1998-8-20", "2028-6-12", "1998-8-8")
        person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "2000-3-25", "1950-5-4", "2070-10-10")
        self.assertEqual(person1.birth_date, [3, 7, 1997])
        self.assertEqual(person1.death_date, [8, 8, 1998])
        self.assertEqual(person2.birth_date, [5, 6, 1945])
        self.assertEqual(person2.death_date, [10, 10, 2070])

    def testBirthBeforeMarry(self):
        """
        Written by HZ
        :return:
        """
        person1 = GedcomClass.Person("I1", "F1", "Ethan", "Winters", 80, "1997-7-3", "1998-8-20", "2028-6-12", "1998-8-8")
        person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "1900-3-25", "1950-5-4", "1925-10-10")

        self.assertTrue(person1.isBirthBeforeMarry())
        self.assertFalse(person2.isBirthBeforeMarry())

    def testBirthBeforeDeath(self):
        """
        Written by HZ
        :return:
        """
        person1 = GedcomClass.Person("I1", "F1", "Ethan", "Winters", 80, "1997-7-3", "1998-8-20", "2028-6-12", "1998-8-8")
        person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 70, "1945-6-5", "2000-3-25", "1950-5-4", "1900-10-10")

        self.assertTrue(person1.isBirthBeforeDeath())
        self.assertFalse(person2.isBirthBeforeDeath())

    def testMarryBeforeDeath(self):
        """
        Written by FJ
        :return:
        """
        person1 = GedcomClass.Person("I1", "F1", "Orion", "White", 66, "929-5-18", "1955-2-27", "NA", "1995-9-7")
        person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 11, "2000-3-25", "2070-5-4", "2049-10-10", "NA")
        print(person2.isMarryBeforeDeath())
        self.assertTrue(person1.isMarryBeforeDeath())
        self.assertFalse(person2.isMarryBeforeDeath())

    def testDivorceBeforeDeath(self):
        """
        Written by FJ
        :return:
        """
        person1 = GedcomClass.Person("I1", "F1", "Regulus", "White", 91, "1906-11-4", "1930-6-11", "1935-3-4", "1998-4-18")
        person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 22, "2000-3-25", "2070-5-4", "2049-10-10", "NA")

        self.assertTrue(person1.isDivorceBeforeDeath())
        self.assertFalse(person2.isDivorceBeforeDeath())

    def testMarryBeforeDivorce(self):
        """
        Written by CX
        :return:
        """
        person1 = GedcomClass.Person("I1", "F1", "Regulus", "White", 91, "1906-11-4", "1930-6-11", "1935-3-4", "1998-4-18")
        person2 = GedcomClass.Person("I1", "F1", "Thomas", "Shelby", 22, "2000-3-25", "2070-5-4", "2049-10-10", "NA")

        self.assertTrue(person1.isMarryeBeforeDivorce())
        self.assertFalse(person2.isMarryeBeforeDivorce())

    def testDatesBeforeCurrent(self):
        """
        Written by CX
        :return:
        """
        person1 = GedcomClass.Person("I1", "F1", "Regulus", "White", 91, "1906-11-4", "1930-6-11", "1935-3-4", "1998-4-18")
        self.assertTrue(person1.isDatesBeforeCurrent())

    """
    Sprint 2 Tests below
    """
    def testIsLessThan150YearOld(self):
        """
        Written by HZ
        :return:
        """
        person1 = GedcomClass.Person("I1", "F1", "Regulus", "White", 91, "1800-11-4", "1930-6-11", "1935-3-4",
                                     "1998-4-18")
        self.assertTrue(person1.isLessThan150YearOld())

    def testIsBirthAfterParentsDeath(self):
        """
        Written by HZ
        :return:
        """
        individuals = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1989-6-4"),
                       GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1995-3-3"),
                       GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
                                          "1989-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
                       GedcomClass.Person("I4", "F1", "Ghost", "Isme", 15,
                                          "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
                                          "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       ]
        families = [GedcomClass.Family("F1", "1985-2-27",
                                      "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.isBirthAfterParentsDeath(individuals, families))

    def testIsBirthAfterParentsMarriage(self):
        """
            Written by FJ
            :return:
        """
        individuals = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1989-6-4"),
                       GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1995-3-3"),
                       GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
                                          "1982-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
                       GedcomClass.Person("I4", "F1", "Ghost", "Isme", 15,
                                          "1988-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
                                          "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       ]
        families = [GedcomClass.Family("F1", "1985-2-27",
                                       "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.isBirthAfterParentsMarriage(individuals, families))

    def testIsMarriageAfter14(self):
        """
            Written by FJ
            :return:
        """
        individuals = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1989-6-4"),
                       GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
                                          "1980-3-5", "1985-2-27", "NA", "1995-3-3"),
                       ]
        families = [GedcomClass.Family("F1", "1985-2-27",
                                       "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.isMarriageAfter14(individuals, families))

    def testIsParentsNotTooOld(self):
        """
        Written by CX
        :return:
        """
        individuals = [GedcomClass.Person("I1", "F1", "Father", "Isme", 15,
                                          "1920-3-5", "1985-2-27", "NA", "1989-6-4"),
                       GedcomClass.Person("I2", "F1", "Mother", "Isme", 15,
                                          "1940-3-5", "1985-2-27", "NA", "1995-3-3"),
                       GedcomClass.Person("I3", "F1", "Normal", "Isme", 15,
                                          "1989-8-15", "2000-6-11", "2001-3-4", "2013-4-18"),
                       GedcomClass.Person("I4", "F1", "Ghost", "Isme", 15,
                                          "1990-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       GedcomClass.Person("I5", "F1", "Monster", "Isme", 15,
                                          "1995-3-5", "1930-6-11", "1935-3-4", "1998-4-18"),
                       ]
        families = [GedcomClass.Family("F1", "1985-2-27",
                                       "NA", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4', 'I5'])]
        self.assertTrue(GedcomMain.isParentsNotTooOld(individuals, families))

    def testIsThereBigamy(self):
        """
        Written by CX
        :return:
        """
        families1 = [GedcomClass.Family("F1", "1985-2-27",
                                       "1986-2-27", "I1", "Father /Isme/", "I2", "Mother /Isme/", ['I3', 'I4']),
                    GedcomClass.Family("F2", "1987-2-27",
                                       "NA", "I1", "Father /Isme/", "I2", "Mother /Ash/", ['I5']),
                    ]
        families2 = [GedcomClass.Family("F1", "1985-2-27",
                                        "1995-2-27", "I1", "Father /Buck/", "I2", "Mother /Jenny/", ['I3', 'I4']),
                     GedcomClass.Family("F2", "1990-2-27",
                                        "2000-2-27", "I6", "Father /Bob/", "I2", "Mother /Jenny/", ['I5']),
                     ]
        self.assertFalse(GedcomMain.isThereBigamy(families1))
        self.assertTrue(GedcomMain.isThereBigamy(families2))


if __name__ == '__main__':
    unittest.main()
