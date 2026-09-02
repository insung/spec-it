---
id: DATA-006
title: Evidence-based stream selection
status: active
introduced: 0.1.0
scope: event-streams
condition: "A project selects or changes an event streaming platform."
statement: "MUST compare producer and consumer model, fan-out, ordering, replay window, ecosystem, operations, recovery, and total cost."
forbidden: ["Standardize Kinesis or Kafka without workload evidence.", "Select Kafka only for future scale."]
evidence: ["ADR names workload assumptions, alternatives, pilot or estimate, and revisit triggers."]
exception: {allowed: true, requirements: ["Organizational platform mandate and measured local impact."]}
approver: [architecture-owner, data-owner]
rationale: "Streaming products optimize different consumer and operating models."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# DATA-006 — Stream choice

Kinesis는 AWS 관리 비용이 유리한 경우의 후보이고, Kafka는 Kafka 생태계·다수 소비자·긴 replay 같은 요구가 결정적일 때의 후보입니다.
