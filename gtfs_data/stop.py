from pyproj import Proj
from shapely.geometry import Point
import bisect

class Stop(object):
  def __init__(self, zone=None, utm_zone=17, **data):
    self.__dict__.update(data)
    
    if zone:
      zone.stops.append(self)
    self.zone = zone
    
    p = Proj(proj='utm',zone=utm_zone,ellps='WGS84')
    self._xy = list(p(self.stop_lon, self.stop_lat))
    
    self.stop_times = []
    
  def addStopTime(self, stop_time):
    bisect.insort(self.stop_times, stop_time)
    
  def point(self, ):
    return Point(self._xy)
  
  def columnData(self, ):
    yield self.__dict__