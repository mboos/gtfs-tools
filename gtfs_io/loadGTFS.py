import os
import csv
from gtfs_data import *


def loadAgencies(folder):
  rows, headings = csv.readCSV(os.path.join(folder, 'agency.txt'),
                               idColumn='agency_id')
  return {k: Agency(**d) for k, d in rows.items()}
  
def loadStops(folder, zones={}):
  rows, headings = csv.readCSV(os.path.join(folder, 'stops.txt'),
                               idColumn='stop_id')
  #TODO: handle zones
  return {k: Stop(**d) for k, d in rows.items()}

def loadRoutes(folder, agencies):
  rows, headings = csv.readCSV(os.path.join(folder, 'routes.txt'),
                               idColumn='route_id')
  return {k: Route(agency=agencies[d['agency_id']], **d)
          for k, d in rows.items()}

def loadTrips(folder, routes, services):
  rows, headings = csv.readCSV(os.path.join(folder, 'trips.txt'),
                               idColumn='trip_id')
  return {k: Trip(route=routes[d['route_id']], service=services[d['service_id']], **d)
          for k, d in rows.items()}

def loadStopTimes(folder, trips, stops):
  rows, headings = csv.readCSV(os.path.join(folder, 'stop_times.txt'))
  return [StopTime(trip=trips[d['trip_id']], stop=stops[d['stop_id']], **d)
          for d in rows]

def loadCalendar(folder):
  rows, headings = csv.readCSV(os.path.join(folder, 'calendar.txt'),
                                            idColumn='service_id')
  return {k: Service(**d) for k,d in rows.items()}

def loadExceptions(folder, services):
  rows, headings = csv.readCSV(os.path.join(folder, 'calendar_dates.txt'))
  return [CalendarException(service=services[d['service_id']], **d)
          for d in rows]



def loadGTFS(folder):
  agencies = loadAgencies(folder)
  services = loadCalendar(folder)
  exceptions = loadExceptions(folder, services)
  stops = loadStops(folder)
  routes = loadRoutes(folder, agencies)
  trips = loadTrips(folder, routes, services)
  stopTimes = loadStopTimes(folder, trips, stops)
  
  print 'Agencies:', len(agencies)
  print 'Services:', len(services)
  print 'Exceptions:', len(exceptions)
  print 'Stops:', len(stops)
  print 'Routes:', len(routes)
  print 'Trips:', len(trips)
  print 'Stop Times:', len(stopTimes)
  #TODO fares, zones, frequencies, etc.

if __name__ == '__main__':
  import argparse
  
  parser = argparse.ArgumentParser()
  parser.add_argument(dest='folder')
  args = parser.parse_args()
  loadGTFS(args.folder)
