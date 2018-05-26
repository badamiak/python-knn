'''Programm main input point'''
import sys
import argparse
import enum
import errors.errors as err

class MetricType(enum.IntEnum):
    TAXI = 0
    EUCLID =1

class TestSetType(enum.IntEnum):
    TRAIN = 0
    SPLIT = 1
    CROSS = 2

class Arguments(object):
    def __init__(self, neighbours: int, metric: MetricType, test_set: TestSetType, decision_attribute: int, data_file: str):
        self.neighbours = neighbours
        self.metric = metric
        self.test_set = test_set 
        self.decision_attribute = decision_attribute
        self.data_file = data_file

def ParseArgs(args = sys.argv) -> Arguments:
    '''Parses input arguments to Arguments class object'''

    print('Args are: {}'.format(args))
    parser = argparse.ArgumentParser(args)
    parser.add_argument('-n', dest = 'neighbours', type=int, default = 5)
    parser.add_argument('-m', dest = 'metric', type=str, default = 5)
    parser.add_argument('-t', dest = 'test_set', type=str, default = 5)
    parser.add_argument('-d', dest = 'decision_argument', type=int, default = None)
    parser.add_argument('file', metavar = 'F', nargs=1, type=str, default = None)
    parser_result = parser.parse_args()

    metric: MetricType = None
    test_set_type: TestSetType = None

    if parser_result.metric == 'taxi':
        metric = MetricType.TAXI
    elif parser_result.metric == 'euclid':
        metric = MetricType.EUCLID
    else:
        raise err.ParserError('Wrong metric, use on of (euclid,taxi)')

    if parser_result.test_set == 'train':
        test_set_type = TestSetType.TRAIN
    elif parser_result.test_set == 'split':
        test_set_type = TestSetType.SPLIT
    elif parser_result.test_set == "cross":
        test_set_type = TestSetType.CROSS
    else:
        raise err.ParserError('Wrong test_set, use one of (test, split, cross)')

    return Arguments(
        parser_result.neighbours,
        metric,
        test_set_type,
        parser_result.decision_argument,
        parser_result.file[0]
    )
    
if __name__ == '__main__':
    result = ParseArgs()