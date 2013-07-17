from datetime import datetime

weekdays = ['monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday']

class Service(object):
  def __init__(self, **data ):
    self.__dict__.update(data)
    if not self.__dict__.has_key('_start_date'):
      self._start_date = datetime.strptime(self.start_date, '%Y%m%d').date()
    if not self.__dict__.has_key('_end_date'):
      self._end_date = datetime.strptime(self.end_date, '%Y%m%d').date()
    
    self.trips = []
    
    self.addExceptions = []
    self.removeExceptions = []
  
  def columnData(self, ):
    yield self.__dict__
    
  def addTrip(self, trip):
    self.trips.append(trip)
    
  def addDate(self, exception):
    self.addExceptions.append(exception)
  
  def removeDate(self, exception):
    self.removeExceptions.append(exception)
    
  def hasDate(self, date):
    for exception in self.addExceptions:
      if exception.hasDate(date):
        return true

    if date < self._start_date or date > self._end_date:
      return false
    if self.__dict__[weekdays[date.weekday()]] == '0':
      return false
    for exception in self.removeExceptions:
      if exception.hasDate(date):
        return false
    
    return true
  
  
class CalendarException(object):
  def __init__(self, service, **data):
    self.__dict__.update(data)
    self._date = datetime.strptime(self.date, '%Y%m%d').date()
    
    self.service = service
    if int(self.exception_type) == 1:
      service.addDate(self)
    else:
      service.removeDate(self)
  
  def columnData(self, ):
    yield self.__dict__
    
  def hasDate(self, date):
    return self._date == date
  

