class StopTime(object):
  def __init__(self, data, stop, trip):
    self.__dict__.update(data)
    
    stop.addStopTime(self)
    self.stop = stop
    
    trip.addStopTime(self)
    self.trip = trip
  
  def columnData(self, ):
    yield self.__dict__
    
  def __cmp__(self, other):
    if (self.departure_time < other.departure_time
          and self.arrival_time < other.arrival_time):
      return -1
    elif (self.departure_time > other.departure_time
          and self.arrival_time > other.arrival_time):
      return 1
    else: # Neither stop occurs before the other
      return 0