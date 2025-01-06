# generated file
#    python -m pywisetransfer.model.recipient && black .

from pywisetransfer.model.timestamp import Date
from .address import AddressDetails
from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import date
from .literals import (
    ACCOUNTTYPE,
    ADDRESS_COUNTRY,
    BANKCODE,
    IDDOCUMENTTYPE,
    LANGUAGE,
    LEGALTYPE,
    NATIONALITY,
    RUSSIAREGION,
    SWIFTCODE,
)


class RecipientDetails(BaseModel):
    """The recipient details model.

    See https://docs.wise.com/api-docs/api-reference/recipient
    """

    dateOfBirth: Optional[date] = Field(description="Date of birth", default=None)
    address: Optional[AddressDetails] = None

    accountType: Optional[ACCOUNTTYPE] = None
    bankCode: Optional[BANKCODE] = None
    idDocumentType: Optional[IDDOCUMENTTYPE] = None
    language: Optional[LANGUAGE] = None
    legalType: Optional[LEGALTYPE] = None
    nationality: Optional[NATIONALITY] = None
    russiaRegion: Optional[RUSSIAREGION] = None
    swiftCode: Optional[SWIFTCODE] = None
    BIC: Optional[str] = Field(
        examples=["BARCGB22XXX", "Please choose recipient's bank"],
        min_length=8,
        max_length=11,
        pattern="(^[A-Za-z]{6}[A-Za-z\\d]{2}([A-Za-z\\d]{3})?$)",
        default=None,
    )
    IBAN: Optional[str] = Field(
        examples=[
            "AE070331234567890123456",
            "CR95015114920010169410",
            "DE12345678901234567890",
            "IL620108000000099999999",
            "TR330006100519786457841326",
        ],
        min_length=2,
        max_length=42,
        pattern="(^AE\\d{21}$)|(^IL\\d{2}([-_\\s]?\\d{4}){4}[-_\\s]?\\d{3}$)|(^[a-zA-Z]{2}[a-zA-Z0-9 ]{12,40}$)",
        default=None,
    )
    abartn: Optional[str] = Field(
        examples=["020123456"], min_length=9, max_length=9, pattern="(^\\d{9}$)", default=None
    )
    accountHolderName: Optional[str] = Field(
        examples=None,
        min_length=2,
        max_length=255,
        pattern="(^[ -~゠-ヿ\u3000-〿¥￥！-ﾟ゙-゜]+$)|(^[0-9A-Za-zÀ-ÖØ-öø-ÿ-_()'*,.%#^@&{}~<>+$\"\\[\\]\\\\ ]+$)|(^[0-9A-Za-zÀ-ÖØ-öø-ÿ-_()őŐűŰ'*,.%#^@&{}~<>+$\"\\[\\]\\\\ ]+$)|(^[A-Za-z0-9âçğıİîöşüûÂÇĞIİÎÖŞÜÛ0-9-_()'*,. ]+$)|(^[а-яА-ЯёЁ' \\-]+$)",
        default=None,
    )
    accountNumber: Optional[str] = Field(
        examples=[
            "+254123456789",
            "+601122223333",
            "+6587654321",
            "+852-56781234 / abc@email.com / 123456789",
            "+86-12345678901",
            "00-0000-0000000-00",
            "00012345678",
            "00052312891",
            "000800003288795610242",
            "0023183991919",
            "0044123",
            "0052312891",
            "0170099220000067797370",
            "0584412903",
            "1020667389342",
            "120000071234567800000008",
            "1223183991919",
            "1234",
            "1234567",
            "12345678",
            "12345678-9",
            "123456789",
            "1234567890",
            "12345678901234567890",
            "123456789012345678901234",
            "12345678901234567890123456",
            "1254693521232",
            "159012938613",
            "231289112",
            "265487900",
            "40820810999999999999",
            "5060011118",
            "639171234567",
            "6789112345678",
            "678911234567891",
            "6793312000",
            "86-12345678901 or example@email.com",
            "880XXXXXXXXXX",
            "951-7-38426-0",
            "wise@yesb",
        ],
        min_length=1,
        max_length=255,
        pattern="(.*)|([0-9]{6,16})|([0-9]{8})|(\\d{7,12})|(^((H?\\d{2})|\\d{3})-?\\d{1}-?\\d{5}-?\\d{1,7})|(^(40|42){1}\\d{18}$)|(^[0-9-]{1,22}$)|(^[0-9]{26}$)|(^[0-9]{4,20}$)|(^[0-9a-zA-Z]+$)|(^[0-9a-zA-Z]{1,35}$)|(^[1-9][0-9]{7}-?([0-9]{8})?-?[0-9]{8}$)|(^[\\d -]+$)|(^[a-zA-Z0-9\\s]{4,34}$)|(^[a-zA-Z0-9]{5,20}$)|(^\\+?([0-9]{1,3})-([0-9]{4,13})$)|(^\\+?880\\d{10}$)|(^\\d{10}$)|(^\\d{2,7}$)|(^\\d{21}$)|(^\\d{24}$)|(^\\d{3}\\ ?\\d{4}\\ ?\\d\\ ?\\d{13}\\ ?\\d$)|(^\\d{4,17}$)|(^\\d{4,9}$)|(^\\d{4}$)|(^\\d{6,15}$)|(^\\d{6,20}$)|(^\\d{7,11}$)|(^\\d{7,18}$)|(^\\d{7,20}$)|(^\\d{8,20}$)",
        default=None,
    )
    bankCode: Optional[str] = Field(
        examples=["041234567", "5500"],
        min_length=4,
        max_length=9,
        pattern="(^04\\d{7}$)|(^\\d{4}$)",
        default=None,
    )
    billerCode: Optional[str] = Field(
        examples=["12345"], min_length=3, max_length=10, pattern="(^[0-9]{3,10}$)", default=None
    )
    branchCode: Optional[str] = Field(
        examples=["1234", "Please choose recipient's branch", "Please enter branch name"],
        min_length=3,
        max_length=6,
        pattern="(^[\\d\\-]{3,5}[\\dxX]$)",
        default=None,
    )
    bsbCode: Optional[str] = Field(
        examples=["802985"],
        min_length=6,
        max_length=7,
        pattern="(^\\d{3}\\-?\\d{3}$)",
        default=None,
    )
    cannotHavePatronymicName: Optional[str] = Field(
        examples=None, min_length=None, max_length=None, pattern=None, default=None
    )
    clabe: Optional[str] = Field(
        examples=["032180000118359719"],
        min_length=18,
        max_length=18,
        pattern="(^\\d{5}\\s?\\d{8}\\s?\\d{5}$)",
        default=None,
    )
    cnpj: Optional[str] = Field(
        examples=["64.753.719/0001-86"],
        min_length=None,
        max_length=None,
        pattern=None,
        default=None,
    )
    cpf: Optional[str] = Field(
        examples=["123.456.789-12"], min_length=None, max_length=None, pattern=None, default=None
    )
    customerReferenceNumber: Optional[str] = Field(
        examples=["0123456789"],
        min_length=2,
        max_length=20,
        pattern="(^(\\s*(?:\\d\\s*){2,20})$)",
        default=None,
    )
    email: Optional[str] = Field(
        examples=["example@example.ex"],
        min_length=None,
        max_length=255,
        pattern="(\\s*[a-zA-Z0-9.!#$%&'*+\\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+\\s*)|(^[^\\s]+@[^\\s]+\\.[^\\s]{2,}$)",
        default=None,
    )
    familyName: Optional[str] = Field(
        examples=None, min_length=1, max_length=30, pattern="(^[а-яА-ЯёЁ' \\-]+$)", default=None
    )
    givenName: Optional[str] = Field(
        examples=None, min_length=1, max_length=30, pattern="(^[а-яА-ЯёЁ' \\-]+$)", default=None
    )
    idDocumentNumber: Optional[str] = Field(
        examples=["09740475", "901270245"], min_length=7, max_length=14, pattern=None, default=None
    )
    identificationNumber: Optional[str] = Field(
        examples=None, min_length=None, max_length=None, pattern=None, default=None
    )
    ifscCode: Optional[str] = Field(
        examples=["YESB0236041"],
        min_length=11,
        max_length=11,
        pattern="(^[A-Za-z]{4}0[A-Za-z0-9]{6}$)",
        default=None,
    )
    institutionNumber: Optional[str] = Field(
        examples=["006"], min_length=3, max_length=3, pattern="(\\d{3})", default=None
    )
    interacAccount: Optional[str] = Field(
        examples=["example@example.ex"], min_length=6, max_length=50, pattern="(.*)", default=None
    )
    job: Optional[str] = Field(
        examples=None, min_length=3, max_length=22, pattern=None, default=None
    )
    patronymicName: Optional[str] = Field(
        examples=None, min_length=1, max_length=30, pattern="(^[а-яА-ЯёЁ' \\-]+$)", default=None
    )
    phoneNumber: Optional[str] = Field(
        examples=[
            "+27111234567",
            "+51 987654321",
            "+56 33 555 5555",
            "+57 21 5555 5555",
            "01012345678",
            "Phone number linked to bank card (eg 380123456789)",
        ],
        min_length=7,
        max_length=20,
        pattern="(^((\\+)|(00))?[0-9]{9,15}$)",
        default=None,
    )
    prefix: Optional[str] = Field(
        examples=["000000"], min_length=None, max_length=6, pattern="(^\\d{0,6}$)", default=None
    )
    rut: Optional[str] = Field(
        examples=["760864285"],
        min_length=8,
        max_length=12,
        pattern="(^[0-9Kk\\.\\-]{8,12}$)",
        default=None,
    )
    sortCode: Optional[str] = Field(
        examples=["40-30-20"],
        min_length=6,
        max_length=8,
        pattern="(^\\d{2}-?\\d{2}-?\\d{2}$)",
        default=None,
    )
    swiftCode: Optional[str] = Field(
        examples=["BUKBGB22"],
        min_length=8,
        max_length=11,
        pattern="(^[a-zA-Z]{6}(([a-zA-Z0-9]{2})|([a-zA-Z0-9]{5}))$)",
        default=None,
    )
    taxId: Optional[str] = Field(
        examples=["20084908488"],
        min_length=None,
        max_length=None,
        pattern="(^\\d{2}\\-?\\d{8}\\-?\\d$)",
        default=None,
    )
    transitNumber: Optional[str] = Field(
        examples=["04841"], min_length=5, max_length=5, pattern="(\\d{5})", default=None
    )


__all__ = ["RecipientDetails"]
