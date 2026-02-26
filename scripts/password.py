class Password:

    _serviceName = ""
    _username = ""
    _hashedPassword = ''

    def __init__(self, serviceName, username, hasedPassword):
        self._serviceName = serviceName
        self._username = username
        self._hashedPassword = hasedPassword

    def get_serviceName(self):
        return self._serviceName
    
    def get_username(self):
        return self._username
    
    def get_hasedPassword(self):
        return self._hashedPassword