"""file that stores exceptions"""

class NonRequiredParamsMustHaveDefault(Exception):
    """for when the user does nto specify default for a non required parameter"""

class InvalidSid(Exception):
    """sid invalid"""