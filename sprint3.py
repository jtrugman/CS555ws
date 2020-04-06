import test_age
import tag_parse as tag
import age
import family_structure_test
from make_table import print_tables
import family_structure

# File Setup
people, families = tag.read_file('./test_case.ged')
people = age.store_ages(families, people)
print_tables(families, people)


# JD User Stories
# Sprint 1
print(family_structure.fiveLessBirths(people, families))
print(family_structure.fifteenLessSiblings(families))
# Sprint 2
print(family_structure.noChildMarry(families))
print(age.datesBeforeCurrent(people, families))
# Sprint 3
print(family_structure.uniqueFam(people, families))
print(family_structure.uniqueFirst(people, families))


# RT User Stories
# Sprint 1
for x in family_structure.parents_not_too_old(people, families):
    print(x)
for x in family_structure.male_last_names_align(people, families):
    print(x)
# Sprint 2
for x in family_structure.noSiblingMarriage(families):
    print(x)
for x in family_structure.correctGender(families, people):
    print(x)
# Sprint 3
for x in family_structure.noCousinMarriage(families):
    print(x)
for x in family_structure.noNieceNephewMarriage(families):
    print(x)


# JT User Stories
# Sprint 1
for person in people:
    print(age.less_than_one_fifty(person, people))
for person in people:
    print(age.marrige_after_fourteen(person, people))
# Sprint 2
print(family_structure.uniqueIndividualIDs(people))
print(family_structure.uniqueFamilyIDs(families))
print(family_structure.listDeceased)
# Sprint 3
print(age.listRecentBirths(people))
for person in people:
    print(age.validateDates(person, people))


# #KV User Stories
# #US30 -List living married
# #US31 -List living single
# people, families = tag.read_file('./sprint3/kv_sprint3.ged')
# people = age.store_ages(families, people)
# print('KV User Stories: US30 - List living married and US31 -List living single')
# print_tables(families, people)
# print("US30 - List living Married: ", family_structure_test.test_ListLivingMarried(people))
# print("US31 - List living Single over 30: ", family_structure_test.test_ListLivingSingle(people))
# print('\n##########################################################################\n')
#
#
# #RT User Stories
# print("RT user stories US19 & US20")
# people, families = tag.read_file('./sprint3/rtSprint3.ged')
# people = age.store_ages(families, people)
# print_tables(families, people)
# #US19 - First cousins should not marry
# family_structure_test.noCousinMarriageTest(families)
# #US20 - Aunts and uncles should not marry nieces and nephews
# family_structure_test.noNieceNephewMarriageTest(families)
# print('\n##########################################################################\n')
#
#
# # JD User Stories
# print('JD User Stories 24 & 25')
# people, families = tag.read_file('./sprint3/jd_sprint3.ged')
# people = age.store_ages(families, people)
# print_tables(families, people)
# # US24
# print(family_structure_test.test_unique_fam(people, families))
# # US25
# print(family_structure_test.test_unique_first(people, families))
# print('\n##########################################################################\n')
#
#
# # JT User Stories
# #US35
# people, families = tag.read_file('./sprint3/jt_list_recent_births.ged')
# people = age.store_ages(families, people)
# print('JT user stories US35 and US42')
# print_tables(families, people)
# print("US35 - Recent Births:", age.listRecentBirths(people))
#
# # run validate age last because it will exit out the program when an invalid age is entered
# # this is because there is no point in continuing with the rest of the program when the dates are invalid
# #US 42
# people, families = tag.read_file('./sprint3/jt_validate_age.ged')
# people = age.store_ages(families, people)
# print_tables(families, people)
# print('US42 - Reject illegitamite Dates:', age.calc_ages(people))
