# -*- coding: utf-8 -*- 
# @Time : 9/26/2021 12:31 AM
# @Author : Ethan
# @File : GedcomTest.py
# @Description : Test the class and its functions in GedcomClass.py

import unittest
import GedcomClass


class TestExtract(unittest.TestCase):
    # def testName(self):
    #     person1 = GedcomClass.Person("Ethan", "Winters", "20 8 1998", "12 6 2028", "8 8 1998")
    #     person2 = GedcomClass.Person("Thomas", "Shelby", "25 3 2000", "4 5 1950", "10 10 2070")
    #     self.assertEqual(person1.first_name, "Ethan")
    #     self.assertEqual(person1.last_name, "Winters")
    #     self.assertEqual(person2.first_name, "Thomas")
    #     self.assertEqual(person2.last_name, "Shelby")

    # def testBirthBeforeDeath(self):
    #     person1 = GedcomClass.Person("Ethan", "Winters", "20 8 1998", "12 6 2028", "8 8 1998")
    #     person2 = GedcomClass.Person("Thomas", "Shelby", "25 3 2000", "4 5 1950", "10 10 2070")
    #     self.assertEqual(person1.birth_date[0], 20)
    #     self.assertEqual(person1.birth_date[1], 8)
    #     self.assertEqual(person1.birth_date[2], 1998)
    #
    #     self.assertFalse(person1.isBirthBeforeDeath())
    #     self.assertTrue(person2.isBirthBeforeDeath())

    def testMarryBeforeDeath(self):
        person1 = GedcomClass.Person("Orion", "White", 66, "18-5-1929", "27-2-1955", "NA", "7-9-1995")
        person2 = GedcomClass.Person("Thomas", "Shelby", 11, "25-3-2000", "4-5-2070", "10-10-2049", "NA")
        print(person2.isMarryBeforeDeath())
        self.assertTrue(person1.isMarryBeforeDeath())
        self.assertFalse(person2.isMarryBeforeDeath())

    def testDivorceBeforeDeath(self):
        person1 = GedcomClass.Person("Regulus", "White", 91, "4-11-1906", "11-6-1930", "4-3-1935", "18-4-1998")
        person2 = GedcomClass.Person("Thomas", "Shelby", 22, "25-3-2000", "4-5-2070", "10-10-2049", "NA")

        self.assertTrue(person1.isDivorceBeforeDeath())
        self.assertFalse(person2.isDivorceBeforeDeath())

    # def testIsLessThan150YearOld(self):
    #     """
    #     This test is based on the tests written before
    #     :return: Whether the age is less than 150
    #     """
    #     person1 = GedcomClass.Person("Ethan", "Winters", "20 8 1998", "12 6 2000", "8 8 2050")
    #     person2 = GedcomClass.Person("Thomas", "Shelby", "25 3 1800", "4 5 2070", "10 10 2049")
    #
    #     self.assertTrue(person1.isLessThan150YearOld())
    #     self.assertFalse(person2.isLessThan150YearOld())


if __name__ == '__main__':
    unittest.main()
