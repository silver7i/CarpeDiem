# TIL
1. 라이브 강의 복습 (HTML&CSS)
2. 과제 풀기
3. BFS, 트리 강의 다시 듣기

---
## 오늘의 수업 : HTML&CSS
---
## HTML
웹페이지를 만들기 위한 언어\
**HT** - **H**yper **T**ext, 문서와 문서가 링크로 연결되어 있다.\
**ML** - **M**arkup **L**anguage, 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

### 문서의 구조 < ! + tab>
```
<!DOCTYPE html> : 해당 문서의 타입

<html>

<head> : 사용자에게 보이지 않음

    문서를 정의하는 메타 데이터를 작성

    <title> : 브라우저 탭 제목</title>

</head>

<body>

    <p>문서에 표시되는 컨텐츠를 작성</p>

</body>

</html>
```

---
## CSS
웹 페이지의 디자인과 레이아웃을 구성하는 언어

### CSS 적용 방법
1. 인라인(Inline) 스타일
2. 내부(Internal) 스타일 시트
3. 외부(External) 스타일 시트
```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link rel="stylesheet" href="style.css">
  <style>
    h2 {
      color: red;
    }
  </style>
</head>

<body>
  <h1 style="color: blue; background-color: yellow;">Inline Style</h1>
  <h2>Internal Style</h2>
  <h3>External Style</h3>
</body>

</html>
```

### CSS Selectors
HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자
```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* 전체 선택자 */
    * {
      color: red;
    }
    /* 요소 선택자 */
    h2 {
      color: orange;
    }
    h3,
    h4 {
      color: blue;
    }

    /* class 선택자 */
    .green {
      color: green;
    }

    /* id 선택자 */
    #purple {
      color:purple;
    }

    /* 자식 결합자 */
    .green > span {
      font-size: 50px;
    }

    /* 자손 결합자 */
    .green li {
      color: brown;
    }

    /* 속성 선택자 */
    [class^="y"] {
      color: yellow;
    }
  </style>
</head>

<body>
  <h1 class="green">Heading</h1>
  <h2>선택자</h2>
  <h3>연습</h3>
  <h4>반가워요</h4>
  <p id="purple">과목 목록</p>
  <ul class="green">
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹
      <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>PYTHON</li>
      </ol>
    </li>
  </ul>
  <p class="green">Lorem, <span>ipsum</span> dolor.</p>
  <p class="yellow">TEST</p>
</body>

</html>
```

### 명시도가 높은 순
1. !important
2. Inline 스타일
3. 선택자 (id>class>tag)
4. 소스 코드 선언 순서

### CSS Declaration
선택된 요소에 적용할 스타일을 구체적으로 명시하는 부분


### CSS Box Model
웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델