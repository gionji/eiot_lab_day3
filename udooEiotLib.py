import requests
import json
from time import gmtime, strftime
import time


BASE_URL    = "https://udoo.cloud"
API_URL     = "/ext"
API_VERSION = "/v1"
IOT_URL = BASE_URL + API_URL + API_VERSION


def login(username, password):
    url = BASE_URL + '/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'username': username, 'password': password}
    #print(payload)

    result = requests.post(url, headers=headers, data=payload)
    try:
        data = json.loads(result.text)
        print(data)
        if data['status']:
            return [data['token'], data['companies']]
        else:
            exit()
    except ValueError as e:
        print(e)
        print(result)

def composeHeader(token):
    header = {'Authorization': 'JWT ' + token}
    return header

def getCompany(companies):
    if len(companies) > 1:
        print('COMPANIES FOUND:')
        for i, company in enumerate(companies):
            if company[2]:
                print(str(i) + ' - ' + company[0] + '(default)')
            else:
                print(str(i) + ' - ' + company[0])

        companyId = input('Select Company:')
        company = companies[companyId]
    else:
        company = companies[0]
        print('Company selected automatically: ' + company['displayName'])

    return company


def getGatewaysByCompany(token, companyId):
    url = IOT_URL + '/network/' + companyId
    # print(url)
    # print(composeHeader(token))
    result = requests.get(url, headers=composeHeader(token))
    network = json.loads(result.text)
    if 'gateways' not in network:
        network['gateways'] = []
    if 'gateway_aliases' not in network:
        network['gateway_aliases'] = []
    if 'node_aliases' not in network:
        network['node_aliases'] = []

    return network['gateways'] #, network['gateway_aliases'], network['node_aliases']


def getSensorValue(token, gateway, device, sensor_type, sensor_id):
    url = IOT_URL + '/sensors/read/' + gateway + '/' + device + '/' + sensor_type + '/' + sensor_id

    # print(url)
    # print(composeHeader(token))
    result = requests.get(url, headers=composeHeader(token))
    try:
        data = json.loads(result.text)
        return int(str(data['value']).replace('[', '').replace(']', ''))
    except ValueError as e:
        print(e)


def getSensorHistory(token, gateway, device, sensor_type, sensor_id, history_type, limit):
    url = IOT_URL + '/sensors/history/' + history_type + '/' + gateway + '/' + device + '/' + sensor_type + '/' + sensor_id + '/' + str(limit)

    # print(url)
    # print(composeHeader(token))
    result = requests.get(url, headers=composeHeader(token))
    try:
        data = json.loads(result.text)
        return data
    except ValueError as e:
        print(e)


def sendActuatorWrite(token, gateway, device, actuator_type, actuator_id, value):
    url = IOT_URL + '/sensors/write/' + gateway + '/' + device + '/' + actuator_type + '/' + actuator_id + '/' + value

    # print(url)
    # print(composeHeader(token))
    result = requests.get(url, headers=composeHeader(token))
    try:
        data = json.loads(result.text)
        return data
    except ValueError as e:
        print(e)