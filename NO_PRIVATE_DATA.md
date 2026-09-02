# No Private Data

이 공개 core에는 개인 판단 기록, 회사명·프로젝트명, 실제 계정·리전·ARN·IP, 고객·사용자 정보, secret, 내부 장애 원문을 넣지 않습니다.

비공개 내용은 별도 overlay에 두고 공개 core의 `policy_version`을 고정합니다. overlay는 규칙을 추가하거나 강화할 수 있습니다. 완화는 공개 규칙이 요구하는 예외 형식과 만료 조건을 따릅니다.
