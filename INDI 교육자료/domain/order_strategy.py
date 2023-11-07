class OrderStrategy:
    
    def __init__(self, stock_code="A005930", order_quantity=3, count=5, price_change=1000):
        self.stock_code = stock_code  # 종목코드
        self.order_quantity = order_quantity  # 한 번에 주문하는 수량
        self.count = count  # count 횟수 EX) 몇 번 주문?
        self.price_change = price_change # 가격 변화량 EX) 1000원
