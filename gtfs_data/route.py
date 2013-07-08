class Route(object):
  def __init__(self, data, agency):
    self.__dict__.update(data)
    self.agency = agency
    
    self.trips = []
    
  def addTrip(self, trip):
    bisect.insort(trips, trip)
  
  def columnData(self, ):
    yield self.__dict__