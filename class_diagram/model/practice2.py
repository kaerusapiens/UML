import logging


class Employee:

    """
    社員情報を管理するクラス

    Attributes:
        employee_id( int ) : 社員ID
        name( str ) : 名前
        salary( int ) : 年間単位の給与
    """
    def __init__(self,emp_id:int,name:str,salary:int):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def _work(self)->None:
        logging.info('動きます')

    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int) -> None:
        self.__salary = salary

        