"""The currency model."""

from __future__ import annotations
from typing import ClassVar, TypeVar
from pydantic import BaseModel, Field
import re

from wise_banking_api_client.model.enum import StrEnum


CODE_REGEX = "^[A-Z][A-Z][A-Z]$"
CURRENCY = Field(
    title="code",
    description="Currency code (ISO 4217 Alphabetic Code)",
    examples=["USD", "EUR"],
    pattern=CODE_REGEX,
)


class CurrencyGetter:

    def __init__(self, json: str):
        """Return the currency with this JSON."""
        self._json = json

    def __get__(self, instance, owner) -> Currency:
        return Currency.model_validate_json(self._json)


class Currency(BaseModel):
    """The currency model.

    See https://docs.wise.com/api-docs/api-reference/currencies

    Attributes:
        code: Currency code (ISO 4217 Alphabetic Code)
        symbol: The symbol of this currency
        name: Display name of this currency
        countryKeywords: Keywords associated with this currency
        supportsDecimals: Whether this currency supports decimal values or not
    """

    code: str = CURRENCY
    symbol: str
    name: str
    countryKeywords: list[str]
    supportsDecimals: bool

    AED: ClassVar[Currency] = CurrencyGetter(
        '{"code":"AED","symbol":"د.إ","name":"United Arab Emirates dirham","countryKeywords":["AED","AE","are","United Arab Emirates"],"supportsDecimals":true}'
    )
    AFN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"AFN","symbol":"؋","name":"Afghanistan afghani","countryKeywords":["Afghanistan","afg","AF","AFN"],"supportsDecimals":true}'
    )
    ALL: ClassVar[Currency] = CurrencyGetter(
        '{"code":"ALL","symbol":"Lek","name":"Albanian lek","countryKeywords":["ALL","alb","AL","Albania"],"supportsDecimals":true}'
    )
    AMD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"AMD","symbol":"֏","name":"Armenian dram","countryKeywords":["Armenia","AMD","AM","arm"],"supportsDecimals":true}'
    )
    ANG: ClassVar[Currency] = CurrencyGetter(
        '{"code":"ANG","symbol":"ƒ","name":"Netherlands Antillean guilder","countryKeywords":["CW","cuw","Sint Maarten (Dutch part)","SX","ant","Netherlands Antilles","sxm","ANG","Curaçao","AN"],"supportsDecimals":true}'
    )
    AOA: ClassVar[Currency] = CurrencyGetter(
        '{"code":"AOA","symbol":"Kz","name":"Angolan kwanza","countryKeywords":["AOA","Angola","ago","AO"],"supportsDecimals":true}'
    )
    ARS: ClassVar[Currency] = CurrencyGetter(
        '{"code":"ARS","symbol":"$","name":"Argentine peso","countryKeywords":["AR","ARS","Argentina","arg"],"supportsDecimals":true}'
    )
    AUD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"AUD","symbol":"A$","name":"Australian dollar","countryKeywords":["TV","NR","HM","Christmas Island","cck","Kiribati","AUD","tuv","Cocos (Keeling) Islands","kir","cxr","KI","CC","Heard Island and McDonald Islands","Tuvalu","Norfolk Island","nru","nfk","AU","CX","NF","Nauru","Australia","aus","hmd"],"supportsDecimals":true}'
    )
    AWG: ClassVar[Currency] = CurrencyGetter(
        '{"code":"AWG","symbol":"AWG","name":"Aruban florin","countryKeywords":["AWG","AW","abw","Aruba"],"supportsDecimals":true}'
    )
    AZN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"AZN","symbol":"man.","name":"Azerbaijani manat","countryKeywords":["Azerbaijan","AZN","AZ","aze"],"supportsDecimals":true}'
    )
    BAM: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BAM","symbol":"KM","name":"Bosnia and Herzegovina convertible mark","countryKeywords":["bih","Bosnia and Herzegovina","BAM","BA"],"supportsDecimals":true}'
    )
    BBD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BBD","symbol":"BBD","name":"Barbadian dollar","countryKeywords":["BB","brb","Barbados","BBD"],"supportsDecimals":true}'
    )
    BDT: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BDT","symbol":"Tk","name":"Bangladeshi taka","countryKeywords":["BD","Bangladesh","BDT","bgd"],"supportsDecimals":true}'
    )
    BGN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BGN","symbol":"лв","name":"Bulgarian lev","countryKeywords":["BG","BGN","bgr","Bulgaria"],"supportsDecimals":true}'
    )
    BHD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BHD","symbol":"BHD","name":"Bahraini dinar","countryKeywords":["BH","bhr","Bahrain","BHD"],"supportsDecimals":true}'
    )
    BIF: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BIF","symbol":"BIF","name":"Burundian franc","countryKeywords":["Burundi","bdi","BI","BIF"],"supportsDecimals":false}'
    )
    BMD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BMD","symbol":"BMD","name":"Bermudian dollar","countryKeywords":["BMD","Bermuda","BM","bmu"],"supportsDecimals":true}'
    )
    BND: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BND","symbol":"BND","name":"Brunei dollar","countryKeywords":["BND","BN","Brunei Darussalam","brn"],"supportsDecimals":true}'
    )
    BOB: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BOB","symbol":"BOB","name":"Bolivian boliviano","countryKeywords":["BOB","Bolivia","BO","bol"],"supportsDecimals":true}'
    )
    BRL: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BRL","symbol":"R$","name":"Brazilian real","countryKeywords":["BR","bra","Brazil","BRL"],"supportsDecimals":true}'
    )
    BSD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BSD","symbol":"BSD","name":"Bahamian dollar","countryKeywords":["BS","BSD","bhs","Bahamas"],"supportsDecimals":true}'
    )
    BTN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BTN","symbol":"BTN","name":"Bhutanese ngultrum","countryKeywords":["BT","Bhutan","BTN","btn"],"supportsDecimals":true}'
    )
    BWP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BWP","symbol":"BWP","name":"Botswana pula","countryKeywords":["BW","Botswana","BWP","bwa"],"supportsDecimals":true}'
    )
    BYN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BYN","symbol":"BYN","name":"Belarusian ruble","countryKeywords":["BYN","BY","blr","Belarus"],"supportsDecimals":true}'
    )
    BZD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"BZD","symbol":"BZ$","name":"Belizean dollar","countryKeywords":["blz","BZ","Belize","BZD"],"supportsDecimals":true}'
    )
    CAD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"CAD","symbol":"C$","name":"Canadian dollar","countryKeywords":["can","Canada","CAD","CA"],"supportsDecimals":true}'
    )
    CDF: ClassVar[Currency] = CurrencyGetter(
        '{"code":"CDF","symbol":"CDF","name":"Congolese franc","countryKeywords":["CD","CDF","cod","Congo, the Democratic Republic of the"],"supportsDecimals":true}'
    )
    CHF: ClassVar[Currency] = CurrencyGetter(
        '{"code":"CHF","symbol":"SFr.","name":"Swiss franc","countryKeywords":["CHF","che","CH","Liechtenstein","lie","LI","Switzerland"],"supportsDecimals":true}'
    )
    CLP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"CLP","symbol":"$","name":"Chilean peso","countryKeywords":["CLP","chl","CL","Chile"],"supportsDecimals":false}'
    )
    CNH: ClassVar[Currency] = CurrencyGetter(
        '{"code":"CNH","symbol":"¥","name":"Chinese yuan","countryKeywords":[],"supportsDecimals":true}'
    )
    CNY: ClassVar[Currency] = CurrencyGetter(
        '{"code":"CNY","symbol":"¥","name":"Chinese yuan","countryKeywords":["China","chn","CN","CNY"],"supportsDecimals":true}'
    )
    COP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"COP","symbol":"$","name":"Colombian peso","countryKeywords":["col","Colombia","COP","CO"],"supportsDecimals":true}'
    )
    CRC: ClassVar[Currency] = CurrencyGetter(
        '{"code":"CRC","symbol":"₡","name":"Costa Rican colón","countryKeywords":["CRC","cri","CR","Costa Rica"],"supportsDecimals":true}'
    )
    CUC: ClassVar[Currency] = CurrencyGetter(
        '{"code":"CUC","symbol":"CUC$","name":"Cuban Convertible peso","countryKeywords":[],"supportsDecimals":true}'
    )
    CUP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"CUP","symbol":"CUP","name":"Cuban peso","countryKeywords":["cub","Cuba","CU","CUP"],"supportsDecimals":true}'
    )
    CVE: ClassVar[Currency] = CurrencyGetter(
        '{"code":"CVE","symbol":"CVE","name":"Cape Verdean escudo","countryKeywords":["Cape Verde","CVE","CV","cpv"],"supportsDecimals":true}'
    )
    CZK: ClassVar[Currency] = CurrencyGetter(
        '{"code":"CZK","symbol":"Kč","name":"Czech koruna","countryKeywords":["Czech Republic","CZK","CZ","cze"],"supportsDecimals":true}'
    )
    DJF: ClassVar[Currency] = CurrencyGetter(
        '{"code":"DJF","symbol":"DJF","name":"Djiboutian franc","countryKeywords":["Djibouti","DJF","dji","DJ"],"supportsDecimals":false}'
    )
    DKK: ClassVar[Currency] = CurrencyGetter(
        '{"code":"DKK","symbol":"kr","name":"Danish krone","countryKeywords":["grl","dnk","fro","DKK","GL","Faroe Islands","DK","Denmark","FO","Greenland"],"supportsDecimals":true}'
    )
    DOP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"DOP","symbol":"$","name":"Dominican peso","countryKeywords":["dom","DOP","Dominican Republic","DO"],"supportsDecimals":true}'
    )
    DZD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"DZD","symbol":"DZD","name":"Algerian dinar","countryKeywords":["DZ","dza","Algeria","DZD"],"supportsDecimals":true}'
    )
    EGP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"EGP","symbol":"E£","name":"Egyptian pound","countryKeywords":["EG","egy","Egypt","EGP"],"supportsDecimals":true}'
    )
    ERN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"ERN","symbol":"ERN","name":"Eritrean nakfa","countryKeywords":["ERN","Eritrea","ER","eri"],"supportsDecimals":true}'
    )
    ETB: ClassVar[Currency] = CurrencyGetter(
        '{"code":"ETB","symbol":"Br","name":"Ethiopian birr","countryKeywords":["ETB","eth","Ethiopia","ET"],"supportsDecimals":true}'
    )
    EUR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"EUR","symbol":"€","name":"Euro","countryKeywords":["Cambodia","cck","fin","Paraguay","uga","lux","iot","Solomon Islands","Montserrat","deu","Guadeloupe","egy","lva","hnd","nzl","AD","fji","AE","Falkland Islands","AG","Seychelles","AI","glp","AL","AM","Bahrain","AO","wlf","AR","AS","AT","AU","AW","Finland","AX","Faroe Islands","AZ","gmb","BA","BB","BD","BE","BF","BG","BH","mys","BJ","myt","BL","BM","BN","BO","BS","BT","Cocos (Keeling) Islands","BW","Liechtenstein","gnb","Bulgaria","sen","CA","CC","irl","flk","qat","CH","CI","CK","Côte d\'Ivoire","CL","United Arab Emirates","CN","tha","Kenya","CR","French Polynesia","Saint Lucia","CV","CX","CY","abw","CZ","Mayotte","San Marino","Israel","Tajikistan","DE","Gibraltar","isl","Cyprus","DK","bel","kwt","DM","isr","ben","Malaysia","DO","Armenia","DZ","ita","Turks and Caicos Islands","pan","bfa","ukr","sgp","EC","EE","Ecuador","che","EG","reu","chl","chn","hrv","ES","ET","tjk","vnm","shn","Italy","bgd","Haiti","FI","FJ","FK","FM","American Samoa","FO","FR","bgr","Vatican City","civ","grd","grc","GA","GB","hti","GD","GE","Kyrgyzstan","GF","GG","grl","GH","GI","GL","GM","GN","Uzbekistan","GP","GR","bhs","bhr","GT","GW","GY","dma","tls","Dominica","bih","hun","Benin","HK","HN","ago","HR","HT","Portugal","HU","Grenada","wsm","Mongolia","Latvia","fra","Morocco","Guatemala","nam","ID","per","IE","dnk","gtm","fro","IL","IM","IN","IO","Tanzania","slb","IS","Ghana","IT","sle","India","Canada","Maldives","Kosovo, Republic of","Taiwan","aia","guf","JE","slv","Germany","fsm","Fiji","JM","dom","United States","Guinea","JP","Micronesia, Federated States of","Sao Tome and Principe","guy","mac","Costa Rica","Vietnam","ton","maf","ncl","smr","KE","KG","KH","mar","blm","KN","Timor-Leste","KR","KW","Switzerland","Samoa","KY","Spain","KZ","phl","LA","LB","LC","Palau","ury","LI","cok","LK","Estonia","usa","esp","LR","LS","est","LT","LU","LV","bmu","Niue","Mozambique","vut","MA","El Salvador","alb","MC","ala","MD","eth","ME","mco","MF","ner","MH","lao","Lesotho","MK","Tonga","ML","MN","MO","EUR","MQ","MR","MS","MT","MU","cpv","MV","MW","mda","MX","MY","Mauritius","MZ","Norfolk Island","spm","nfk","NA","NC","NE","NF","lbn","NI","lbr","mdv","NL","bol","NO","NP","NR","NU","lca","NZ","Malta","Cape Verde","and","Ireland","rou","cri","France","Lithuania","OM","mex","srb","kaz","tto","PA","Nicaragua","PE","Norway","PF","Macao","PG","PH","Uganda","Mexico","plw","Suriname","PL","PM","Saint Helena","Greenland","Papua New Guinea","PT","PW","nic","PY","Kazakhstan","tun","Åland Islands","Bahamas","QA","tur","brb","tuv","Marshall Islands","Mali","Panama","jam","niu","Laos","zaf","brn","Argentina","png","Zambia","stp","mhl","Guinea-Bissau","RE","Macedonia, Former Yugoslav Republic of","Namibia","Georgia","Saint Kitts and Nevis","RO","RS","RW","Aruba","twn","pol","SA","SB","SC","omn","sur","SE","Sweden","SG","are","Malawi","SH","ken","SI","Andorra","arg","SK","Poland","SL","SM","SN","uzb","Tunisia","arm","btn","SR","ST","SV","nld","svk","svn","Tuvalu","TC","Lebanon","Azerbaijan","TF","Czech Republic","Mauritania","Guernsey","TH","TJ","TL","asm","TN","TO","Australia","TR","swe","TT","TV","TW","TZ","mkd","lie","dza","UA","Oman","Iceland","Gabon","atf","UG","atg","Luxembourg","Algeria","tza","Slovenia","Jersey","cxr","US","kgz","jey","Antigua and Barbuda","UY","UZ","Moldova","VA","mli","VC","bwa","VG","khm","Vanuatu","idn","prt","mlt","cym","pry","VN","Honduras","cyp","syc","Nauru","rwa","aus","VU","aut","lka","Singapore","French Guiana","Christmas Island","gab","WF","cze","nor","Netherlands","China","Martinique","Saint Pierre and Miquelon","WS","Bhutan","Romania","mne","Philippines","mng","npl","XK","gbr","British Virgin Islands","British Indian Ocean Territory","Montenegro","Indonesia","Angola","Brunei Darussalam","New Caledonia","Cayman Islands","Greece","Guyana","moz","YT","Chile","Nepal","Isle of Man","ZA","Ukraine","vat","Anguilla","nru","Turkey","ZM","Belgium","Trinidad and Tobago","South Africa","Bermuda","Jamaica","Peru","Hong Kong","Thailand","aze","geo","Saint Martin (French part)","Kuwait","kna","Croatia","Sri Lanka","Cook Islands","Uruguay","vct","United Kingdom","mrt","Liberia","Burkina Faso","Saint Barthélemy","pyf","msr","Wallis and Futuna","zmb","kor","Austria","South Korea","Monaco","ecu","ggy","gha","Hungary","Réunion","Japan","mtq","Albania","New Zealand","Senegal","Ethiopia","gib","hkg","Egypt","lso","mus","Sierra Leone","imn","Bolivia","gin","Saudi Arabia","vgb","can","tca","Gambia","Qatar","Slovakia","Serbia","Bosnia and Herzegovina","ind","xkx","Niger","sau","Rwanda","jpn","French Southern Territories","ltu","Bangladesh","Barbados","Saint Vincent and the Grenadines","Botswana","Denmark","Dominican Republic","mwi"],"supportsDecimals":true}'
    )
    FJD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"FJD","symbol":"FJD","name":"Fijian dollar","countryKeywords":["FJD","Fiji","FJ","fji"],"supportsDecimals":true}'
    )
    FKP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"FKP","symbol":"£","name":"Falkland Islands pound","countryKeywords":["South Georgia and the South Sandwich Islands","flk","Falkland Islands","FK","FKP","GS","sgs"],"supportsDecimals":true}'
    )
    GBP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"GBP","symbol":"£","name":"British pound","countryKeywords":["PT","fin","Kazakhstan","tun","lux","QA","tur","deu","lva","AD","AE","Seychelles","AL","Bahrain","stp","AT","Macedonia, Former Yugoslav Republic of","Faroe Islands","Finland","AZ","Georgia","RO","BA","RS","BE","BG","BH","pol","SA","SC","SE","Sweden","are","SI","Andorra","Liechtenstein","Poland","SK","SM","Bulgaria","Tunisia","ST","irl","qat","CH","nld","svk","svn","United Arab Emirates","CR","Lebanon","Azerbaijan","Czech Republic","Mauritania","Saint Lucia","Guernsey","CY","CZ","TL","TN","San Marino","Israel","TR","swe","DE","Gibraltar","isl","Cyprus","DK","mkd","bel","kwt","lie","isr","DO","UA","Iceland","Luxembourg","ita","Slovenia","Jersey","ukr","jey","EE","che","Moldova","hrv","ES","VG","prt","mlt","Italy","cyp","syc","aut","FI","FO","FR","bgr","cze","nor","Netherlands","GBP","grc","GB","GE","GG","grl","GI","Romania","mne","GL","GR","GT","bhr","gbr","British Virgin Islands","tls","Montenegro","bih","hun","HR","Portugal","HU","Greece","Latvia","fra","Guatemala","IE","dnk","gtm","fro","IL","IM","Isle of Man","Ukraine","IS","IT","Turkey","Belgium","JE","Germany","dom","Sao Tome and Principe","aze","Costa Rica","geo","smr","Kuwait","Croatia","Timor-Leste","United Kingdom","KW","Switzerland","mrt","Spain","KZ","LB","LC","LI","Estonia","esp","est","LT","LU","LV","Austria","Monaco","MC","alb","MD","ME","ggy","mco","MK","Hungary","MR","MT","MU","mda","Mauritius","Albania","lbn","NL","gib","NO","mus","imn","lca","Malta","Saudi Arabia","vgb","Qatar","Ireland","and","rou","Slovakia","cri","Lithuania","Serbia","France","Bosnia and Herzegovina","srb","kaz","sau","ltu","Norway","Denmark","Dominican Republic","PL","Greenland"],"supportsDecimals":true}'
    )
    GEL: ClassVar[Currency] = CurrencyGetter(
        '{"code":"GEL","symbol":"GEL","name":"Georgian lari","countryKeywords":["geo","Georgia","GE","GEL"],"supportsDecimals":true}'
    )
    GGP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"GGP","symbol":"£","name":"Guernsey pound","countryKeywords":[],"supportsDecimals":true}'
    )
    GHS: ClassVar[Currency] = CurrencyGetter(
        '{"code":"GHS","symbol":"GH¢","name":"Ghanaian cedi","countryKeywords":["GH","gha","GHS","Ghana"],"supportsDecimals":true}'
    )
    GIP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"GIP","symbol":"£","name":"Gibraltar pound","countryKeywords":["gib","GI","Gibraltar","GIP"],"supportsDecimals":true}'
    )
    GMD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"GMD","symbol":"GMD","name":"Gambian dalasi","countryKeywords":["Gambia","GM","gmb","GMD"],"supportsDecimals":true}'
    )
    GNF: ClassVar[Currency] = CurrencyGetter(
        '{"code":"GNF","symbol":"GNF","name":"Guinean franc","countryKeywords":["Guinea","GN","gin","GNF"],"supportsDecimals":false}'
    )
    GTQ: ClassVar[Currency] = CurrencyGetter(
        '{"code":"GTQ","symbol":"Q","name":"Guatemalan quetzal","countryKeywords":["gtm","GTQ","Guatemala","GT"],"supportsDecimals":true}'
    )
    GYD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"GYD","symbol":"GYD","name":"Guyanese dollar","countryKeywords":["GY","GYD","Guyana","guy"],"supportsDecimals":true}'
    )
    HKD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"HKD","symbol":"$","name":"Hong Kong dollar","countryKeywords":["HKD","HK","Hong Kong","hkg"],"supportsDecimals":true}'
    )
    HNL: ClassVar[Currency] = CurrencyGetter(
        '{"code":"HNL","symbol":"L","name":"Honduran lempira","countryKeywords":["HN","HNL","Honduras","hnd"],"supportsDecimals":true}'
    )
    HTG: ClassVar[Currency] = CurrencyGetter(
        '{"code":"HTG","symbol":"HTG","name":"Haitian gourde","countryKeywords":["Haiti","HTG","HT","hti"],"supportsDecimals":true}'
    )
    HUF: ClassVar[Currency] = CurrencyGetter(
        '{"code":"HUF","symbol":"Ft","name":"Hungarian forint","countryKeywords":["hun","Hungary","HUF","HU"],"supportsDecimals":false}'
    )
    IDR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"IDR","symbol":"Rp","name":"Indonesian rupiah","countryKeywords":["idn","IDR","ID","Indonesia"],"supportsDecimals":false}'
    )
    ILS: ClassVar[Currency] = CurrencyGetter(
        '{"code":"ILS","symbol":"₪","name":"Israeli shekel","countryKeywords":["ILS","IL","PS","pse","isr","Israel","Palestine"],"supportsDecimals":true}'
    )
    IMP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"IMP","symbol":"£","name":"Isle of Man pound","countryKeywords":[],"supportsDecimals":true}'
    )
    INR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"INR","symbol":"₹","name":"Indian rupee","countryKeywords":["IN","INR","ind","India"],"supportsDecimals":true}'
    )
    IQD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"IQD","symbol":"IQD","name":"Iraqi dinar","countryKeywords":["IQ","irq","Iraq","IQD"],"supportsDecimals":true}'
    )
    IRR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"IRR","symbol":"﷼","name":"Iranian rial","countryKeywords":["irn","Iran","IRR","IR"],"supportsDecimals":true}'
    )
    ISK: ClassVar[Currency] = CurrencyGetter(
        '{"code":"ISK","symbol":"kr","name":"Icelandic króna","countryKeywords":["ISK","isl","IS","Iceland"],"supportsDecimals":false}'
    )
    JEP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"JEP","symbol":"£","name":"Jersey pound","countryKeywords":[],"supportsDecimals":true}'
    )
    JMD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"JMD","symbol":"J$","name":"Jamaican dollar","countryKeywords":["JMD","JM","jam","Jamaica"],"supportsDecimals":true}'
    )
    JOD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"JOD","symbol":"JD","name":"Jordanian dinar","countryKeywords":["JO","jor","Jordan","JOD"],"supportsDecimals":true}'
    )
    JPY: ClassVar[Currency] = CurrencyGetter(
        '{"code":"JPY","symbol":"¥","name":"Japanese yen","countryKeywords":["JPY","JP","Japan","jpn"],"supportsDecimals":false}'
    )
    KES: ClassVar[Currency] = CurrencyGetter(
        '{"code":"KES","symbol":"Ksh","name":"Kenyan shilling","countryKeywords":["ken","KES","KE","Kenya"],"supportsDecimals":false}'
    )
    KGS: ClassVar[Currency] = CurrencyGetter(
        '{"code":"KGS","symbol":"KGS","name":"Kyrgyzstani som","countryKeywords":["KGS","KG","Kyrgyzstan","kgz"],"supportsDecimals":true}'
    )
    KHR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"KHR","symbol":"៛","name":"Cambodian riel","countryKeywords":["khm","KHR","Cambodia","KH"],"supportsDecimals":true}'
    )
    KMF: ClassVar[Currency] = CurrencyGetter(
        '{"code":"KMF","symbol":"KMF","name":"Comorian franc","countryKeywords":["com","KM","KMF","Comoros"],"supportsDecimals":false}'
    )
    KPW: ClassVar[Currency] = CurrencyGetter(
        '{"code":"KPW","symbol":"KPW","name":"North Korean won","countryKeywords":["KPW","KP","Korea, Democratic People\'s Republic of","prk"],"supportsDecimals":true}'
    )
    KRW: ClassVar[Currency] = CurrencyGetter(
        '{"code":"KRW","symbol":"₩","name":"South Korean won","countryKeywords":["KRW","South Korea","KR","kor"],"supportsDecimals":false}'
    )
    KWD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"KWD","symbol":"ك","name":"Kuwaiti dinar","countryKeywords":["KWD","kwt","KW","Kuwait"],"supportsDecimals":true}'
    )
    KYD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"KYD","symbol":"$","name":"Cayman Islands dollar","countryKeywords":["Cayman Islands","cym","KYD","KY"],"supportsDecimals":true}'
    )
    KZT: ClassVar[Currency] = CurrencyGetter(
        '{"code":"KZT","symbol":"₸","name":"Kazakhstani tenge","countryKeywords":["KZT","kaz","Kazakhstan","KZ"],"supportsDecimals":true}'
    )
    LAK: ClassVar[Currency] = CurrencyGetter(
        '{"code":"LAK","symbol":"LAK","name":"Lao kip","countryKeywords":["LA","LAK","lao","Laos"],"supportsDecimals":true}'
    )
    LBP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"LBP","symbol":"LBP","name":"Lebanon Pound","countryKeywords":["Lebanon","LB","lbn","LBP"],"supportsDecimals":true}'
    )
    LKR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"LKR","symbol":"Sr","name":"Sri Lankan rupee","countryKeywords":["LKR","lka","Sri Lanka","LK"],"supportsDecimals":true}'
    )
    LRD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"LRD","symbol":"L$","name":"Liberian dollar","countryKeywords":["Liberia","LR","lbr","LRD"],"supportsDecimals":true}'
    )
    LSL: ClassVar[Currency] = CurrencyGetter(
        '{"code":"LSL","symbol":"LSL","name":"Lesotho loti","countryKeywords":["LSL","LS","lso","Lesotho"],"supportsDecimals":true}'
    )
    LYD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"LYD","symbol":"LYD","name":"Libyan dinar","countryKeywords":["lby","LYD","LY","Libya"],"supportsDecimals":true}'
    )
    MAD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MAD","symbol":"د.م.","name":"Moroccan dirham","countryKeywords":["MAD","Western Sahara","EH","MA","Morocco","esh","mar"],"supportsDecimals":true}'
    )
    MDL: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MDL","symbol":"MDL","name":"Moldovan leu","countryKeywords":["MDL","MD","Moldova","mda"],"supportsDecimals":true}'
    )
    MGA: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MGA","symbol":"MGA","name":"Malagasy ariary","countryKeywords":["mdg","MGA","MG","Madagascar"],"supportsDecimals":true}'
    )
    MKD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MKD","symbol":"ден","name":"Macedonian denar","countryKeywords":["Macedonia, Former Yugoslav Republic of","MKD","mkd","MK"],"supportsDecimals":true}'
    )
    MMK: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MMK","symbol":"K","name":"Myanmar kyat","countryKeywords":["MM","Myanmar","mmr","MMK"],"supportsDecimals":true}'
    )
    MNT: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MNT","symbol":"MNT","name":"Mongolian tugrik","countryKeywords":["MN","MNT","Mongolia","mng"],"supportsDecimals":true}'
    )
    MOP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MOP","symbol":"MOP","name":"Macanese pataca","countryKeywords":["MO","Macao","mac","MOP"],"supportsDecimals":true}'
    )
    MRU: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MRU","symbol":"UM","name":"Ouguiya","countryKeywords":["MRU","Mauritania","MR","mrt"],"supportsDecimals":true}'
    )
    MUR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MUR","symbol":"₨","name":"Mauritian rupee","countryKeywords":["MU","mus","MUR","Mauritius"],"supportsDecimals":true}'
    )
    MVR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MVR","symbol":"MVR","name":"Maldivian rufiyaa","countryKeywords":["Maldives","MVR","MV","mdv"],"supportsDecimals":true}'
    )
    MWK: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MWK","symbol":"MWK","name":"Malawian kwacha","countryKeywords":["MWK","Malawi","MW","mwi"],"supportsDecimals":true}'
    )
    MXN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MXN","symbol":"Mex$","name":"Mexican peso","countryKeywords":["mex","MXN","Mexico","MX"],"supportsDecimals":true}'
    )
    MYR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MYR","symbol":"RM","name":"Malaysian ringgit","countryKeywords":["mys","MYR","Malaysia","MY"],"supportsDecimals":true}'
    )
    MZN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"MZN","symbol":"MT","name":"Mozambican metical","countryKeywords":["MZN","Mozambique","moz","MZ"],"supportsDecimals":true}'
    )
    NAD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"NAD","symbol":"$","name":"Namibian dollar","countryKeywords":["NAD","NA","Namibia","nam"],"supportsDecimals":true}'
    )
    NGN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"NGN","symbol":"₦","name":"Nigerian naira","countryKeywords":["NGN","NG","nga","Nigeria"],"supportsDecimals":true}'
    )
    NIO: ClassVar[Currency] = CurrencyGetter(
        '{"code":"NIO","symbol":"NIO","name":"Nicaraguan córdoba","countryKeywords":["Nicaragua","NIO","nic","NI"],"supportsDecimals":true}'
    )
    NOK: ClassVar[Currency] = CurrencyGetter(
        '{"code":"NOK","symbol":"kr","name":"Norwegian krone","countryKeywords":["nor","bvt","NO","BV","Norway","SJ","sjm","NOK","Bouvet Island","Svalbard and Jan Mayen"],"supportsDecimals":true}'
    )
    NPR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"NPR","symbol":"₨","name":"Nepalese rupee","countryKeywords":["NPR","NP","npl","Nepal"],"supportsDecimals":false}'
    )
    NZD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"NZD","symbol":"$","name":"New Zealand dollar","countryKeywords":["nzl","Tokelau","Cook Islands","NU","CK","Pitcairn Islands","NZ","Niue","New Zealand","tkl","TK","NZD","pcn","niu","PN","cok"],"supportsDecimals":true}'
    )
    OMR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"OMR","symbol":"OMR","name":"Omani rial","countryKeywords":["omn","OMR","OM","Oman"],"supportsDecimals":true}'
    )
    PAB: ClassVar[Currency] = CurrencyGetter(
        '{"code":"PAB","symbol":"B/.","name":"Panamanian balboa","countryKeywords":["PAB","PA","Panama","pan"],"supportsDecimals":true}'
    )
    PEN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"PEN","symbol":"S/.","name":"Peruvian sol","countryKeywords":["PE","PEN","per","Peru"],"supportsDecimals":true}'
    )
    PGK: ClassVar[Currency] = CurrencyGetter(
        '{"code":"PGK","symbol":"PGK","name":"Papua New Guinean kina","countryKeywords":["Papua New Guinea","PGK","PG","png"],"supportsDecimals":true}'
    )
    PHP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"PHP","symbol":"₱","name":"Philippine peso","countryKeywords":["phl","Philippines","PH","PHP"],"supportsDecimals":true}'
    )
    PKR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"PKR","symbol":"₨","name":"Pakistani rupee","countryKeywords":["Pakistan","PKR","PK","pak"],"supportsDecimals":true}'
    )
    PLN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"PLN","symbol":"zł","name":"Polish złoty","countryKeywords":["PLN","Poland","PL","pol"],"supportsDecimals":true}'
    )
    PYG: ClassVar[Currency] = CurrencyGetter(
        '{"code":"PYG","symbol":"₲","name":"Paraguay guaraní","countryKeywords":["pry","PY","Paraguay","PYG"],"supportsDecimals":false}'
    )
    QAR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"QAR","symbol":"QR","name":"Qatari riyal","countryKeywords":["QA","QAR","qat","Qatar"],"supportsDecimals":true}'
    )
    RON: ClassVar[Currency] = CurrencyGetter(
        '{"code":"RON","symbol":"L","name":"Romanian leu","countryKeywords":["RON","Romania","rou","RO"],"supportsDecimals":true}'
    )
    RSD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"RSD","symbol":"РСД","name":"Serbian dinar","countryKeywords":["RS","RSD","srb","Serbia"],"supportsDecimals":true}'
    )
    RUB: ClassVar[Currency] = CurrencyGetter(
        '{"code":"RUB","symbol":"руб","name":"Russian rouble","countryKeywords":["rus","Russian Federation","RU","RUB"],"supportsDecimals":true}'
    )
    RWF: ClassVar[Currency] = CurrencyGetter(
        '{"code":"RWF","symbol":"RWF","name":"Rwandan franc","countryKeywords":["RWF","RW","Rwanda","rwa"],"supportsDecimals":false}'
    )
    SAR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SAR","symbol":"SR","name":"Saudi riyal","countryKeywords":["Saudi Arabia","SAR","sau","SA"],"supportsDecimals":true}'
    )
    SBD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SBD","symbol":"SI$","name":"Solomon Islands dollar","countryKeywords":["SBD","slb","SB","Solomon Islands"],"supportsDecimals":true}'
    )
    SCR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SCR","symbol":"₨","name":"Seychellois rupee","countryKeywords":["SC","SCR","Seychelles","syc"],"supportsDecimals":true}'
    )
    SDG: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SDG","symbol":"SDG","name":"Sudanese Pound","countryKeywords":["SD","SDG","Sudan","sdn"],"supportsDecimals":true}'
    )
    SEK: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SEK","symbol":"kr","name":"Swedish krona","countryKeywords":["swe","SE","Sweden","SEK"],"supportsDecimals":true}'
    )
    SGD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SGD","symbol":"S$","name":"Singapore dollar","countryKeywords":["SGD","Singapore","SG","sgp"],"supportsDecimals":true}'
    )
    SHP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SHP","symbol":"£","name":"Saint Helena pound","countryKeywords":["SH","shn","SHP","Saint Helena"],"supportsDecimals":true}'
    )
    SLL: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SLL","symbol":"SLL","name":"Sierra Leonean leone","countryKeywords":["SLL","SL","Sierra Leone","sle"],"supportsDecimals":true}'
    )
    SLE: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SLE","symbol":"SLE","name":"Sierra Leonean leone","countryKeywords":[],"supportsDecimals":true}'
    )
    SOS: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SOS","symbol":"Sh.So.","name":"Somali shilling","countryKeywords":["som","SOS","Somalia","SO"],"supportsDecimals":true}'
    )
    SRD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SRD","symbol":"$","name":"Surinamese dollar","countryKeywords":["sur","SRD","Suriname","SR"],"supportsDecimals":true}'
    )
    SSP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SSP","symbol":"SSP","name":"South Sudanese pound","countryKeywords":["SS","SSP","South Sudan","ssd"],"supportsDecimals":true}'
    )
    STD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"STD","symbol":"STD","name":"São Tomé & Príncipe dobra","countryKeywords":[],"supportsDecimals":true}'
    )
    STN: ClassVar[Currency] = CurrencyGetter(
        '{"code":"STN","symbol":"STN","name":"Dobra","countryKeywords":["ST","Sao Tome and Principe","STN","stp"],"supportsDecimals":true}'
    )
    SVC: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SVC","symbol":"₡","name":"Salvadoran colón","countryKeywords":[],"supportsDecimals":true}'
    )
    SYP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SYP","symbol":"£","name":"Syrian pound","countryKeywords":["Syrian Arab Republic","SY","SYP","syr"],"supportsDecimals":true}'
    )
    SZL: ClassVar[Currency] = CurrencyGetter(
        '{"code":"SZL","symbol":"SZL","name":"Swazi lilangeni","countryKeywords":["SZL","Swaziland","SZ","swz"],"supportsDecimals":true}'
    )
    THB: ClassVar[Currency] = CurrencyGetter(
        '{"code":"THB","symbol":"฿","name":"Thai baht","countryKeywords":["TH","tha","Thailand","THB"],"supportsDecimals":true}'
    )
    TJS: ClassVar[Currency] = CurrencyGetter(
        '{"code":"TJS","symbol":"TJS","name":"Tajikistani somoni","countryKeywords":["tjk","TJ","TJS","Tajikistan"],"supportsDecimals":true}'
    )
    TMT: ClassVar[Currency] = CurrencyGetter(
        '{"code":"TMT","symbol":"TMT","name":"Turkmenistani manat","countryKeywords":["tkm","TM","TMT","Turkmenistan"],"supportsDecimals":true}'
    )
    TND: ClassVar[Currency] = CurrencyGetter(
        '{"code":"TND","symbol":"TND","name":"Tunisian dinar","countryKeywords":["TN","TND","tun","Tunisia"],"supportsDecimals":true}'
    )
    TOP: ClassVar[Currency] = CurrencyGetter(
        '{"code":"TOP","symbol":"TOP","name":"Tongan pa\'anga","countryKeywords":["ton","TOP","TO","Tonga"],"supportsDecimals":true}'
    )
    TRY: ClassVar[Currency] = CurrencyGetter(
        '{"code":"TRY","symbol":"TL","name":"Turkish lira","countryKeywords":["tur","Turkey","TRY","TR"],"supportsDecimals":true}'
    )
    TTD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"TTD","symbol":"TTD","name":"Trinidad and Tobago dollar","countryKeywords":["TT","TTD","Trinidad and Tobago","tto"],"supportsDecimals":true}'
    )
    TWD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"TWD","symbol":"NT$","name":"Taiwanese New Taiwan dollar","countryKeywords":["TWD","TW","Taiwan","twn"],"supportsDecimals":true}'
    )
    TZS: ClassVar[Currency] = CurrencyGetter(
        '{"code":"TZS","symbol":"tzs","name":"Tanzanian shilling","countryKeywords":["TZ","Tanzania","tza","TZS"],"supportsDecimals":true}'
    )
    UAH: ClassVar[Currency] = CurrencyGetter(
        '{"code":"UAH","symbol":"₴","name":"Ukrainian hryvnia","countryKeywords":["Ukraine","UA","UAH","ukr"],"supportsDecimals":true}'
    )
    UGX: ClassVar[Currency] = CurrencyGetter(
        '{"code":"UGX","symbol":"Ush","name":"Ugandan shilling","countryKeywords":["UG","UGX","Uganda","uga"],"supportsDecimals":false}'
    )
    USD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"USD","symbol":"$","name":"United States dollar","countryKeywords":["Cambodia","cck","fin","Paraguay","uga","lux","iot","Solomon Islands","Montserrat","deu","Guadeloupe","lva","vir","hnd","nzl","AD","fji","AE","Falkland Islands","AG","Seychelles","AI","glp","AL","AM","Bahrain","AO","wlf","AQ","AR","AS","AT","AU","Finland","AX","Faroe Islands","AZ","gmb","BA","BB","Puerto Rico","BE","BF","BG","BH","mys","BJ","myt","BL","BN","BO","BQ","BS","BT","Cocos (Keeling) Islands","BW","Liechtenstein","United States Virgin Islands","gnb","Bulgaria","sen","CA","CC","irl","flk","CH","CI","CK","Côte d\'Ivoire","CL","United Arab Emirates","CN","tha","Kenya","CR","French Polynesia","Saint Lucia","CX","CY","CZ","Mayotte","San Marino","Israel","Tajikistan","DE","Gibraltar","isl","Cyprus","DK","bel","kwt","Northern Mariana Islands","DM","isr","ben","Malaysia","DO","Armenia","bes","DZ","ita","Turks and Caicos Islands","pan","bfa","ukr","sgp","sgs","EC","EE","Ecuador","che","EH","reu","chl","chn","hrv","ES","ET","United States Minor Outlying Islands","tjk","vnm","shn","Italy","Haiti","FI","FJ","FK","FM","American Samoa","FO","FR","bgr","Vatican City","umi","civ","tkl","grc","pcn","GA","GB","hti","GE","Kyrgyzstan","GF","GG","grl","GH","GI","GL","GM","GN","Uzbekistan","GP","GR","GS","bhs","bhr","GT","GU","GW","GY","dma","tls","Dominica","bih","hun","Benin","HK","HN","ago","HR","HT","Portugal","HU","wsm","Mongolia","Latvia","fra","Morocco","Guatemala","nam","ID","per","IE","dnk","gtm","fro","IL","IM","IN","IO","Tanzania","slb","IS","Ghana","IT","sle","India","Canada","Taiwan","aia","guf","JE","slv","gum","Germany","fsm","Fiji","JM","dom","United States","Guinea","JP","Micronesia, Federated States of","Sao Tome and Principe","guy","mac","Costa Rica","Vietnam","ton","ncl","smr","KE","KG","KH","mar","blm","KN","USD","Timor-Leste","KR","KW","Switzerland","Samoa","KY","Spain","KZ","phl","LA","LB","LC","Palau","esh","ury","LI","cok","LK","Estonia","usa","esp","LR","est","LT","LU","LV","Niue","vut","MA","El Salvador","alb","MC","ala","eth","Guam","ME","mco","ner","MH","lao","MK","Tonga","ML","MN","Western Sahara","MO","MP","MQ","MR","MS","MT","MU","MW","MX","MY","Mauritius","Norfolk Island","spm","nfk","NA","Sint Maarten (Dutch part)","NC","NE","NF","lbn","NI","lbr","NL","bol","NO","NP","NR","NU","lca","NZ","Malta","and","Ireland","rou","cri","France","Lithuania","mex","srb","kaz","tto","PA","Nicaragua","PE","Norway","PF","Macao","PG","PH","Uganda","Mexico","plw","Suriname","PL","PM","PN","Saint Helena","Greenland","PR","Papua New Guinea","PT","PW","nic","PY","Kazakhstan","tun","Åland Islands","Bahamas","tur","brb","tuv","Marshall Islands","Mali","Panama","jam","niu","Laos","zaf","brn","Argentina","png","Zambia","stp","mhl","Guinea-Bissau","RE","Namibia","Macedonia, Former Yugoslav Republic of","Georgia","Saint Kitts and Nevis","RO","RS","RW","twn","pol","SB","SC","sur","South Georgia and the South Sandwich Islands","SE","Sweden","SG","are","Malawi","SH","ken","SI","Andorra","arg","SK","Poland","SL","SM","SN","uzb","Tunisia","arm","btn","SR","ST","SV","SX","nld","svk","svn","Tuvalu","TC","Lebanon","Azerbaijan","TF","Czech Republic","Mauritania","Guernsey","TH","TJ","TK","TL","asm","TN","TO","Bonaire","Australia","TR","swe","TT","TV","TW","TZ","mkd","lie","dza","UA","Iceland","ata","Gabon","atf","UG","atg","Luxembourg","UM","Algeria","tza","Slovenia","Jersey","cxr","US","kgz","jey","Antigua and Barbuda","UY","UZ","pri","sxm","VA","mli","VC","bwa","VG","khm","Vanuatu","idn","prt","VI","mlt","cym","pry","VN","Honduras","Antarctica","cyp","syc","Nauru","rwa","aus","VU","aut","lka","Singapore","French Guiana","Christmas Island","gab","WF","cze","nor","Netherlands","China","Martinique","Saint Pierre and Miquelon","WS","Bhutan","Romania","mne","Philippines","mng","npl","mnp","gbr","British Virgin Islands","British Indian Ocean Territory","Montenegro","Indonesia","Angola","Brunei Darussalam","New Caledonia","Cayman Islands","Greece","Guyana","YT","Chile","Nepal","Isle of Man","ZA","Ukraine","vat","Anguilla","nru","Turkey","ZM","Belgium","Trinidad and Tobago","South Africa","Jamaica","Peru","Tokelau","Hong Kong","Pitcairn Islands","Thailand","aze","geo","Kuwait","kna","Croatia","Sri Lanka","Cook Islands","Uruguay","vct","United Kingdom","mrt","Liberia","Burkina Faso","Saint Barthélemy","pyf","msr","Wallis and Futuna","zmb","kor","Austria","South Korea","Monaco","ecu","ggy","gha","Hungary","Réunion","Japan","mtq","Albania","New Zealand","Senegal","Ethiopia","gib","hkg","mus","Sierra Leone","imn","Bolivia","gin","vgb","can","tca","Gambia","Slovakia","Serbia","Bosnia and Herzegovina","ind","Niger","Rwanda","jpn","French Southern Territories","ltu","Barbados","Saint Vincent and the Grenadines","Botswana","Denmark","Dominican Republic","mwi"],"supportsDecimals":true}'
    )
    UYU: ClassVar[Currency] = CurrencyGetter(
        '{"code":"UYU","symbol":"$U","name":"Uruguayan peso","countryKeywords":["UYU","UY","Uruguay","ury"],"supportsDecimals":true}'
    )
    UYW: ClassVar[Currency] = CurrencyGetter(
        '{"code":"UYW","symbol":"UYW","name":"Unidad Previsional","countryKeywords":[],"supportsDecimals":true}'
    )
    UZS: ClassVar[Currency] = CurrencyGetter(
        '{"code":"UZS","symbol":"UZS","name":"Uzbekistani som","countryKeywords":["UZ","Uzbekistan","uzb","UZS"],"supportsDecimals":true}'
    )
    VES: ClassVar[Currency] = CurrencyGetter(
        '{"code":"VES","symbol":"Bs.","name":"Venezuelan bolívar soberano","countryKeywords":[],"supportsDecimals":true}'
    )
    VND: ClassVar[Currency] = CurrencyGetter(
        '{"code":"VND","symbol":"VND","name":"Vietnamese dong","countryKeywords":["Vietnam","vnm","VN","VND"],"supportsDecimals":false}'
    )
    VUV: ClassVar[Currency] = CurrencyGetter(
        '{"code":"VUV","symbol":"VUV","name":"Vanuatu vatu","countryKeywords":["Vanuatu","vut","VUV","VU"],"supportsDecimals":false}'
    )
    WST: ClassVar[Currency] = CurrencyGetter(
        '{"code":"WST","symbol":"WST","name":"Samoan tala","countryKeywords":["wsm","WST","WS","Samoa"],"supportsDecimals":true}'
    )
    XAF: ClassVar[Currency] = CurrencyGetter(
        '{"code":"XAF","symbol":"XAF","name":"Central African CFA franc","countryKeywords":["CF","CG","Cameroone","Chad","cmr","gab","caf","CM","GQ","gnq","Equatorial Guinea","Congo","TD","Gabon","tcd","cog","GA","Central African Republic","XAF"],"supportsDecimals":false}'
    )
    XCD: ClassVar[Currency] = CurrencyGetter(
        '{"code":"XCD","symbol":"$","name":"East Caribbean dollar","countryKeywords":["DM","lca","msr","Grenada","Montserrat","atg","grd","GD","kna","Antigua and Barbuda","KN","MS","AG","vct","AI","Anguilla","VC","Saint Lucia","Saint Vincent and the Grenadines","LC","XCD","aia","dma","Saint Kitts and Nevis","Dominica"],"supportsDecimals":true}'
    )
    XOF: ClassVar[Currency] = CurrencyGetter(
        '{"code":"XOF","symbol":"XOF","name":"West African CFA franc","countryKeywords":["Benin","BF","BJ","nga","ben","civ","Mali","gnb","ner","SN","Nigeria","bfa","tgo","sen","ML","Togo","Niger","CI","Côte d\'Ivoire","mli","XOF","GW","Guinea-Bissau","TG","Burkina Faso","Senegal","NE","NG"],"supportsDecimals":false}'
    )
    XPF: ClassVar[Currency] = CurrencyGetter(
        '{"code":"XPF","symbol":"XPF","name":"CFP franc","countryKeywords":["wlf","NC","ncl","PF","pyf","Wallis and Futuna","New Caledonia","XPF","French Polynesia","WF"],"supportsDecimals":false}'
    )
    YER: ClassVar[Currency] = CurrencyGetter(
        '{"code":"YER","symbol":"﷼","name":"Yemeni rial","countryKeywords":["yem","YER","YE","Yemen"],"supportsDecimals":true}'
    )
    ZAR: ClassVar[Currency] = CurrencyGetter(
        '{"code":"ZAR","symbol":"R","name":"South African rand","countryKeywords":["ZA","South Africa","ZAR","zaf"],"supportsDecimals":true}'
    )
    ZMW: ClassVar[Currency] = CurrencyGetter(
        '{"code":"ZMW","symbol":"ZMW","name":"Zambian kwacha","countryKeywords":["ZM","ZMW","Zambia","zmb"],"supportsDecimals":true}'
    )
    ZWG: ClassVar[Currency] = CurrencyGetter(
        '{"code":"ZWG","symbol":"ZWG","name":"Zimbabwe Gold","countryKeywords":[],"supportsDecimals":true}'
    )

    @classmethod
    def all_currencies(cls) -> list[Currency]:
        return [getattr(cls, name) for name in cls.__dict__.keys() if re.match(CODE_REGEX, name)]

    def as_parameter(self) -> str:
        """Transform into a parameter."""
        return self.code

    codes: ClassVar[list[str]] = [
        code for code in locals() if len(code) == 3 and code.upper() == code
    ]
    del code


CurrencyCode = StrEnum("CurrencyCode", {code: code for code in Currency.codes})

__all__ = ["Currency", "CURRENCY", "CurrencyCode"]
