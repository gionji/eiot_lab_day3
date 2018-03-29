import udooEiotLib as udooiot
import json, time

#### USERS PARAMETERS ################
USERNAME  = "EIOT18_giovanni"
PASSWORD  = "123qweASD"
BOARD_ID  = '1d33c9d4e3172182' # you can get this value from the udoo.cluod web interface
######################################

DEVICE_ID = 'ttyMCC-' + BOARD_ID


if __name__ == '__main__':
    [token, companies] = udooiot.login(USERNAME,PASSWORD)

    ## get the company
    company = udooiot.getCompany(companies)

    ## get the gateway list
    networkStatus = udooiot.getGatewaysByCompany(token, company['company_id'])

    ## print the network structure
    print(json.dumps(networkStatus, indent=4, sort_keys=True))

    # Read analog pin 0 ( A0 )
    print str( udooiot.getSensorValue(token,BOARD_ID, DEVICE_ID, 'analog','0') )
    # Read analog pin 1 ( A1 )
    print str( udooiot.getSensorValue(token,BOARD_ID, DEVICE_ID, 'analog','1') )

    #Turn on digital pin 13 ( LED 13 )
    udooiot.sendActuatorWrite(token,BOARD_ID, DEVICE_ID, 'digital','13', '1')

    # Set the servo position, connected to pin 3,  at 1700 degrees
    udooiot.sendActuatorWrite(token,BOARD_ID, DEVICE_ID, 'servo','3', '10')

    # wait a second
    time.sleep(1)

    # Turn on digital pin 13 ( LED 13 )
    udooiot.sendActuatorWrite(token,BOARD_ID, DEVICE_ID, 'digital','13', '0')

    # Set the servo position, connected to pin 3,  at 1700 degrees
    udooiot.sendActuatorWrite(token,BOARD_ID, DEVICE_ID, 'servo','3', '170')
