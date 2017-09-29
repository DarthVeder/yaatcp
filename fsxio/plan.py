#*_* coding: utf-8 *_*
import xml.etree.cElementTree as et
import spherical.math as sphere


def readFSXplan(file_name):
    """
    Reads a pln file in FSX format. Returns a tuple of positions (lat, lon).
    The first waypoint is the departure airport and the last waypoint is the
    destination airport.
    """
    fin = open(file_name,'r')

    tree = et.parse(fin)
    root = tree.getroot()

    waypoint = []
    print(len(root), root.tag)    
    for node in root:
        if (node.tag == 'FlightPlan.FlightPlan'):
            print('Found '+str(len(node))+' nodes')
            print('Dep: '+node.find('DepartureID').text)
            print('Dest: '+node.find('DestinationID').text)

            wp = node.findall('ATCWaypoint')
            print('Found '+str(len(wp))+' waypoints')
            for w in wp:
                print('WPY '+w.find('ICAO').find('ICAOIdent').text)
                lat, lon, h = w.find('WorldPosition').text.split(',')
                lat = sphere.convertDPS2numeric(lat)
                lon = sphere.convertDPS2numeric(lon)
                print(lat, lon)
                waypoint.append((lat,lon))

    return waypoint
    
if __name__ == '__main__':
    file_name = 'GMMNKJFK_FSX_1494417057.pln'

    wp = readFSXplane(file_name)

    for w in wp:
        print(w)
