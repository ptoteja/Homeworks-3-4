import unittest
import re

## SI 206 - W17 - HW3
## COMMENT WITH:
## Name: Prashant Toteja
## Your section day/time: Thursday 6-7pm
## Any names of people you worked with on this assignment: None

#####################


## PART 1: 300 points

## Use regular expressions to define a function called parse_counted_words which should accept a string, find strings of the form: <count> <word>  e.g. 101 Dalmations, inside it, and should return either the LAST correctly matching number-word combo in the string as a tuple, e.g. ('13', "pineapples"), if there are any such sub-strings, or None, if there are not.
## The number in the <count> should be one or more digits only. The word should be made up of an optional non-alphabetic character followed by any number of alphabetic characters, upper or lower case.
## HINT:  \b matches the beginning or end of a word
## HINT:  you can use the Python re .findall method to get multiple matches in a string
#parse_counted_words('5 watermelons, 13 pineapples, and 1 papaya.') should return ('1', 'papaya')
# parse_counted_words('101 dalmations!') should return ('101', 'dalmations') ...

## Write code to define your parse_counted_words function here.

def parse_counted_words(s):
    list_it = re.findall(r'\b\d+\s\D+\b', s)   #looks at digits (1 or more), space, non-digit (1 or more)
    #split_list = tuple_list.split()
    if len(list_it) == 0:
        return None
    else:
        last_string_in_type_list = list_it[-1]
        list_of = last_string_in_type_list.split()
        a = list_of[0]
        b = list_of[1]
        return_tuple = (a,b)
        return return_tuple


#print(parse_counted_words('goldilocks and the 3 little pigs'))
#print(parse_counted_words('678 1234567 890  '))
#print(parse_counted_words("hellllo 5000"))
#print(parse_counted_words('5 watermelons, 13 pineapples, and 1 papaya.'))
## PART 2: 200 points

## We have provided a text file computer_paths.txt. It's not incredibly long -- you can scan through it, but do NOT hard code your answers! Each line contains 1 filesystem path.

## (a) Write Python code to determine how many of these paths identify FILES, not directories. Save that number in the variable file_paths_num.

f = open("/Users/atoteja/Desktop/Homework3/computer_paths.txt", 'r')
data = f.read()

files_list = re.findall(r'\.[a-z]', data, re.MULTILINE)

file_paths_num = len(files_list)


## (b) Write Python code to determine how many of these paths are FULL paths, not relative paths. Save that number in the variable full_paths_num.
#full_paths = re.findall(r'\.[a-z]', data)
full_paths = re.findall(r'(\$/.*?\.\S*)', data)
print(full_paths)

## (c) Write Python code to determine how many of these paths describe a Python file saved inside a folder called SI206. Save that number in the variable python_course_paths.

new_list = re.findall(r'\/[A-Z][a-z]{1,5}\/[A-Z][a-z]{1,6}\/[A-Z][a-z]{1,9}\/[A-Z]{1,3}[0-9]{1,3}\/', data)
python_course_paths = len(new_list)


## (d) Write Python code to determine how many of these paths describe a Microsoft file (a file that EITHER ends with .docx OR .xlsx, but nothing else counts) where the file name ends in a digit. Save that total in the variable microsoft_files_num.

d = re.findall(r'\d\.docx|\d\.xlsx', data)
microsoft_files_num = len(d)




## We have provided unit tests in this file. To earn the full 500 points, you'll need to pass all of the tests and will need to have followed the instructions.
## Each class of the tests represents one "part" of the homework, and the points for each part are divided approx. equally between each of the tests.

####### UNIT TESTING BELOW; DO NOT CHANGE ANY TESTING CODE #######

class Part1_HW3(unittest.TestCase):
    def test_pcw_1(self):
        self.assertEqual(parse_counted_words('5 watermelons, 13 pineapples, and 1 papaya.'),('1','papaya'))
    def test_pcw_2(self):
        self.assertEqual(parse_counted_words('101 dalmations!'),('101','dalmations'))
    def test_pcw_3(self):
        self.assertEqual(parse_counted_words('snow white and the 7 #littledwarves'),('7','#littledwarves'))
    def test_pcw_4(self):
        self.assertEqual(parse_counted_words('goldilocks and the 3 little pigs'),('3','little'))
    def test_pcw_5(self): 
        self.assertEqual(parse_counted_words('678 1234567 890  '),None)
    def test_pcw_6(self):
        self.assertEqual(parse_counted_words("hellllo 5000"), None)
    def test_pcw_7(self):
        self.assertEqual(parse_counted_words("!!!! 6"), None)
    def test_pcw_8(self):
        self.assertEqual(parse_counted_words("!!!!! 72 and 76 calendars"),('76',"calendars"))

class Part2_HW3(unittest.TestCase):
    def test_cpaths_1(self): 
        self.assertEqual(file_paths_num,16)
    def test_cpaths_2(self):
        self.assertEqual(full_paths_num,16)
    def test_cpaths_3(self):
        self.assertEqual(python_course_paths,3)
    def test_cpaths_4(self):
        self.assertEqual(microsoft_files_num,3)


if __name__ == "__main__":
    unittest.main(verbosity=2)

