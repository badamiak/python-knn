import unittest
import sys
import knn

class TestParamsParsing(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        sys.argv = ['knn_test.py', '-n', '3', '-m', 'euclid', '-t', 'train', '-d', '4', 'testFile']
        self.result = knn.ParseArgs()

    def test_parsed_neighbours(self):
        self.assertEqual(self.result.neighbours, 3)

    def test_parsed_metric(self):
        self.assertEqual(self.result.metric, knn.MetricType.EUCLID)

    def test_parsed_data_type(self):
        self.assertEqual(self.result.test_set, knn.TestSetType.TRAIN)

    def test_parsed_decision_attribute(self):
        self.assertEqual(self.result.decision_attribute, 4)

    def test_parsed_file(self):
        self.assertEqual(self.result.data_file, 'testFile')

if __name__ == '__main__':
    unittest.main()