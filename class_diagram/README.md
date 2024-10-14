# クラス図概念

https://developer.ibm.com/articles/the-class-diagram/


https://tmytokai.github.io/open-ed/activity/class-diag/


# クラス図

### practice1
メソッドを利用してクラスを定義した場合
```mermaid
 
classDiagram
    class Employee {
        +int __emp_id
        +str __name
        +int __salary
        +_work() None
        +get_salary() int
        +set_salary(salary:int) None
    }
```

### practice2
デコレーターを利用してクラスを定義した場合
```mermaid
classDiagram
    class Employee {
        +int employee_id
        +str name
        +int salary
        +_work() None
        +salary() int
    }
```
### practice3
```mermaid
classDiagram
    class Shape {
        <<Interface>>
        +calc_area() int
    }

    class Rectangle {
        -width: int
        -height: int
        +calc_area() int
    }

    class Square {
        -length: int
        +calc_area() int
    }

    class Client {
        -shape: Shape
    }

    Shape <|-- Rectangle
    Shape <|-- Square
    Client o--> Shape
```