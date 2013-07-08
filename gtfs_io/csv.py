def readCSV(fileName, idColumn=None, sep=','):
  '''Reads csv file in fileName.
  If idColumn is defined, use values in column as dict keys
  otherwise, put all values in list
  Define sep to use a different separator from ','
  '''
  if idColumn:
    data = {}
  else:
    data = []
  
  with open(fileName, 'r') as file:
    line = file.readline()
    headings = map(str.strip, line.split(sep))
    if idColumn:
      id = headings.index(idColumn)
    for line in file:
      tokens = map(str.strip, line.split(sep))
      if idColumn:
        row = tokens[id]
      else:
        data.append({})
        row = -1
      data[row] = {}
      for i,h in enumerate(headings):
        data[row][h] = tokens[i]

  return data, headings

def _writeCSVline(fp, line, template):
  fp.write(template.format(**line))


def writeCSV(fileName, data, headings):
  '''Writes csv file in fileName from collections of GTFS objects
  '''
  template = ','.join(map(lambda x: '{' + x + '}', headings)) + '\n'
  
  if type(data) == dict:
    items = data.values()
  elif type(data) == list:
    items = data
  
  with open(filename, 'w') as fp:
    fp.write(','.join(headings) + '\n')
    for item in items:
      for line in item.columnData():
        _writeCSVline(fp, line, template)