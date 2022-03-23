from word_search import WordBank
from linked_list import LinkedList


word_arr = ["Wing", 'Jumbo', "mark", "juke", "james"]
word_bank = WordBank(word_arr)
print(word_bank.has_word("jumbo"))

print('-----------------------------------------------')

weekdays = LinkedList()
weekdays.add_element("monday")
weekdays.add_element("tuesday")
weekdays.add_element("wednesday")
weekdays.add_element("thursday")
weekdays.add_element("friday")
weekdays.add_element("saturday")
weekdays.add_element("sunday")

print(weekdays.view_list(), '''
----------------------------------------------------------
''')

weekdays.add_element_to_start("head")
print(weekdays.preceding_value("tuesday"), "comes before tuesday")
print(weekdays.next_value("saturday"), "comes after saturday")
weekdays.remove_node("head")
print("the head is", weekdays.fetch_head())
