# app source snapshot app-c2 + patch-d2

이 파일은 실행 공간에 제공할 합성 소스의 정확한 내용이다. 실제 제품 코드나 테스트 실행 결과가 아니다.

## src/shared.ts

```ts
export function allowed(excluded: string[], assetId: string) {
  return !excluded.includes(assetId);
}
```

## src/select-a.ts

```ts
import { allowed } from './shared';
export function chooseA(settings, asset) {
  return allowed(settings.excluded, asset.id) ? ['item-a'] : [];
}
```

## src/select-b.ts

```ts
import { allowed } from './shared';
export function chooseB(settings, asset) {
  return allowed(settings.excluded, asset.id) ? ['item-b'] : [];
}
```

## config.json

```json
{"filterFlag": true, "missingSettings": "deny"}
```

## package.json

```json
{"name":"synthetic-selection","private":true,"dependencies":{}}
```

## tests/source.test.ts

```ts
// 이전 실행 기록은 보존되어 있지 않다.
// 현재 snapshot에는 실행 가능한 test command나 runner가 제공되지 않는다.
```
