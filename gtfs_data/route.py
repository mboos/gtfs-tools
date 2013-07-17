import bisect

class Route(object):
  def __init__(self, agency = None, **data):
    self.__dict__.update(data)
    self.agency = agency
    if agency:
      agency.addRoute(self)
    
    self.trips = []
    
  def addTrip(self, trip):
    bisect.insort(self.trips, trip)
  
  def columnData(self, ):
    yield self.__dict__