class Node:
    def __init__(self):
        self.data = None
        self.link = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    # -------------------------
    # 1) 공백 검사
    # -------------------------
    def isEmpty(self):
        return self.count == 0

    # -------------------------
    # 2) 전체 노드 방문(출력)
    # -------------------------
    def printNodes(self):
        if self.isEmpty():
            print("(empty)")
            return

        current = self.head
        print(current.data, end=" ")

        # 원형이므로 다시 head로 돌아오기 전까지 출력
        while current.link != self.head:
            current = current.link
            print(current.data, end=" ")
        print()

    # -------------------------
    # 3) pos 번째 노드 반환
    # -------------------------
    def getNode(self, pos):
        # pos는 0 ~ count-1 범위
        if pos < 0 or pos >= self.count:
            return None

        current = self.head
        for _ in range(pos):
            current = current.link
        return current

    # -------------------------
    # 4) 값 탐색: val을 가진 노드의 위치(pos) 반환
    # -------------------------
    def find(self, val):
        if self.isEmpty():
            return -1

        current = self.head
        idx = 0

        # 원형이므로 head부터 시작해서 다시 head로 돌아오기 전까지 확인
        while True:
            if current.data == val:
                return idx

            current = current.link
            idx += 1

            # 다시 head로 돌아오면 전체를 다 본 것
            if current == self.head:
                break

        return -1

    # -------------------------
    # 5) 삽입: insert(pos, elem)
    # -------------------------
    def insert(self, pos, elem):
        newNode = Node()
        newNode.data = elem

        # (1) 빈 리스트: 첫 노드가 head이자 tail
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            newNode.link = newNode  # 자기 자신을 가리켜 원형 완성
            self.count = 1
            return True

        # (2) 맨 앞 삽입 (pos <= 0)
        if pos <= 0:
            newNode.link = self.head
            self.head = newNode
            self.tail.link = self.head  # tail이 새 head를 가리키도록 유지
            self.count += 1
            return True

        # (3) 맨 뒤 삽입 (pos >= count) -> tail 뒤에 바로 붙임(O(1))
        if pos >= self.count:
            self.tail.link = newNode
            newNode.link = self.head
            self.tail = newNode
            self.count += 1
            return True

        # (4) 중간 삽입: (pos-1) 노드 뒤에 새 노드를 끼워넣기
        prev = self.getNode(pos - 1)
        newNode.link = prev.link
        prev.link = newNode
        self.count += 1
        return True

    # -------------------------
    # 6) 삭제: delete(pos) -> 삭제된 data 반환 (실패 시 None)
    # -------------------------
    def delete(self, pos):
        if self.isEmpty():
            return None

        if pos < 0 or pos >= self.count:
            return None

        # (1) 노드가 1개인 경우
        if self.count == 1:
            removed_data = self.head.data
            self.head = None
            self.tail = None
            self.count = 0
            return removed_data

        # (2) 맨 앞 삭제 (pos == 0)
        if pos == 0:
            removed_data = self.head.data
            self.head = self.head.link
            self.tail.link = self.head  # 원형 유지
            self.count -= 1
            return removed_data

        # (3) 중간/맨 뒤 삭제: prev 찾고 prev.link 제거
        prev = self.getNode(pos - 1)
        target = prev.link
        removed_data = target.data

        prev.link = target.link

        # (4) 맨 뒤 삭제라면 tail 갱신
        if target == self.tail:
            self.tail = prev

        self.count -= 1
        return removed_data


# -------------------------
# 간단 테스트
# -------------------------
if __name__ == "__main__":
    cl = CircularLinkedList()

    cl.printNodes()  # (empty)

    cl.insert(0, 10)
    cl.insert(1, 20)
    cl.insert(2, 30)
    cl.printNodes()  # 10 20 30

    print("find(20):", cl.find(20))  # 1
    print("find(99):", cl.find(99))  # -1

    cl.insert(1, 15)
    cl.printNodes()  # 10 15 20 30

    print("delete(0):", cl.delete(0))  # 10
    cl.printNodes()  # 15 20 30

    print("delete(last):", cl.delete(cl.count - 1))  # 30
    cl.printNodes()  # 15 20
