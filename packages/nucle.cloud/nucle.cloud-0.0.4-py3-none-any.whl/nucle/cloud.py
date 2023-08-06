import requests
from requests.exceptions import HTTPError


class Models:

    class UserModel:
        def __init__(self, id, userName, displayName, email, creationDate, lastLogin):
            self.id = id
            self.userName = userName
            self.displayName = displayName
            self.email = email
            self.creationDate = creationDate
            self.lastLogin = lastLogin

    class GeolocalizationModel:
        def __init__(self, userID, ip, city, region, country, latitude, longtitude, lastUpdate):
            self.userID = userID
            self.ip = ip
            self.city = city
            self.region = region
            self.country = country
            self.latitude = latitude
            self.longtitude = longtitude
            self.lastUpdate = lastUpdate

    class LoginResult:
        def __init__(self, userToken, user):
            self.userToken = userToken
            self.user = user

    class ExternalLoginModel:
        def __init__(self, loginProvider, providerKey, providerDisplayName, userId):
            self.loginProvider = loginProvider
            self.providerKey = providerKey
            self.providerDisplayName = providerDisplayName
            self.userId = userId

    class PresetModel:
        def __init__(self, id, name, globalValue, valueType, updateType, creationDate, lastUpdate):
            self.id = id
            self.name = name
            self.globalValue = globalValue
            self.valueType = valueType
            self.updateType = updateType
            self.creationDate = creationDate
            self.lastUpdate = lastUpdate

    class PresetsModel:
        def __init__(self, list, count):
            self.list = list
            self.count = count

    class VariableModel:
        def __init__(self, id, userId, value, lastUpdate):
            self.id = id
            self.userId = userId
            self.value = value
            self.lastUpdate = lastUpdate

    class VariablesModel:
        def __init__(self, list, totalCount):
            self.list = list
            self.totalCount = totalCount

 
