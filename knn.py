'''Programm main input point'''
import sys
import csv
import argparse
import enum
import errors
import model
import strategies

def ParseArgs(args = sys.argv) -> model.Arguments:
    '''Parses input arguments to Arguments class object'''

    print('Args are: {}'.format(args))
    print('setting-up parser')
    parser = argparse.ArgumentParser(args)
    parser.add_argument('-n', dest = 'neighbours', type=int, default = 5)
    parser.add_argument('-m', dest = 'metric', type=str, default = "euclid")
    parser.add_argument('-t', dest = 'test_set', type=str, default = "train")
    parser.add_argument('-d', dest = 'decision_argument', type=int, default = 0)
    parser.add_argument('file', metavar = 'F', nargs=1, type=str, default = None)

    print('parsing args')
    parser_result = parser.parse_args()

    metric: model.MetricType = None
    test_set_type: model.TestSetType = None

    print('parsing metric')
    if parser_result.metric == 'taxi':
        metric = model.MetricType.TAXI
    elif parser_result.metric == 'euclid':
        metric = model.MetricType.EUCLID
    else:
        raise errors.ParserError('Wrong metric, use on of (euclid,taxi)')
    
    print('parsing set')
    if parser_result.test_set == 'train':
        test_set_type = model.TestSetType.TRAIN
    elif parser_result.test_set == 'split':
        test_set_type = model.TestSetType.SPLIT
    elif parser_result.test_set == "cross":
        test_set_type = model.TestSetType.CROSS
    else:
        raise errors.ParserError('Wrong test_set, use one of (test, split, cross)')

    print('parsed')
    return model.Arguments(
        parser_result.neighbours,
        metric,
        test_set_type,
        parser_result.decision_argument,
        parser_result.file[0]
    )

def load_input_data(args:model.Arguments) -> list:
    facts = list()
    with open(args.data_file, 'r') as file:
        stream = csv.reader(file, delimiter = ',')
        for row in stream:
            if row == "":
                continue
            
            measure = row[args.decision_attribute]
            row.remove(row[args.decision_attribute])
            attributes = list()
            for att in row:
                attributes.append(float(att))

            print (measure)
            print (attributes)
            
            facts.append(model.Fact(measure, attributes))
    
    print ("Decision attribute: {}".format(args.decision_attribute))    
    return facts

def grade_new_fact(fact: model.Fact, known_facts: list, metric:strategies.Distance, neighboursCount:int):
    grades: list = list()
    for known_fact in known_facts:
        grade = metric.get_distance(fact, known_fact)
        grades.append(grade)
        print (grade)

    def sort_function(x:model.GradedFact):
        return x.grade

    neighbours = sorted(grades, key=sort_function)[:neighboursCount]

    result = dict()
    for f in neighbours:
        print('neighbour: {}'.format(f))
        # casted = model.GradedFact(f)
        key = f.fact.measure
        if key in result:
            result[key] += 1
        else:
            result[key] = 1

    print(result)

    return result

    
if __name__ == '__main__':
    
    args = ParseArgs()

    metric: strategies.Distance = None
    facts = load_input_data(args)

    for fact in list(facts):
        print(fact)

    print('setting up metric')
    if args.metric == model.MetricType.EUCLID:
        metric = strategies.EuclidDistance()
    elif args.metric == model.MetricType.TAXI:
        metric = strategies.TaxiDistance()
    else:
        raise errors.UnknownMetric()

    testCase = facts[0]
    print("Test fact: {}".format(testCase))

    grade = grade_new_fact(testCase,facts,metric,args.neighbours)
    print(grade)
    
