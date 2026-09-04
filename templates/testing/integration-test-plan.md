# Integration test plan

- Change or boundary: <database, queue, API, filesystem, cloud service>
- Selected profile: <profile ID>
- Test level: <component, contract, ephemeral integration>
- Environment and isolation: <container, namespace, temporary account or stack>
- Environment purpose: <local/CI contract, stage deployment boundary, production bounded smoke>
- Fixture ownership: <creator and cleanup>
- Data source and classification: <synthetic, generated, de-identified, production-derived plus approval>
- Data minimization or masking evidence: <method, verifier, limitations, or not-applicable>
- External dependency behavior: <real, emulator, fake, unavailable>
- Side-effect sinks: <email, payment, webhook, scheduler, queue and how production destinations are blocked>
- Access and egress: <who can access; allowed destinations>
- Assertions: <observable contract and failure behavior>
- Cleanup and rollback: <method>
- Abort condition and monitoring: <stop signal, owner, blast radius>
- TTL and destruction evidence: <deadline and result when temporary data or infrastructure exists>
- Cost and expected duration: <estimate>
- Evidence freshness trigger: <risk or change trigger>
- Exemption reason: <only when applicable>

## 적용되는 경우에만 채우는 경계 검사

미발행 0.2.0 초안의 [ARCH-005](../../rules/architecture/ARCH-005.md), [DATA-007](../../rules/data/DATA-007.md), [MSG-001](../../rules/messages/MSG-001.md), [MSG-002](../../rules/messages/MSG-002.md)를 위한 시작 항목입니다. 테스트 환경이나 예제 파일이 있다는 사실을 실행 성공으로 표시하지 않습니다.

| 경계 | 확인할 항목 | 실제 증거 / 적용되지 않는 이유 |
| --- | --- | --- |
| 트랜잭션 | owner, 동일 연결, 중간 실패/rollback, 동시 요청, 중복 요청 | <test reference / reason> |
| 프로시저 | SQL 정본, 목표 DB 버전, 새 설치/upgrade, 권한, 구·신 호출자, 복구 | <test reference / reason> |
| 공개 결과 | code별 실제 응답/parameter 타입, HTTP 의미, 비밀정보 비노출 | <test reference / reason> |
| 사용자 안내 | 노출/비노출, 우선순위, 중복 억제, 해제, 결과 미확인 | <test reference / reason> |
| 번역/호환성 | 지원 locale, 누락 key/치환 값, 모르는 code, 구버전 소비자 | <test reference / reason> |
| 로그/후속 작업 | redaction, correlation, 중복 알림, retry 안전, delivery 실패 | <test reference / reason> |
| API 계약 | transport/application mapping, 실제 field/path/method, audience, authn/authz, internal 비노출 | <contract/integration reference / reason> |
| 환경 안전 | data source, isolation, egress·side-effect sink, abort, TTL·cleanup | <TST-006 evidence / reason> |

- 승인된 수용 기준과 확인자: <intent owner / acceptance reference; 실행 코드에서 역으로 추출한 기대값만 사용하지 않음>
- 검사한 코드: <commit plus dirty diff identity/scope; 미커밋 변경이 있으면 commit만 적지 않음>
- 계약과 소비자 버전: <contract version / consumer versions>
- 실행 기록: <command, engine/runtime version, time, result, redacted artifact reference>
- 독립 검토: <verifier / observation against acceptance>
- 미확인·미구현: <planned checks stay human-review; actual violations are fail>
