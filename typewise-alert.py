from temperature_breach import classify_temperature_breach

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')

def send_to_email(breachType):
  recepient = "a.b@c.com"
  print(f'To: {recepient}')
  if breachType == 'TOO_LOW':
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print('Hi, the temperature is too high')
