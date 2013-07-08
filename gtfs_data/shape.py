from pyproj import Proj
from shapely.geometry import LineString
from math import sqrt
import numpy

class Shape(object):
  def __init__(self, points, zone=17):
    self.shape_id = points[0]['shape_id']
    self.latlon = []
    self.seqnums = []
    self.dists = []

    for point in points:
      self.seqnums.append(point['shape_pt_sequence'])
      pt = [float(point['shape_pt_lon']), float(point['shape_pt_lat'])]
      self.latlon.append(pt)
      if (not point.has_key('shape_dist_traveled')
          or len(point['shape_dist_traveled']) > 0):
        self.dists.append(point['shape_dist_traveled'])
    
    p = p or Proj(proj='utm',zone=zone,ellps='WGS84')
    a = numpy.array(self.latlon)
    x, y = p(a[:,0], a[:,1])
    self._xy = zip(x,y)
    
    #if distances aren't listed, compute them
    if len(self.dists) == 0:
      dist = 0
      self.dists.append(0.0)
      for pt1, pt2 in zip(self._xy[:-1], self._xy[1:]):
        x = pt1[0] - pt2[0]
        y = pt1[1] - pt1[1]
        dist += sqrt(x*x+y*y)
        self.dists.append(dist)
    
  def lineString(self, ):
    return LineString(self._xy)
  
  def columnData(self, ):
    for seq, pt, dist in zip(self.seqnums, self.latlon, self.dists):
      yield {
        'shape_id': self.shape_id,
        'shape_pt_lat': pt[1],
        'shape_pt_lon': pt[0],
        'shape_pt_sequence': seq,
        'shape_dist_traveled': int(dist),
      }