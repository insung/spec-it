# SSE message contract fixture

이 fixture는 하나의 HTTP streaming 계약에서 stream open 전 오류는 HTTP status로, open 후 오류는 typed SSE event로 표현하는 구조를 보여줍니다. schema validation은 두 phase의 필드 조합만 확인합니다.

실제 `Content-Type`, event framing, heartbeat, disconnect, reconnect, resume, proxy buffering, 중복 event 처리와 UI 동작은 실행 증거가 없으므로 `not-implemented`입니다. 이 예제는 특정 제품이나 프로젝트의 운영 계약이 아닙니다.
