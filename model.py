import enum

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

class Fact(object):
    def __init__(self, measure, attributes: list):
        self.measure = measure
        self.attributes = attributes