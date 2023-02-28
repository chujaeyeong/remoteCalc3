## 메서드 선언부
def add_func(n1, n2) :
    res = n1 + n2
    return res

def min_func(n1, n2) :
    res = n1 - n2
    return res


## 전역 변수 (인스턴트 변수, 클래스 변수)
num1, num2, result = 100, 200, 0


## 메인 코드부 (main() 메서드)
result1 = add_func(num1, num2)

print(num1, '+', num2, '=', result1)

result2 = min_func(num1, num2)

print(num1, '-', num2, '=', result2)
