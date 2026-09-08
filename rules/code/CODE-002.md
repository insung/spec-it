---
id: CODE-002
title: Project-owned identifiers use English
status: active
introduced: 0.2.0
scope: project-owned-source
condition: "A project-owned source identifier, source filename, package, test name, or structured log key is added or changed."
statement: "MUST use an English identifier that communicates its role without requiring translation or private team context."
forbidden: ["Use non-English project-owned identifiers.", "Use a single letter or unexplained abbreviation outside an established narrow convention.", "Rename generated, vendor, protocol-defined, or externally owned identifiers to imitate this rule."]
evidence: ["Changed identifier review distinguishes project-owned names from generated, external, and language-defined names."]
exception: {allowed: true, requirements: ["The identifier is externally defined, generated, or a conventional narrow-scope mathematical or mechanical temporary name, and the reason is recorded when not self-evident."]}
approver: [architecture-owner]
rationale: "A shared language for project-owned identifiers reduces search, review, and handoff cost across humans and AI agents."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# CODE-002 — English project identifiers

이 규칙은 함수·메서드·타입·클래스·인터페이스·변수·상수·파일·package/module·test identifier와 structured log key에 적용합니다. 사용자 메시지, 번역 resource의 표시 문구, 설명 문서와 필요한 주석의 자연어까지 영어로 강제하지 않습니다.

`tmp`는 짧은 지역 범위의 기계적 중간값이고 실제 역할 이름이 오히려 거짓 정밀도를 만들 때만 허용합니다. 값이 분기·반환·부작용·계층 경계에 관여하면 의미 있는 이름을 사용합니다.
