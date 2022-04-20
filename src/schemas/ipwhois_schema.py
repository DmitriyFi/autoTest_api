from pydantic import BaseModel, validator
from src.enums.ipwhois_enums import IpTypes, ContinentsAndCodes, ApiErrors
from IPy import IP


# создаем класс для валидации, наследуемся от класса BaseModel, описываем объекты api через типы данных:
class Atributes_Ip(BaseModel):
    ip: str
    success: bool
    type: IpTypes
    continent: str
    continent_code: str
    country: str
    country_code: str
    country_flag: str
    country_capital: str
    country_phone: str
    country_neighbours: str
    region: str
    city: str
    latitude: float
    longitude: float
    asn: str
    org: str
    isp: str
    timezone: str
    timezone_name: str
    timezone_dstOffset: int
    timezone_gmtOffset: int
    timezone_gmt: str
    currency: str
    currency_code: str
    currency_symbol: str
    currency_rates: int
    currency_plural: str
    completed_requests: int

    @validator('ip')                                               # проверяем соответствие структуры типа ip допустимой
    def check_valid_ip(cls, ip):
        try:
            IP(ip)  # используем класс IP из библы IPy
            return ip
        except Exception as ex:
            raise ValueError(ApiErrors.WRONG_IP.value)

    @validator('continent')                                        # проверяем соответствие объекта api нашему enum(у)
    def check_valid_continent(cls, continent):
        for item in ContinentsAndCodes.ContExists.value:
            if continent in ContinentsAndCodes[item].value:
                return continent
            else:
                raise ValueError(ApiErrors.WRONG_CONTINENT.value)

    @validator('continent_code')                                  # проверяем соответствие объекта api нашему enum(у)
    def check_valid_continent_code(cls, continent_code):
        for i in ContinentsAndCodes.ContExists.value:
            for j in ContinentsAndCodes[i].value:
                if continent_code in ContinentsAndCodes[i].value[j]:
                    return continent_code
                else:
                    raise ValueError(ApiErrors.WRONG_CONTINENT_CODE.value)
