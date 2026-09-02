# Further reading

이 목록은 규칙 정본이 아니라 배경 지식을 넓히기 위한 출발점입니다.

## Architecture and testing

- Robert C. Martin, *Clean Architecture* — 의존성 방향과 경계의 배경
- Kent Beck, *Test-Driven Development: By Example* — red-green-refactor의 원형
- Martin Fowler, [Architecture Decision Record](https://martinfowler.com/articles/scaling-architecture-conversationally.html) — 결정과 근거를 가까이 보존하는 방법

## Configuration, infrastructure, and delivery

- [The Twelve-Factor App: Config](https://www.12factor.net/config) — 환경별 설정과 코드 분리
- [Terraform module composition](https://developer.hashicorp.com/terraform/language/modules/develop/composition) — 얕은 module 조합
- [AWS SAM local environment variables](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-using-invoke.html) — 로컬 Lambda 실행의 환경 설정
- [GitHub push protection](https://docs.github.com/en/code-security/concepts/secret-security/command-line-push-protection) — push 시 secret 방지

## Observability and security

- [OpenTelemetry specifications](https://opentelemetry.io/docs/specs/) — trace, metric, log와 context의 표준
- [SLSA](https://slsa.dev/spec/) — 공급망 무결성 성숙 모델
- [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) — 애플리케이션 보안 검증 항목

## Deferred domains

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)와 [Web Vitals](https://web.dev/articles/vitals) — frontend profile 재검토 시
- [Zephyr Twister](https://docs.zephyrproject.org/latest/develop/test/twister.html), MISRA, CERT C — embedded profile 재검토 시

도구나 표준을 그대로 규칙으로 복사하지 않고, 실제 프로젝트에서 필요한 부분과 비용을 확인한 뒤 `spec-it:evolve`로 규칙 후보를 만듭니다.
