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
