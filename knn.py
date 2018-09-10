'''Programm main input point'''
import sys
import csv
import argparse
import enum
import errors
import model

def ParseArgs(args = sys.argv) -> model.Arguments:
    '''Parses input arguments to Arguments class object'''

    print('Args are: {}'.format(args))
    parser = argparse.ArgumentParser(args)
    parser.add_argument('-n', dest = 'neighbours', type=int, default = 5)
    parser.add_argument('-m', dest = 'metric', type=str, default = 5)
    parser.add_argument('-t', dest = 'test_set', type=str, default = 5)
    parser.add_argument('-d', dest = 'decision_argument', type=int, default = None)
    parser.add_argument('file', metavar = 'F', nargs=1, type=str, default = None)
    parser_result = parser.parse_args()

    metric: model.MetricType = None
    test_set_type: model.TestSetType = None

    if parser_result.metric == 'taxi':
        metric = model.MetricType.TAXI
    elif parser_result.metric == 'euclid':
        metric = model.MetricType.EUCLID
    else:
        raise errors.ParserError('Wrong metric, use on of (euclid,taxi)')

    if parser_result.test_set == 'train':
        test_set_type = model.TestSetType.TRAIN
    elif parser_result.test_set == 'split':
        test_set_type = model.TestSetType.SPLIT
    elif parser_result.test_set == "cross":
        test_set_type = model.TestSetType.CROSS
    else:
        raise errors.ParserError('Wrong test_set, use one of (test, split, cross)')

    return model.Arguments(
        parser_result.neighbours,
        metric,
        test_set_type,
        parser_result.decision_argument,
        parser_result.file[0]
    )

def load_input_data(path:str, args:model.Arguments) -> list:
    with open(path, 'r') as file:
        with csv.reader(file, delimiter = ',') as stream:
            for row in stream:
                row_as_list = list(row)

                measure = row_as_list[args.decision_attribute]
                attributes = row_as_list.remove(row_as_list[args.decision_attribute])
                
                yield model.Fact(measure, attributes)

if __name__ == '__main__':
    result = ParseArgs()