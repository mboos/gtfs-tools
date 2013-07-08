class Agency(object):
  def __init__(self, data, ):
    self.__dict__.update(data)
    
    self.stops = []
  
  def columnData(self, ):
    yield self.__dict__
    
  def addStop(self, stop):
    stops.append(stop)
  