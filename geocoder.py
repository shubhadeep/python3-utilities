import json, requests

def get_geocoder(service_url='http://maps.googleapis.com/maps/api/geocode/',
                 format='json',
                 sensor='false'):
                 
  def get_request_url():
    return '{0}{1}'.format(service_url, format)
  
  def get_service_response(address2):
    response = requests.get(get_request_url(), 
                            params={'sensor': sensor, 'address': address2})
    return response.text
    
  def get_lat_long_from_result_object(result_object):
    if 'results' in result_object and len(result_object['results']) > 0:
      location = result_object['results'][0]['geometry']['location']
      return (location['lat'], location['lng'])
    return (None, None)
    
  def lookup(address):
    response_object = json.loads(get_service_response(address))
    return get_lat_long_from_result_object(response_object)

  return { 'lookup': lookup,
           'get_request_url': get_request_url,
           'get_service_response': get_service_response,
           'get_lat_long_from_result_object': get_lat_long_from_result_object, }
  
if __name__ == '__main__':
  test_address = 'Gurgaon, India'
  print('Geocoding address: {0}'.format(test_address))
  geocoder = get_geocoder()
  latitude, longitude = geocoder['lookup'](test_address)
  print('latitude: {0}, longitude: {1}'.format(latitude, longitude))
