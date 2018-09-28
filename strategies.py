import model
import errors
import math

class Distance(object):
    def get_distance(self, record: model.Fact, fact: model.Fact) -> model.GradedFact:
        if len(record.attributes) != len(fact.attributes):
            raise errors.IncompatibileData()

class EuclidDistance(Distance):

    def get_distance(self, record: model.Fact, fact: model.Fact) -> model.GradedFact:
        super().get_distance(record, fact)
        
        distance = 0
        for i in range(len(record.attributes)):
            distance += math.pow(float(record.attributes[i]) - float(fact.attributes[i]),2)
        return model.GradedFact(fact, math.sqrt(distance))

class TaxiDistance(Distance):

    def get_distance(self, record: model.Fact, fact:model.Fact) -> model.GradedFact:
        super().get_distance(record, fact)

        distance = 0
        for i in range(len(record.attributes)):
            distance += abs(float(record.attributes[i]) - float(fact.attributes[i]))
        return model.GradedFact(fact, distance)