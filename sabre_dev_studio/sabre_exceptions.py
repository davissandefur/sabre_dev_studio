# Authentication requested, but no credentials (client ID, client secret) provided
class NoCredentialsProvided(Exception):
    pass

# Did not request token
class NotAuthorizedError(Exception):
    pass

class UnsupportedMethodError(Exception):
    pass

# Base API Exception
class SabreDevStudioException(Exception):
    def __init__(self, e=None):
        if isinstance(e, dict):
            message = e.get('message')
            super(SabreDevStudioException, self).__init__(message)

            self.message = message
            self.status = e.get('status')
            self.error_code = e.get('errorCode')
            self.e_type = e.get('type')
            self.tstamp = e.get('timeStamp')
        elif isinstance(e, str):
            self.message = e
        else:
            super(SabreDevStudioException, self).__init__()

    def __unicode__(self):
        if self.message and self.status:
            str += 'Message:\t' + self.message + '\n'
            str += 'Status:\t' + self.status + '\n'
            str += 'Error Code:\t' + self.error_code + '\n'
            str += 'Type:\t' + self.type + '\n'
            str += 'Timestamp:\t' + self.timestamp + '\n'
            return str
        elif self.message:
            return self.message
        else:
            return "<" + self.__class__.__name__ + ">"


# 400
class SabreErrorBadRequest(SabreDevStudioException):
    pass

# 401
class SabreErrorUnauthorized(SabreDevStudioException):
    pass

# 403
class SabreErrorForbidden(SabreDevStudioException):
    pass

# 404
class SabreErrorNotFound(SabreDevStudioException):
    pass

# 404
class SabreErrorMethodNotAllowed(SabreDevStudioException):
    pass

# 406
class SabreErrorNotAcceptable(SabreDevStudioException):
    pass

# 429
class SabreErrorRateLimited(SabreDevStudioException):
    pass

# 500
class SabreInternalServerError(SabreDevStudioException):
    pass

# 503
class SabreErrorServiceUnavailable(SabreDevStudioException):
    pass

# 504
class SabreErrorGatewayTimeout(SabreDevStudioException): 
    pass
