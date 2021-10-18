# -*- coding: utf-8 -*- 
# @Time : 9/26/2021 12:31 AM
# @Author : Ethan
# @File : GedcomTest.py
# @Description : CX the class and its functions in GedcomClass.py

import unittest
import GedcomClass


class TestExtract(unittest.TestCase):
    def testStoreBirthAndDeathDate(self):
        """
        Written by HZ
        :return:
        """
        person1 = GedcomClass.Person("Ethan", "Winters", 80, "1997-7-3", "1998-8-20", "2028-6-12", "1998-8-8")
        person2 = GedcomClass.Person("Thomas", "Shelby", 70, "1945-6-5", "2000-3-25", "1950-5-4", "2070-10-10")
        self.assertEqual(person1.birth_date, [3, 7, 1997])
        self.assertEqual(person1.death_date, [8, 8, 1998])
        self.assertEqual(person2.birth_date, [5, 6, 1945])
        self.assertEqual(person2.death_date, [10, 10, 2070])

    def testBirthBeforeMarry(self):
        """
        Written by HZ
        :return:
        """
        person1 = GedcomClass.Person("Ethan", "Winters", 80, "1997-7-3", "1998-8-20", "2028-6-12", "1998-8-8")
        person2 = GedcomClass.Person("Thomas", "Shelby", 70, "1945-6-5", "1900-3-25", "1950-5-4", "1925-10-10")

        self.assertTrue(person1.isBirthBeforeMarry())
        self.assertFalse(person2.isBirthBeforeMarry())

    def testBirthBeforeDeath(self):
        """
        Written by HZ
        :return:
        """
        person1 = GedcomClass.Person("Ethan", "Winters", 80, "1997-7-3", "1998-8-20", "2028-6-12", "1998-8-8")
        person2 = GedcomClass.Person("Thomas", "Shelby", 70, "1945-6-5", "2000-3-25", "1950-5-4", "1900-10-10")

        self.assertTrue(person1.isBirthBeforeDeath())
        self.assertFalse(person2.isBirthBeforeDeath())

    def testMarryBeforeDeath(self):
        """
        Written by FJ
        :return:
        """
        person1 = GedcomClass.Person("Orion", "White", 66, "929-5-18", "1955-2-27", "NA", "1995-9-7")
        person2 = GedcomClass.Person("Thomas", "Shelby", 11, "2000-3-25", "2070-5-4", "2049-10-10", "NA")
        print(person2.isMarryBeforeDeath())
        self.assertTrue(person1.isMarryBeforeDeath())
        self.assertFalse(person2.isMarryBeforeDeath())

    def testDivorceBeforeDeath(self):
        """
        Written by FJ
        :return:
        """
        person1 = GedcomClass.Person("Regulus", "White", 91, "1906-11-4", "1930-6-11", "1935-3-4", "1998-4-18")
        person2 = GedcomClass.Person("Thomas", "Shelby", 22, "2000-3-25", "2070-5-4", "2049-10-10", "NA")

        self.assertTrue(person1.isDivorceBeforeDeath())
        self.assertFalse(person2.isDivorceBeforeDeath())

    def testMarryBeforeDivorce(self):
        """
        Written by CX
        :return:
        """
        person1 = GedcomClass.Person("Regulus", "White", 91, "1906-11-4", "1930-6-11", "1935-3-4", "1998-4-18")
        person2 = GedcomClass.Person("Thomas", "Shelby", 22, "2000-3-25", "2070-5-4", "2049-10-10", "NA")

        self.assertTrue(person1.isMarryeBeforeDivorce())
        self.assertFalse(person2.isMarryeBeforeDivorce())

    def testDatesBeforeCurrent(self):
        """
        Written by CX
        :return:
        """
        person1 = GedcomClass.Person("Regulus", "White", 91, "1906-11-4", "1930-6-11", "1935-3-4", "1998-4-18")
        self.assertTrue(person1.isDatesBeforeCurrent())


if __name__ == '__main__':
    unittest.main()
