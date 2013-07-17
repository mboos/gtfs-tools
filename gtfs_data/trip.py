import bisect

class Trip(object):
  def __init__(self, route, service=None, **data):
    self.__dict__.update(data)
    
    route.addTrip(self)
    self.route = route
    
    if service:
      service.addTrip(self)
    self.service = service
    
    self.stop_times = []
  
  def addStopTime(self, stop_time):
    bisect.insort(self.stop_times, stop_time)
  
  def columnData(self, ):
    yield self.__dict__