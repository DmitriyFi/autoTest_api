from enum import Enum


class IpTypes(Enum):                                                        # объект api должен возвращать такие данные
    IPv4 = 'IPv4'
    IPv6 = 'IPv6'


class ContinentsAndCodes(Enum):                                             # объект api должен возвращать такие данные
    ContExists = ('Eurasia', 'America', 'Africa', 'Australia', 'Antarctica')
    CodesExists = ('EU', 'AS', 'NA', 'SA', 'AF', 'AU', 'AN')
    Eurasia = {'Europe': 'EU', 'Asia': 'AS'}
    America = {'North America': 'NA', 'South America': 'SA'}
    Africa = {'Africa': 'AF'}
    Australia = {'Australia': 'AU'}
    Antarctica = {'Antarctica': 'AN'}


class ApiErrors(Enum):                                                      # здесь описан перечень возможных ошибок api
    WRONG_CONTINENT = "This continent doesn't exist"
    WRONG_CONTINENT_CODE = "This continent_code doesn't exist"
    WRONG_IP = "This IP doesn't exist"
