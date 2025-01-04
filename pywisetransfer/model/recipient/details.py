# generated file
#    python -m pywisetransfer.model.recipient && black .

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

    dateOfBirth: Optional[date] = None
    address: Optional[AddressDetails] = None

    accountType: ACCOUNTTYPE = None
    bankCode: BANKCODE = None
    idDocumentType: IDDOCUMENTTYPE = None
    language: LANGUAGE = None
    legalType: LEGALTYPE = None
    nationality: NATIONALITY = None
    russiaRegion: RUSSIAREGION = None
    swiftCode: SWIFTCODE = None
    BIC: Optional[str] = Field(
        examples=["Please choose recipient's bank"],
        min_length=8,
        max_length=11,
        pattern="^[A-Za-z]{6}[A-Za-z\\d]{2}([A-Za-z\\d]{3})?$",
        default=None,
    )
    IBAN: Optional[str] = Field(
        examples=["DE12345678901234567890"],
        min_length=14,
        max_length=42,
        pattern="^[a-zA-Z]{2}[a-zA-Z0-9 ]{12,40}$",
        default=None,
    )
    abartn: Optional[str] = Field(
        examples=["020123456"], min_length=9, max_length=9, pattern="^\\d{9}$", default=None
    )
    accountHolderName: Optional[str] = Field(min_length=2, max_length=255, default=None)
    accountNumber: Optional[str] = Field(
        examples=["00052312891"], min_length=7, max_length=11, pattern="^\\d{7,11}$", default=None
    )
    bankCode: Optional[str] = Field(
        examples=["041234567"], min_length=9, max_length=9, pattern="^04\\d{7}$", default=None
    )
    billerCode: Optional[str] = Field(
        examples=["12345"], min_length=3, max_length=10, pattern="^[0-9]{3,10}$", default=None
    )
    branchCode: Optional[str] = Field(
        examples=["1234"],
        min_length=4,
        max_length=6,
        pattern="^[\\d\\-]{3,5}[\\dxX]$",
        default=None,
    )
    bsbCode: Optional[str] = Field(
        examples=["802985"], min_length=6, max_length=7, pattern="^\\d{3}\\-?\\d{3}$", default=None
    )
    clabe: Optional[str] = Field(
        examples=["032180000118359719"],
        min_length=18,
        max_length=18,
        pattern="^\\d{5}\\s?\\d{8}\\s?\\d{5}$",
        default=None,
    )
    cnpj: Optional[str] = Field(examples=["64.753.719/0001-86"], default=None)
    cpf: Optional[str] = Field(examples=["123.456.789-12"], default=None)
    customerReferenceNumber: Optional[str] = Field(
        examples=["0123456789"],
        min_length=2,
        max_length=20,
        pattern="^(\\s*(?:\\d\\s*){2,20})$",
        default=None,
    )
    email: Optional[str] = Field(
        examples=["example@example.ex"],
        max_length=255,
        pattern="\\s*[a-zA-Z0-9.!#$%&'*+\\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+\\s*",
        default=None,
    )
    familyName: Optional[str] = Field(
        min_length=1, max_length=30, pattern="^[а-яА-ЯёЁ' \\-]+$", default=None
    )
    givenName: Optional[str] = Field(
        min_length=1, max_length=30, pattern="^[а-яА-ЯёЁ' \\-]+$", default=None
    )
    idDocumentNumber: Optional[str] = Field(default=None)
    identificationNumber: Optional[str] = Field(default=None)
    ifscCode: Optional[str] = Field(
        examples=["YESB0236041"],
        min_length=11,
        max_length=11,
        pattern="^[A-Za-z]{4}0[A-Za-z0-9]{6}$",
        default=None,
    )
    institutionNumber: Optional[str] = Field(
        examples=["006"], min_length=3, max_length=3, pattern="\\d{3}", default=None
    )
    interacAccount: Optional[str] = Field(
        examples=["example@example.ex"], min_length=6, max_length=50, default=None
    )
    job: Optional[str] = Field(min_length=3, max_length=22, default=None)
    patronymicName: Optional[str] = Field(
        min_length=1, max_length=30, pattern="^[а-яА-ЯёЁ' \\-]+$", default=None
    )
    phoneNumber: Optional[str] = Field(
        examples=["+27111234567"], min_length=7, max_length=20, default=None
    )
    prefix: Optional[str] = Field(
        examples=["000000"], max_length=6, pattern="^\\d{0,6}$", default=None
    )
    rut: Optional[str] = Field(
        examples=["760864285"],
        min_length=8,
        max_length=12,
        pattern="^[0-9Kk\\.\\-]{8,12}$",
        default=None,
    )
    sortCode: Optional[str] = Field(
        examples=["40-30-20"],
        min_length=6,
        max_length=8,
        pattern="^\\d{2}-?\\d{2}-?\\d{2}$",
        default=None,
    )
    swiftCode: Optional[str] = Field(
        examples=["BUKBGB22"],
        min_length=8,
        max_length=11,
        pattern="^[a-zA-Z]{6}(([a-zA-Z0-9]{2})|([a-zA-Z0-9]{5}))$",
        default=None,
    )
    taxId: Optional[str] = Field(
        examples=["20084908488"], pattern="^\\d{2}\\-?\\d{8}\\-?\\d$", default=None
    )
    transitNumber: Optional[str] = Field(
        examples=["04841"], min_length=5, max_length=5, pattern="\\d{5}", default=None
    )


__all__ = ["RecipientDetails"]
