import re
from typing import Self
from pywisetransfer.model.enum import StrEnum


class RequirementType(StrEnum):
    """Type of a recipient account requirement."""

    aba = "aba"
    argentina = "argentina"
    australian = "australian"
    australian_bpay = "australian_bpay"
    bangladesh = "bangladesh"
    bkash = "bkash"
    brazil = "brazil"
    brazil_business = "brazil_business"
    canadian = "canadian"
    chile = "chile"
    chinese_alipay = "chinese_alipay"
    chinese_wechatpay = "chinese_wechatpay"
    colombia = "colombia"
    costa_rica = "costa_rica"
    czech = "czech"
    email = "email"
    emirates = "emirates"
    fiji_mobile = "fiji_mobile"
    hongkong = "hongkong"
    hong_kong_fps = "hong_kong_fps"
    hungarian = "hungarian"
    iban = "iban"
    indian = "indian"
    indian_upi = "indian_upi"
    indonesian = "indonesian"
    interac = "interac"
    israeli_local = "israeli_local"
    japanese = "japanese"
    kenya_local = "kenya_local"
    kenya_mobile = "kenya_mobile"
    malaysian = "malaysian"
    malaysian_duitnow = "malaysian_duitnow"
    mexican = "mexican"
    morocco = "morocco"
    mozambique_local = "mozambique_local"
    namibia_local = "namibia_local"
    nepal = "nepal"
    newzealand = "newzealand"
    nigeria = "nigeria"
    peru = "peru"
    philippines = "philippines"
    philippinesmobile = "philippinesmobile"
    polish = "polish"
    privatbank = "privatbank"
    russiarapida = "russiarapida"
    singapore = "singapore"
    singapore_paynow = "singapore_paynow"
    sort_code = "sort_code"
    southafrica = "southafrica"
    south_korean_paygate = "south_korean_paygate"
    south_korean_paygate_business = "south_korean_paygate_business"
    srilanka = "srilanka"
    tanzania_local = "tanzania_local"
    thailand = "thailand"
    turkish_earthport = "turkish_earthport"
    uganda_local = "uganda_local"
    uruguay = "uruguay"
    vietname_earthport = "vietname_earthport"
    fedwire_local = "fedwire_local"
    swift_code = "swift_code"


    @classmethod
    def from_camel_case(cls:type[Self], string:str) -> Self:
        """Return a RequirementType from a camelCase string.
        
        >>> from pywisetransfer import RequirementType
        >>> RequirementType.sort_code
        'sort_code'
        >>> RequirementType.from_camel_case('sort_code')
        'sort_code'
        >>> RequirementType.from_camel_case('sortCode')
        'sort_code'
        >>> RequirementType.from_camel_case('Iban')
        'iban'
        
        """
        return "_".join(s.lower() for s in re.findall(r'^[a-z_]+|[a-z_]+$|[A-Z][a-z_]*', string))



__all__ = ["RequirementType"]
