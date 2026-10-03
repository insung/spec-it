# 구현과 PR 리뷰 인계

- Issue: [#3](https://github.com/insung/spec-it/issues/3); PR: 구현 세션에서 생성하지 않음
- Plan / Todo: [plan](plan.md), [01](task-01-guidance.md), [02](task-02-validation.md)
- base: `d9ed1663f95bb6c7746aa79bb99c208d8e07cc1d`; 계획: `7de83171e3c4ecc42c1e55ffd98e737fe8138dba`
- 지침 구현: `50158dee08acb5dae5fcdcb1d8a754660890d64a`; 관찰 설명: `643288b6bb0fa314d7802f001ef1dafba183d79e`
- 실제 실행 담당: 별도 구현 세션 `implement_pair_docs`; 매 실행 새 하위 실행자가 응답 생성, 판정은 구현 세션
- 검토: `review-pending`; 분리된 검토 기준·입력을 읽거나 작성하지 않음
- spec-it: manifest/lock의 source `.`와 pin `0.7.0`, 정본 `rules/` 확인. 정책·lock·VERSION 변경 없음

## 사용자 의도와 구현 결과

| AC | 기대 동작 | 구현 경로/커밋 | 대응 TC | 실제 충족·미확인 |
| --- | --- | --- | --- | --- |
| AC-01 | AGENTS 기본 경로와 선택적 후보 구분 | README·pair-work-cycle·skills/README·pair SKILL; 50158dee | TC-01/04 | 문서 경계 확인; 설치·자동 선택 미검증 |
| AC-02 | 일반 질문 직접 답변과 승인 경계 보존 | template AGENTS·converge·pair SKILL; 50158dee | TC-01/04 | 원문 확인·합성 관찰; 실사용 미검증 |
| AC-03/04 | S3 여섯 단계와 공통화 조건·권한·소비자 구분 | s3-shared-library-pairing; 50158dee | TC-02/04 | 규칙 대조; 실제 구현·AWS 호출 제외 |
| AC-05/06 | 문서 링크와 증거 상태 정합성 | 색인·Unreleased·pilots; 50158dee/643288b6 | TC-03/04/F01 | 정적 검사 및 v1 역사·합성·실사용 구분 |
| AC-07/08 | 기준선·원본 보존 및 구현/검토 분리 | 계획·허용 경로·인계 | TC-05/F02 | 원본11개·index 전후 지문 일치, 검토 자료 미열람 |

## 계획 대비 차이와 판단

계획의11개 후보 경로만 반입했다. 스냅샷에서 impact의 미발행 표시를 제거한 부분은 pair 주제 밖이므로 기준선의 표시를 보존했다. 기존 정책·실행 코드와 다른 검증 작업을 변경하지 않았다. 기준선 합성 응답은 이미 요청 경계를 유지했으므로 실패를 만들거나 추가 지침의 효과를 단정하지 않았다. 검토 자료의 존재와 정합성은 부모 검토 세션 담당이다.

## 검증 요약과 증거

| TC/AC | 사례·기대 | 실제·상태 | 작업·실행 위치 | 대상·환경·시각 |
| --- | --- | --- | --- | --- |
| TC-01 | 기본/후보·일반 질문·권한 경계, 강제 설치·새 권한 부재 | 통과: 원문 대조 | 계획11개 파일 읽기; 리포 루트 | 50158dee; 2026-10-03 KST |
| TC-02 | S3 설명과 ARCH-001/002/003·domain-core-libraries, 책임·소비자 구분 | 통과: 원문 대조 및 runner 참조 제거 | 규칙·문서 읽기; 리포 루트 | 50158dee; 2026-10-03 KST |
| TC-03/F01 | 상대 링크·fragment·front matter·diff 공백, 유효한 구조와 증거 구분 | 통과: 최종 상대 링크129개, 투영 template 링크5개 별도 구분; 오류0 | Python 검사 및 git diff --check; 리포 루트 | 643288b6와 후속 기록 문서; macOS/Python3/Git; 2026-10-03 KST |
| TC-04 | 고정3입력의 기준선/후보 응답, task의 경계 보존 | 합성 관찰 통과: 각 조건·입력3/3, 총18회; 실제 RED 실패 없음 | 매 실행 새 컨텍스트 실행자 | 기준선d9ed1663·후보50158dee; 2026-10-03 KST |
| TC-05/F02 | 보호 경로 무변경·원본/index 보존·분리 | 구현 범위 통과: 허용 경로와 원본11개/index 일치·검토자료 미열람 | git diff 경로 및 SHA-256; 리포 루트 | 643288b6와 후속 기록 문서; 최종 시각 아래 기록 |

정적 검사로 실제 모델 행동을 판정하지 않았다. 합성 응답으로 실제 저장소 탐색·구현·운영·정책 강제를 검증하지 않았다.

## 합성 시나리오 입력과 관찰

### 조건과 실행 방법

기준선은 `d9ed1663f95bb6c7746aa79bb99c208d8e07cc1d`의 `templates/project/AGENTS.md`와 `skills/spec-it-converge/SKILL.md`를 순서대로 두 개의 개행으로 연결한 지침이다. 후보는 `50158dee08acb5dae5fcdcb1d8a754660890d64a`의 같은 두 파일에 `skills/spec-it-pair/SKILL.md`를 같은 방식으로 추가했다. 후보의 세 지침 파일 bytes는 설명 보완 커밋643288b6에서도 동일하다. 프로젝트·규칙 요약은 가상 요청 자료이며 spec-it 자체 manifest의 선택 규칙을 뜻하지 않는다.

실행 방법은 `collaboration.spawn_agent(fork_turns="none")`으로 매번 새 실행자를 시작하는 것이다. 해당 지침과 해당 입력만 읽고 제공된 가상 자료만 사용하며 외부 호출·원본 수정·판정을 수행하지 않도록 지시했다. 기대 결과·검토 기준·다른 실행 결과는 제공하지 않았다. 실행자는 한국어 사용자 응답을 별도 로컬 증거 파일에 저장하고 반환했다. 구현 세션이 task의 경계와 대조했으며 독립 검토를 대신하지 않는다. 원시 로그와 머신 절대 경로는 공개 문서에 포함하지 않았다.

### 원문 입력

#### 일반

```text
RDS와 EC2는 뭐가 달라? 일반 개념만 설명해줘.
```

#### 승인된 프로젝트

```text
승인된 예산과 복구 목표 안에서 EC2 설정을 같이 검토해줘. 지금은 파일 수정 없이 아래 자료로 다음 작은 검증을 정리해줘.
가상 서비스 자료: 기존 ADR은 EC2 유지, RTO 30분, 월 총비용 상한 30만원을 승인했다. EC2 1대와 배포 설정에서 health check 30초, ASG 최소/최대 1/1을 확인했다. 지난 회차의 복구 훈련은 22분이었으나 이번 변경 후 훈련은 아직 없다. 최근 CPU 최대 62%이고 메모리·동시 접속 수는 미측정이다. 별도 증설·EKS 이전·AWS 조작은 승인하지 않았다. 적용 lock은 INFRA-001/002와 COST-001/002를 포함하며 승인 목표·총비용·측정·재검토 조건으로 선택을 평가한다.
```

#### S3 재사용

```text
A에 S3 업로드 기능을 추가하려고 한다. 아래 가상 저장소 자료에서 구현 위치와 다음 작은 작업을 판단해줘. 아직 파일은 수정하지 마.
A는 보고서 업로드 시 고객별 경로와 보존기간을 결정한다. some-library/object-storage에는 upload(bucket,key,body) 공개 API와 재시도·오류 계약 테스트가 있다. A는 아직 이를 import하지 않는다. 라이브러리의 현행 API는 A 업로드 요건을 충족한다. B의 업로드 도입은 미래 계획이며 B 저장소는 읽을 수 없다. A의 lock에 ARCH-001/002/003과 COST-002가 선택돼 있다: 도메인 정책은 SDK와 독립, 책임 경계가 있는 모듈, 추상화의 실제 변동성·외부 경계 격리·승인 교체 근거, 총비용 비교. 승인 범위는 A 내부 변경뿐이다. 관련 라이브러리는 읽기만 허용됐고 새 릴리스는 승인되지 않았다.
```

### 실행별 응답과 판정

저장 시각은 응답 파일 저장 시각이며 소요 시간 측정값이 아니다. 추가 사용자 질문은 별도 답변을 요구하는 질문 수이며 설명용 질문이나 다음 측정 항목을 제외했다. 각 실행자 suffix는 구현 세션 하위의 실제 실행자 이름이다.

| 실행자 suffix | 응답 저장 시각 KST | 실제 응답 요약 | 추가 질문 수 | 구현 세션 판정 |
| --- | --- | --- | --- | --- |
| red_general_1 | 2026-10-03 14:41:28 | EC2 가상 서버와 RDS 관리형 DB 비교, 직접 설명 | 0 | task의 요청 경계 충족 |
| red_general_2 | 2026-10-03 14:43:00 | 관리 책임과 쇼핑몰 예시, 직접 설명 | 0 | task의 요청 경계 충족 |
| red_general_3 | 2026-10-03 14:44:27 | 관리 범위·자유도·백업 비교, 직접 설명 | 0 | task의 요청 경계 충족 |
| red_project_1 | 2026-10-03 14:42:11 | 과거22분과 현재 미측정 구분, 복구 훈련·자원·총비용 확인 제안 | 0 | task의 요청 경계 충족 |
| red_project_2 | 2026-10-03 14:43:23 | 복구·자원·비용 자료 확인, 총비용 미확인과 실행 경계 구분 | 0 | task의 요청 경계 충족 |
| red_project_3 | 2026-10-03 14:45:48 | ASG1/1·health check 한계, 다음 복구 절차·훈련 확인 | 0 | task의 요청 경계 충족 |
| red_s3_1 | 2026-10-03 14:42:21 | 기존 API 재사용·A 내부 연결, B 접근·총비용 측정 미확인 | 0 | task의 요청 경계 충족 |
| red_s3_2 | 2026-10-03 14:44:07 | 기존 API·A 책임 경계, 보존기간 결정과 실제 적용 공백 발견 | 0 | task의 요청 경계 충족 |
| red_s3_3 | 2026-10-03 14:46:01 | 기존 API·A 최소 변경, 보존기간 적용과 소스 revision 확인 제안 | 0 | task의 요청 경계 충족 |
| green_general_1 | 2026-10-03 14:47:48 | EC2 서버와 RDS 관리형 DB 관리 책임 비교, 직접 설명 | 0 | task의 요청 경계 충족 |
| green_general_2 | 2026-10-03 14:50:51 | EC2/RDS 용도·관리·자유도 비교, 직접 설명 | 0 | task의 요청 경계 충족 |
| green_general_3 | 2026-10-03 14:52:28 | 운영 책임·백업·함께 사용하는 구조, 직접 설명 | 0 | task의 요청 경계 충족 |
| green_project_1 | 2026-10-03 14:48:15 | 변경 후 복구 훈련 계획, 과거22분·health check·비용 미확인 구분 | 0 | task의 요청 경계 충족 |
| green_project_2 | 2026-10-03 14:51:35 | 변경 상세와 기존 복구 절차의 단계 대조, 측정·실행 경계 구분 | 0 | task의 요청 경계 충족 |
| green_project_3 | 2026-10-03 14:53:14 | 복구 절차 사전 점검, 과거 기록·현재 미측정·총비용 미확인 구분 | 0 | task의 요청 경계 충족 |
| green_s3_1 | 2026-10-03 14:49:57 | 기존 API·테스트·A 미import 구분, A 읽기 조사와 B 미확인 | 0 | task의 요청 경계 충족 |
| green_s3_2 | 2026-10-03 14:51:49 | 기존 API와 A 내부 연결, 보존기간 API 인자 부재·적용 공백 발견 | 0 | task의 요청 경계 충족 |
| green_s3_3 | 2026-10-03 14:53:32 | 기존 API와 A 책임 경계, lifecycle 등 보존기간 실제 적용 미확인 | 0 | task의 요청 경계 충족 |

RED는 변경 전 단계의 이름이며 기준선 결함이 발생했다는 뜻이 아니다. 기준선·후보 모두 일반 직접 답변3/3, 승인된 프로젝트의 승인 재사용·미확인 구분3/3, S3의 기존 API 재사용·A 변경 경계·B 미확인3/3으로 관찰됐다. 추가 사용자 질문은 모두0개였다.

발견과 추천은 두 조건에서 겹쳤다. 프로젝트 응답은 과거 복구22분과 현재 변경 후 미측정, CPU만으로 용량을 확정할 수 없음, 총비용 자료 부족을 양쪽 모두 언급했다. S3 응답도 양쪽 모두 기존 API 재사용과 A 내부 연동을 추천했다. 보존기간 결정과 실제 적용의 공백은 기준선2·3회와 후보2·3회에서 구체적으로 다뤘다. 추가 지침의 개선·필요성·조사 시간 단축은 확인되지 않았다.

### 증거 지문

원문 증거는 로컬 보관하고 부모 세션에 접근 위치를 별도로 인계했다. 공개 문서에는 입력·요약·판정·SHA-256을 남겼다.

| 입력/지침/응답 | SHA-256 |
| --- | --- |
| baseline-instructions.md | `fd5bd431c8773c7befea4374f40bd02efb1855a993603bc66c8d2a9370940198` |
| candidate-instructions.md | `f53b68e17c5985f7b7e6e3810659755d9d5c915f54da97ea848e7a930a70e1da` |
| general.txt | `5bccf72a703ebd79d469f9fc645a07da960f4409805e7147f7200f54af5d22e7` |
| project.txt | `016cccdb2cfde79649af67d72f8809ff707df6edd5b7d77980377b8ea96de3ab` |
| s3.txt | `1ff1dad33bba9cdd935ac58a26a58443a0dedbaebf39161813add9aada01e1dc` |
| red_general_1.txt | `f7d8661814bd505a1f939e94bf4fdffd68d64be20a995db31fabcb938cdec68c` |
| red_general_2.txt | `58de0bbe1793b1387b10857de1bc98805ae62c3b5732a4fd3fb7cace62c4e185` |
| red_general_3.txt | `25b954f602a804cd0216025da2fec6a980861f7b366356dcf211c22924620812` |
| red_project_1.txt | `fb7c36a1a8eb2179ab518c599203cf9ce48291dc1dfa090168e1a30f3c9bd466` |
| red_project_2.txt | `de693f4f914fdd9dddcdc4043c599f1467c9a446fc58a45dc25b7ecc4561e1d2` |
| red_project_3.txt | `fa6eb48b359cbc4b110bb814a8e95dc2ed7ef0cac1d839bd794e9da7763e8f87` |
| red_s3_1.txt | `205e7f211986c7a1769fe2a7a3eb7ce8983f37ea7d19c42c99b49a7416f8ee9e` |
| red_s3_2.txt | `52cc8c0f4a57ef35a22744692327aa61303df0e9f1a8c03d192f03002b620a39` |
| red_s3_3.txt | `f1c3df274ffaef9a82257e53ead1c0de99f36b381678ff86cd74b3787518b6d1` |
| green_general_1.txt | `5fca7d5c99ea5705175c07e666c4fcaa7421bae684f9ca4484a506222c31a7be` |
| green_general_2.txt | `dfe76448f3b3827111560f8b5505d02b8f59e6c78417f54767ef1ab1b69a3086` |
| green_general_3.txt | `a434218ff6068da8d6272507623553ccc900790462b22b7e8658364d2e620547` |
| green_project_1.txt | `b655cc25527e7c45cab11b2c90351b3e258189f2bf07c852b3c2d84a37eaa7ea` |
| green_project_2.txt | `8ba09a939f642def4d4910b8cd9bea09620e51a9639a6972c3f10f57eab7d7e2` |
| green_project_3.txt | `7d8cc7c47023c7875421ab67dafb650e17b8bcdc61ada9702c47c3916a414079` |
| green_s3_1.txt | `57abe27f0470691203ae0376b7eaca27bfadb98924bc8661c6a97cf9b1edb5e4` |
| green_s3_2.txt | `12cc7fce26c2a740bfde664a354886e9b197fcebc3de6847f9053572c94cdc4a` |
| green_s3_3.txt | `a5cf21f28b2477b60380f414a4ef27e9b7238307b2b788bf1f6d79d7e4bbcadb` |

## 원본과 보호 경로 보존

- 최종 대조 시각: 2026-10-03T20:51:30.858163+09:00
- 원본 main 후보11개: 인계 스냅샷과 전후 SHA-256 모두 일치
- 원본 main index: 전후 SHA-256 `a83546c5f0395e6037c7400296ed5f6320e1137210123135b12dcd5174d01474` 일치
- 허용 범위: 후보11개 경로와 이 Issue의 plan/task/handoff만 변경
- 보호 범위: rules·profiles·schemas·manifest·lock·VERSION·hook·runner 실행 코드 무변경
- .comments: 구현 worktree에 디렉터리 없음, 포함할 resolved/미승인 열린 스레드 없음
- 다른 verification 작업본: 열람·수정하지 않음
- 검토 분리: 검토 브랜치·worktree·기준·입력을 열람하지 않음. 자료의 존재와 정합성은 부모 검토 세션 확인

## 커밋과 문서 상태

- 50158dee: 11개 계획 경로 반입, AGENTS 기본/후보·S3 경계 설명
- 643288b6: v1 역사와18회 합성 관찰·실사용 미검증 구분
- 후속 plan/task/handoff 기록 커밋의 HEAD: 부모 세션에 실제 hash 전달. 자기 hash 기록을 위한 amend 없음
- 확인한 원격 문서: Issue #3. 변경 문서의 원격 게시·push·PR 상태는 부모 세션에서 재조회

## 미실행·위험·전달

실제 프로젝트의 파일 탐색·수정·테스트·배포, AWS 통합·부하, 호스트의 implicit 선택·설치 효과는 미실행이다. 기존 active policy loop 코드 테스트는 실행 코드 변화가 없어 이번 문서 변경의 행동 증거로 사용하지 않았다. 변경은 instruction-only 후보와 설명이므로 소비자 구현·정책 채택·외부 시스템 동작을 바꾸지 않는다. 추가 pair의 필요성은 미확인이다.

구현 세션은 push·PR·머지·발행을 실행하지 않았다. 부모 세션이 독립 검토와 원격 전달을 맡는다. 최종 머지는 사용자 승인 후 진행하며 롤백은 새 커밋을 revert하는 별도 검토로 처리한다. 기존 기준선 이력을 재작성하지 않는다.

## 최종 정적 검사 재현

실제 작업 디렉터리는 구현 branch 리포 루트다. 아래 명령은 변경 대상 전체의 상대 링크·외부 fragment·front matter·후보/권한 경계와 공백을 검사한다. 소비자에 투영할 template의 `.architecture` 링크5개는 실행 리포의 경로로 검사하지 않는다. 같은 파일 안의 task anchor는 `<a id>`와 제목을 원문 대조했다.

```sh
python3 - <<'CHECK_LINKS'
from pathlib import Path
import re,json,hashlib,subprocess
root=Path.cwd()
files=['CHANGELOG.md', 'README.md', 'docs/README.md', 'docs/agent-work-cycle.md', 'skills/README.md', 'skills/spec-it-converge/SKILL.md', 'templates/project/AGENTS.md', 'docs/pair-work-cycle.md', 'docs/pilots/pair-workflow-acceptance.md', 'docs/s3-shared-library-pairing.md', 'skills/spec-it-pair/SKILL.md']
files += ['docs/git-workflows/2026-10/03_3_pair-workflow/'+x for x in ['plan.md','task-01-guidance.md','task-02-validation.md','handoff.md'] if (root/'docs/git-workflows/2026-10/03_3_pair-workflow'/x).exists()]
errors=[];count=0; projected=0
for file in files:
 text=(root/file).read_text(); cleaned=re.sub(r'```.*?```','',text,flags=re.S)
 for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',cleaned):
  link=link.strip().split(' ',1)[0]
  if re.match(r'[a-zA-Z][a-zA-Z+.-]*:',link) or link.startswith('#'):continue
  if file=='templates/project/AGENTS.md' and link.startswith('.architecture/'):
   projected+=1; continue
  target=link.split('#',1)[0]
  if not target:continue
  count+=1
  destination=(root/file).parent.joinpath(target)
  if not destination.exists():errors.append(file+': '+link);continue
  if '#' in link and destination.is_file():
   body=destination.read_text()
   anchors=set(re.findall(r'<a id="([^"]+)"',body))
   for heading in re.findall(r'^#{1,6} (.+)$',body,flags=re.M):
    slug=re.sub(r'[^\w\s-]','',heading.lower()).replace(' ','-')
    anchors.add(slug)
   if link.split('#',1)[1] not in anchors:errors.append(file+': missing anchor '+link)
skill=(root/'skills/spec-it-pair/SKILL.md').read_text()
assert re.match(r'---\nname: spec-it-pair\ndescription: .+\n---',skill)
assert 'rules/' in skill and 'Pairing does not grant new edit or external-action authority.' in skill
assert 'local-verification.md' not in (root/'docs/s3-shared-library-pairing.md').read_text()
assert 'unpublished instruction candidate' in skill
assert 'AGENTS.md' in (root/'docs/pair-work-cycle.md').read_text().split('```',1)[0]
assert not errors, errors
subprocess.run(['git','diff','--check'],check=True)
print(json.dumps({'relative_links_checked':count,'projected_template_links':projected,'files_checked':len(files),'errors':errors},ensure_ascii=False))
CHECK_LINKS
git diff --name-only d9ed1663f95bb6c7746aa79bb99c208d8e07cc1d..HEAD
```
