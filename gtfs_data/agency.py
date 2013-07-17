class Agency(object):
  def __init__(self, **data):
    self.__dict__.update(data)
    
    self.routes = []
  
  def columnData(self, ):
    yield self.__dict__
    
  def addRoute(self, route):
    self.routes.append(route)
  