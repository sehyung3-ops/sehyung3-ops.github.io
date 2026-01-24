# 스택 크기 설정
SIZE = 5

# 스택 생성 및 초기화
stack = [None for _ in range(SIZE)]
top = -1   # 스택이 비어 있음을 의미


def isStackFull():
    # 스택이 가득 찼는지 확인
    return top == SIZE - 1


def isStackEmpty():
    # 스택이 비어 있는지 확인
    return top == -1


def push(data):
    global top
    if isStackFull():
        print("스택이 가득 찼습니다.")
        return
    top += 1              # top 증가
    stack[top] = data     # 데이터 삽입


def pop():
    global top
    if isStackEmpty():
        print("스택이 비어 있습니다.")
        return None
    data = stack[top]     # top 위치 데이터 저장
    stack[top] = None     # 해당 공간 비우기
    top -= 1              # top 감소
    return data


def peek():
    # top 위치의 데이터만 확인
    if isStackEmpty():
        print("스택이 비어 있습니다.")
        return None
    return stack[top]
