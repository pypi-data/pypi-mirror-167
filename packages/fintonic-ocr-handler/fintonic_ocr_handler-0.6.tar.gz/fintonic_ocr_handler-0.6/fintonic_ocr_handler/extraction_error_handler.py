# -*- coding: utf-8 -*-
"""
    Clases de tipo Exception para flujo de extracción de datos
"""
import re


class TransactionsDoesNotExistError(Exception):
    def __init__(self, *args: object) -> None:
        # self.code = 'transactions_doesnotexist'
        self.message = 'No se pudieron obtener transacciones del documento'
        super().__init__(*args)

    def __str__(self) -> str:
        return str(self.message)


class DocumentStructureError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = 'El documento no tiene un formato del cual se pueda extraer texto'
        super().__init__(*args)

    def __str__(self) -> str:
        return str(self.message)


class ColumnMatchError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = 'Las fechas, conceptos y montos no coinciden'
        super().__init__(*args)

    def __str__(self) -> str:
        return str(self.message)


class ExtractDataError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = 'Se presento un problema al extraer la información, error de estructura'
        super().__init__(*args)

    def __str__(self) -> str:
        return str(self.message)


class CustomExceptionError(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return str(self.message)


class DataframeEmptyError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = 'No se encontraron transacciones en el documento'
        super().__init__(*args)

    def __str__(self) -> str:
        return str(self.message)


class DescriptionEmptyError(Exception):
    def __init__(self, *args: object) -> None:
        self.message = 'Se encontraron transacciones pero las descripciones no son válidas'
        super().__init__(*args)

    def __str__(self) -> str:
        return str(self.message)


class BankSelectedError(Exception):
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return str(self.message)


class DocumentInProgress(Exception):
    pass


class ApiWebHookAggregatorError(Exception):
    pass


class SlakWebHookError(Exception):
    pass


class DatabaseCodeError:
    def __init__(self, content: str, pattern: str = '\((.*?)\)') -> None:
        try:
            prefix = 'aws' if content.find('aws') >= 0 else ''
            substring = re.findall(pattern, content)
            if len(substring) == 0:
                raise Exception
            substring = ''.join(substring[0:1])
            self.message = f'{prefix}{substring}'
        except:
            code = content[0:30].strip().lower()
            self.message = code.replace(' ', '')

    def __str__(self) -> str:
        return str(self.message).lower()


class MessageforClientError(Exception):
    pass


class MessageSystemError(Exception):
    pass
