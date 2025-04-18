x = input()

사과 = 1000;
배 = 2000;
감 = 3000;
샤인머스켓 = 4000;
딸기 = 5000;
바나나 = 6000;
포도 = 7000;
블루베리 = 8000;

if x == "사과":
    price = 사과
elif x == "배":
    price = 배
elif x == "감":
    price = 감
elif x == "샤인머스켓":
    price = 샤인머스켓
elif x == "딸기":
    price = 딸기
elif x == "바나나":
    price = 바나나
elif x == "포도":
    price = 포도
elif x == "블루베리":
    price = 블루베리

if price<5000:
    print("최소 주문 금액을 채워주세요")
else:
    print("구매 가능합니다")