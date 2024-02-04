import unittest

import phonebook


class MyTestCase(unittest.TestCase):

    def setUp(self):
        phonebook.add_contact("moh", "1234567")
        phonebook.add_contact("loki", "987635")
        phonebook.add_contact("Magnus", "9873453")

    def tearDown(self):
        phonebook.contacts.clear()

    def test_that_contact_was_added_to_phonebook(self):
        phonebook.add_contact("abike", "346738")
        expected = 4
        self.assertEqual(expected, len(phonebook.contacts))

    def test_search_for_contact_by_name(self):
        phonebook.add_contact("loki", "987635")
        expected = "Loki \t 987635"
        self.assertEqual(expected, phonebook.search_for_contact_name("loki"))

        phonebook.add_contact("Magnus", "9873453")
        expected1 = "Magnus \t 9873453"
        self.assertEqual(expected1, phonebook.search_for_contact_name("magnus"))

    def test_search_for_contact_by_number(self):
        expected = "Magnus \t 9873453"
        self.assertEqual(expected, phonebook.search_for_contact_number("9873453"))

    def test_delete_contact_by_name(self):
        phonebook.delete_contact("loki")
        self.assertEqual(2, len(phonebook.contacts))

    def test_delete_contact_by_number(self):
        phonebook.delete_contact_by_number("987635")
        self.assertEqual(2, len(phonebook.contacts))

    def test_edit_contact_name(self):
        phonebook.edit_contact_name("loki", "tobi")
        self.assertEqual(phonebook.contacts[1]["Name"], "Tobi")

    def test_edit_contact_number(self):
        phonebook.edit_contact_number("loki", "11111")
        self.assertEqual(phonebook.contacts[1]["Phone Number"], "11111")


if __name__ == '__main__':
    unittest.main()
