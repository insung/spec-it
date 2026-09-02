# Code comments

주석은 코드가 이미 말하는 동작을 반복하는 대신 이유, 제약, 비직관적 선택, 외부 계약을 설명합니다. 복잡한 분기가 생기면 먼저 이름 있는 함수·정책 객체·타입으로 구조를 드러내고, 그래도 남는 업무 이유를 주석으로 보완합니다.

Python은 공개 module·class·function의 계약에 docstring을 사용하고 내부 구현은 필요한 이유만 인라인 주석으로 남기는 방향을 취합니다. Go는 exported identifier의 doc comment로 계약을 설명하고 내부 분기에는 왜 그 조건이 필요한지를 남깁니다. 정확한 형식은 language profile이 추가합니다.

정본 규칙: [CODE-001](../rules/code/CODE-001.md).
