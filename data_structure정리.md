선형구조 : array, stack, queue  
비선형구조 : graph, Tree


### Array(list)
논리적 순서와 물리적 순서가 일치함 (메모리에 순차적)

*장점*
- index값을 통한 접근이 가능하며, indexing, slicing이 가능함
- 다중 차원 배열이 존재할 수 있다.

*단점*
- 삽입, 삭제 등에 대한 연산의 경우, 메모리가 이어져 있어야 하기 때문에 shift연산이 필요
- 처음 생성될 때 메모리를 미리 할당하기 때문에 데이터가 메모리 이상으로 많아지면 resize가 필요

⇒ 특정 요소를 빠르게 읽거나, 순서가 중요한 데이터나, 데이터가 자주 변하지 않을 경우 사용하는 것이 좋음


### LinkedList
삽입, 삭제 연산에 대한 Array의 비효율성을 극복하기 위해 만들어짐  
단일 연결 리스트, 이중 연결 리스트, 환형 연결 리스트가 있다

- 논리적 순서와 물리적 순서가 다름(논리적으로는 순서대로이지만, 물리적으로는 순서대로 되어있지 않음)
- 각 원소에는 다음 index 위치의 물리적 주소를 가지고 있음
- 이중 연결, 환형 연결 리스트에는 이전 index의 물리적 주소도 가지고 있음

*장점*
- 삽입, 삭제에 대한 연산 시 물리적 주소만 변경해주면 되기 때문에 연산이 쉽고 빠름

*단점*
- 다음 노드의 위치를 저장하기 위한 추가 공간이 필요함
- 원하는 index를 참조하기 위해 1번 index부터 차례대로 접근해야함


### Stack
LIFO(Last In First Out)  
미로찾기, 괄호 유효성 체크 등에 활용

- 참조 지역성이 높음(한번 참조된 곳은 다시 참조될 확률 ↑)
- 데이터 탐색이 어려움

⇒ 함수 호출 기록을 저장할 때 사용(콜스택)


### Queue
FIFO(First In First Out)  
우선순위, 힙 구현 등에 활용

⇒ 프린터의 인쇄 대기 목록 등에 사용


### Graph
node와 edge를 하나로 모아 놓은 자료구조, 네트워크 모델
- 2개 이상의 경로가 가능
- 순회가 가능하며 DFS(Depth First Search)나 BFS(Breadth First Search)로 이루어짐
- 방향그래프와 무방향 그래프가 있음
- 순환 혹은 비순환


### Tree
계층적 구조를 표현한 자료구조  
- 그래프의 한 종류로 cycle이 없음
- Directed Acyclic Graph(DAG) : 방향성이 있는 비순환 그래프
- node, edge(노드와 노드를 연결하는 선), root node, terminal node(= leaf node, 최하위 노드), internal node(최하위 노드를 제외한 모든 노드)으로 이루어짐

**Binary Tree**  
Full Binary Tree(포화 이진 트리) : 모든 레벨이 가득 찬 이진 트리  
Complete Binary Tree(완전 이진 트리) : 왼쪽에서 오른쪽으로 순서대로 채워진 이진 트리
Perfect Binary Tree()
- 루트 노드를 제외한 모든 노드의 자식이 2개 이하

**Binary Search Tree(이진 탐색 트리)**  
부모 노드의 값은 왼쪽 자식보다 크고, 오른쪽 자식보다 작다 → 탐색할 개수가 절반씩 줆  
**Red Black Tree**  
트리가 한쪽으로 치우쳐 지는것을 해결하기 위한 방법 중 Rebalancing 기법 중 하나  
**Binray Heap**  
max heap과 min heap으로 이루어짐  
힙은 우선순위 큐를 위해 만들어짐


### Hash table
key-value를 1:1로 매핑해서 저장하는 자료구조
- key, Hash function, Hash, value, Bucket(저장소)로 이루어짐
- key값을 통해 value를 조작할 수 있음(저장, 검색, 수정, 삭제)
- key는 중복될 수 없다
- key → hash function → hash를 배열의 index로 사용하고, hash는 value와 매칭되어 저장됨
- hash가 충돌 될 때(서로 다른 key가 중복 hash로 나오는 경우)
  - separating chaining : 해당 인덱스에 연결(LinkedList나 Red Black Tree 사용) → 추가 메모리가 필요
  - open addressing : 다른 인덱스를 탐색 → 추가 메모리 필요 없음
  - resize : 저장 공간이 채워지면 저장소를 두배로 확장

*장점*
- 적은 리소스로 많은 데이터 효율적으로 관리 가능
- 검색, 삽입, 삭제가 빠름
- key와 hash에 연관성이 없어 보안에 유리

*단점*
- 충돌발생
- 공간 복잡도 증가
- 해시 함수에 의존도가 높아짐


>Hash table vs Hash map  
Hash table : 비동기에서 사용, NULL 허용  
Hash map : 동기에서 사용, NULL 허용하지 않음
