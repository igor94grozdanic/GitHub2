from shapely.geometry import LineString
import shapefile #pyshp lib
import pygeoif

class ShapeFile:
    def __init__(self, type, path):
        __type = type
        __path = path

    def getPath(self):
        return self.__path

    def getType(self):
        return self.__type

    def getWktGeometry(self):
        pass

    #def shpTo

#get polygon geometry from a shapefile
p = shapefile.Reader("D://2_b_Posao//QGIS_plugin//Polygon") #reads shapefile

print (type(p))
print (type(p.shapes()))
print (type(p.shapes()))

line = LineString([(7507684.6,4786258.2), (7507816.9,4786144.1)]) #splitting line

print (type(line))

for s in p.shapes(): #loop through all features (1 feature) shapes
    print(pygeoif.geometry.as_shape(s).wkt)
    print(pygeoif.geometry.as_shape(s))
    a = pygeoif.geometry.as_shape(s)

print (pygeoif.geometry.as_shape(p))

# splitting line: 7507684.6,4786258.2 7507816.9,4786144.1

# LINE=((7500200.0 4500000.0, 7499800.0 4500000.0))
# POLYGON((7507663.213699883 4786210.287958311, 7507782.011616671 4786305.273375075, 7507865.884533424 4786208.70045831, 7507727.507449949 4786118.477541551, 7507663.213699883 4786210.287958311))