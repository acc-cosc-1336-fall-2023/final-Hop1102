#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
#no test functions for question A/1, B/2, or D/4
from src.question_c.question_c import test_config, get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_question_c_config(self):
        self.assertEqual(True, test_config())


    def test_find_positions(self):
        dna_string1 = "GATATATGCATATACTT"
        dna_string2 = "ATAT"

        result_positions = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        self.assertEqual(result_positions, (2, 4, 10))