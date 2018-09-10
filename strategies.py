import model
import errors
import math

class Distance(object):

    @staticmethod
    def get_distance(record: model.Fact, fact: model.Fact):
        if len(record.attributes) != len(fact.attributes):
            raise errors.IncompatibileData()

class EuclidDistance(Distance):

    @staticmethod
    def get_distance(record: model.Fact, fact: model.Fact):
        super().get_distance(record, fact)
        
        distance = 0
        for i in range(len(record.attributes)):
            distance += math.pow(record.attributes[i]-fact.attributes[i], 2)

        return math.sqrt(distance)

class TaxiDistance(Distance):

    @staticmethod
    def get_distance(record, fact):
        super().get_distance(record, fact)

        distance = 0
        for i in range(len(record.attributes)):
            distance += abs(record.attributes[i] - fact.attributes[i])
        return distance