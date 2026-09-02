# Security and supply chain

모든 프로젝트가 같은 무게를 갖지는 않지만 dependency lock, vulnerability scan, secret scan, least privilege, 외부 dependency의 근거를 공통 출발점으로 둡니다. SBOM은 standard·high risk에서 기본 증거이며 lightweight 프로젝트는 기록된 면제를 사용할 수 있습니다.

의무화는 한 번에 완성하지 않습니다. Phase 0는 규칙과 evidence contract를 정의하고, Phase 1 validator, 실제 프로젝트 pilot, 안정화된 CI 순으로 승격합니다. 구현되지 않은 검사는 `planned` 또는 `advisory`로 표시하며 통과로 가장하지 않습니다.

정본 규칙: [SEC-002](../rules/security/SEC-002.md), [RULE-002](../rules/rule-system/RULE-002.md).
