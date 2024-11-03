def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):  
  temperature_limits = {'PASSIVE_COOLING':(0,35), 
                        'HI_ACTIVE_COOLING':(0,45), 
                        'MED_ACTIVE_COOLING': (0,40)}
  return infer_breach(temperatureInC, temperature_limits[coolingType][0], temperature_limits[coolingType][1])