class User:
    @staticmethod
    def Create(projectId,userName,email,password) -> Models.UserModel:
        URL = "https://api.nucle.cloud/v1/user/create"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "projectId": projectId}
        Json = {"userName": userName,
                "email": email, "password":password}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()

            result = Models.UserModel(r.get('id'), r.get('userName'), r.get(
                'displayName'), r.get('email'), r.get('creationDate'), r.get('lastLogin'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def Login(projectId,email,password ) -> Models.LoginResult:
        URL = "https://api.nucle.cloud/v1/user/login"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "projectId": projectId}
        Json = {"email": email, "password": password}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()

            user = Models.UserModel(r.get('id'), r.get('userName'), r.get(
                'displayName'), r.get('email'), r.get('creationDate'), r.get('lastLogin'))
            result = Models.LoginResult(r.get('userToken'), user)
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def RevokeToken(userToken) -> Models.LoginResult:
        URL = "https://api.nucle.cloud/v1/user/revoketoken"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        try:
            response = requests.post(url=URL, headers=Headers)
            response.raise_for_status()
            r = response.json()

            user = Models.UserModel(r.get('id'), r.get('userName'), r.get(
                'displayName'), r.get('email'), r.get('creationDate'), r.get('lastLogin'))
            result = Models.LoginResult(r.get('userToken'), user)
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def SendResetPassword(projectId,email):
        URL = "https://api.nucle.cloud/v1/user/passwordreset/send"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "projectId": projectId}
        Json = {"email": email}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()

        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def SendEmailConfirmation(projectId,email):
        URL = "https://api.nucle.cloud/v1/user/confirmemail/send"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "projectId": projectId}
        Json = {"email": email}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()

        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def Upgrade(userToken,userName,email,password) -> Models.UserModel:
        URL = "https://api.nucle.cloud/v1/user/upgrade"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        Json = {"userName": userName,
                "email": email, "password": password}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()

            result = Models.UserModel(r.get('id'), r.get('userName'), r.get(
                'displayName'), r.get('email'), r.get('creationDate'), r.get('lastLogin'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def GetById(userToken,userId) -> Models.UserModel:
        URL = "https://api.nucle.cloud/v1/user/get"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        Json = {"id": userId}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()

            result = Models.UserModel(r.get('id'), r.get('userName'), r.get(
                'displayName'), r.get('email'), r.get('creationDate'), r.get('lastLogin'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def GetType(userToken) -> str:
        URL = "https://api.nucle.cloud/v1/user/get/type"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}

        try:
            response = requests.post(url=URL, headers=Headers)
            response.raise_for_status()
            r = response.text

            return r
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def SetDisplayName(userToken,displayName) -> Models.UserModel:
        URL = "https://api.nucle.cloud/v1/user/displayname/set"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        Json = {"displayName": displayName}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()

            result = Models.UserModel(r.get('id'), r.get('userName'), r.get(
                'displayName'), r.get('email'), r.get('creationDate'), r.get('lastLogin'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def GetGeolocalizationData(userToken) -> Models.GeolocalizationModel:
        URL = "https://api.nucle.cloud/v1/user/geolocalization/get"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}

        try:
            response = requests.post(url=URL, headers=Headers)
            response.raise_for_status()
            r = response.json()

            result = Models.UserModel(r.get('userID'), r.get('ip'), r.get('city'), r.get(
                'region'), r.get('country'), r.get('latitude'), r.get('longtitude'), r.get('lastUpdate'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def Delete(userToken) -> Models.UserModel:
        URL = "https://api.nucle.cloud/v1/user/delete"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}

        try:
            response = requests.post(url=URL, headers=Headers)
            response.raise_for_status()
            r = response.json()

            result = Models.UserModel(r.get('id'), r.get('userName'), r.get(
                'displayName'), r.get('email'), r.get('creationDate'), r.get('lastLogin'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')


class Anonymous:

    @staticmethod
    def Login(projectId,deviceId) -> Models.LoginResult:
        URL = "https://api.nucle.cloud/v1/user/anonymous/login"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "projectId": projectId}
        Json = {"deviceId": deviceId}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()

            user = Models.UserModel(r.get('id'), r.get('userName'), r.get(
                'displayName'), r.get('email'), r.get('creationDate'), r.get('lastLogin'))
            result = Models.LoginResult(r.get('userToken'), user)
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def Create(projectId,deviceId) -> Models.LoginResult:
        URL = "https://api.nucle.cloud/v1/user/anonymous/create"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "projectId": projectId}
        Json = {"deviceId": deviceId}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()

            user = Models.UserModel(r.get('id'), r.get('userName'), r.get(
                'displayName'), r.get('email'), r.get('creationDate'), r.get('lastLogin'))
            result = Models.LoginResult(r.get('userToken'), user)
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')


class ExternalLogin:
    @staticmethod
    def Create(projectId,loginProvider,providerKey,providerDisplayName,userEmail,userName) -> Models.LoginResult:
        URL = "https://api.nucle.cloud/v1/user/externallogin/create"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "projectId": projectId}
        Json = {"loginProvider": loginProvider, "providerKey": providerKey,
                "providerDisplayName": providerDisplayName, "userEmail": userEmail, "userName": userName}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()

            user = Models.UserModel(r.get('id'), r.get('userName'), r.get(
                'displayName'), r.get('email'), r.get('creationDate'), r.get('lastLogin'))
            result = Models.LoginResult(r.get('userToken'), user)
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def Login(projectId,loginProvider,providerKey) -> Models.LoginResult:
        URL = "https://api.nucle.cloud/v1/user/externallogin/login"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "projectId": projectId}
        Json = {"loginProvider": loginProvider,
                "providerKey": providerKey}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()

            user = Models.UserModel(r.get('id'), r.get('userName'), r.get(
                'displayName'), r.get('email'), r.get('creationDate'), r.get('lastLogin'))
            result = Models.LoginResult(r.get('userToken'), user)
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def Get(userToken,loginProvider,providerKey) -> Models.ExternalLoginModel:
        URL = "https://api.nucle.cloud/v1/user/externallogin/get"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        Json = {"loginProvider": loginProvider,
                "providerKey": providerKey}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()
            result = Models.ExternalLoginModel(r.get('loginProvider'), r.get(
                'providerKey'), r.get('providerDisplayName'), r.get('userId'),)
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def Delete(userToken,loginProvider,providerKey) -> Models.ExternalLoginModel:
        URL = "https://api.nucle.cloud/v1/user/externallogin/delete"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        Json = {"loginProvider": loginProvider,
                "providerKey": providerKey}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()
            result = Models.ExternalLoginModel(r.get('loginProvider'), r.get(
                'providerKey'), r.get('providerDisplayName'), r.get('userId'),)
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')


class Preset:
    @staticmethod
    def GetById(userToken,presetId) -> Models.PresetModel:
        URL = "https://api.nucle.cloud/v1/preset/get/id"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        Json = {"presetId": presetId}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()
            result = Models.PresetModel(r.get('id'), r.get('name'), r.get('globalValue'), r.get('valueType'),
                                        r.get('updateType'), r.get('creationDate'), r.get('lastUpdate'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def GetByName(userToken,presetName) -> Models.PresetModel:
        URL = "https://api.nucle.cloud/v1/preset/get/name"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        Json = {"presetName":presetName}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()
            result = Models.PresetModel(r.get('id'), r.get('name'), r.get('globalValue'), r.get('valueType'),
                                        r.get('updateType'), r.get('creationDate'), r.get('lastUpdate'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')


class Variable:
    @staticmethod
    def Update(userToken,presetId, value) -> Models.VariableModel:
        URL = "https://api.nucle.cloud/v1/variable/update"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        Json = {"presetId": presetId, "value": value}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()
            result = Models.VariableModel(r.get('id'), r.get(
                'userId'), r.get('value'), r.get('lastUpdate'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def Get(userToken,presetId) -> Models.VariableModel:
        URL = "https://api.nucle.cloud/v1/variable/get"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        Json = {"presetId": presetId}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()
            result = Models.VariableModel(r.get('id'), r.get(
                'userId'), r.get('value'), r.get('lastUpdate'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def Delete(userToken,presetId) -> Models.VariableModel:
        URL = "https://api.nucle.cloud/v1/variable/delete"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        Json = {"presetId": presetId}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()
            result = Models.VariableModel(r.get('id'), r.get(
                'userId'), r.get('value'), r.get('lastUpdate'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def GetList(userToken,presetId,skip,take,orderType, searchValue) -> Models.VariablesModel:
        URL = "https://api.nucle.cloud/v1/variable/list"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        args = {"skip":skip, "take": take,
                "orderType": orderType, "search": searchValue}
        Json = {"presetId": presetId, "args": args}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            r = response.json()

            list = []
            for variable in r.get('list'):
                list.append(Models.VariableModel(variable.get('id'), variable.get(
                    'userId'), variable.get('value'), variable.get('lastUpdate')))

            result = Models.VariablesModel(list, r.get('totalCount'))
            return result
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')

    @staticmethod
    def Count(userToken,presetId, searchValue) -> str:
        URL = "https://api.nucle.cloud/v1/variable/count"
        Headers = {
            "Content-Type": "application/json; charset=utf-8", "userToken": userToken}
        Json = {"presetId": presetId,
                "searchValue": searchValue}

        try:
            response = requests.post(url=URL, json=Json, headers=Headers)
            response.raise_for_status()
            return response.text
        except HTTPError as http_err:
            errorMessage = http_err.response.json().get('errorMessage')
            print(f'HTTP error occurred: {errorMessage}')
        except Exception as err:
            print(f'Other error occurred: {err}')
