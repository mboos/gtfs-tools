class TransitSystem:
  def __init__(self, agencies, services, exceptions, routes, trips, stops, stopTimes):
    self.agencies = agencies
    self.services = services
    self.exceptions = exceptions
    self.routes = routes
    self.trips = trips
    self.stops = stops
    self.stopTimes = stopTimes
  