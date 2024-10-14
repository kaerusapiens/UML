from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    """
    抽象クラスShape作成。
    継承先でcalc_areaメソッドが実装されないとエラーになる。
    """
    @abstractmethod
    def calc_area(self) -> int:
        pass


class Rectangle(Shape):
    """
    長方形の面積を計算するクラス
    """
    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height

    def calc_area(self) -> int:
        return self.__width * self.__height

class Square(Shape):
    """
    正方形の面積を計算するクラス
    """
    def __init__(self, length: int):
        self.__length = length

    def calc_area(self) -> int:
        return self.__length ** 2

class Client:
    def __init__(self, shape: Shape):
        """
        shapeというオブジェクトはShapeというクラスを継承する
        """
        self.__shape = shape