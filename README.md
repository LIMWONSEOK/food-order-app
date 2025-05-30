![diagram png](https://github.com/user-attachments/assets/518f7c1b-0889-40a8-af42-a501767d9465)# food-order-app

# 🍔 음식 주문 앱 시뮬레이션 (개인 실습 과제 1)

## ⓐ 시퀀스 다이어그램

> 일상 속 소프트웨어 사용 사례로 "음식 배달 앱"의 주문 흐름을 모델링한 시퀀스 다이어그램입니다.

### 시퀀스 다이어그램 설명
사용자가 앱에서 음식을 주문하면, 앱은 서버를 통해 음식점에 주문을 전달하고 응답을 받아 사용자에게 알림을 보냅니다.

### 시각적 다이어그램
![시퀀스 다이어그램](file:///C:/Users/dladn/OneDrive/%EB%B0%94%ED%83%95%20%ED%99%94%EB%A9%B4/food-order-app/diagram.png.svg)

---![Uploading diagram.png.svg…]()


## ⓑ 샘플 코드 (Python)

> 시퀀스 다이어그램을 기반으로 실제 작동 가능한 샘플 코드를 Python으로 구현하였습니다.

```python
class FoodApp:
    def __init__(self, server):
        self.server = server

    def order_food(self, food_item):
        print(f"앱: '{food_item}' 주문 요청을 서버에 전달")
        response = self.server.process_order(food_item)
        print(f"앱: 서버로부터 응답 수신 - {response}")
        return response


class Server:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def process_order(self, food_item):
        print("서버: 음식점에 주문 전달")
        accepted = self.restaurant.accept_order(food_item)
        return "주문 수락됨" if accepted else "주문 거절됨"


class Restaurant:
    def accept_order(self, food_item):
        print(f"음식점: '{food_item}' 주문 수락")
        return True


# 실행 예시
restaurant = Restaurant()
server = Server(restaurant)
app = FoodApp(server)

result = app.order_food("김치찌개")
print(f"최종 사용자 알림: {result}")

```

## ⓒ 모듈 평가 (응집도 / 결합도)
| 평가 항목   | 설명                                                                                                                 |
| ------- | ------------------------------------------------------------------------------------------------------------------ |
| **응집도** | 각 클래스는 명확한 역할(앱, 서버, 음식점)을 가지며, 단일 책임 원칙(SRP)을 잘 따름. **응집도 높음**                                                    |
| **결합도** | `FoodApp`은 `Server`, `Server`는 `Restaurant`에 직접 의존. **중간 수준의 결합도**. 향후 **인터페이스 분리** 또는 **DI(의존성 주입)** 적용 시 낮출 수 있음 |

