# TIL
1. 라이브 강의 복습 (CSS Layout)
2. 과제 풀기
3. 트리 강의 다시 듣기

---
## 오늘의 수업 : CSS Layout
---
## CSS Display (outer)
### block 타입 (div)
하나의 독립된 덩어리처럼 동작하는 요소 (밀어내기 가능)

### inline 타입 (span)
문장 안의 단어처럼 흐름에 따라 자연스럽게 배치되는 요소 (밀어내기 불가능)

```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <title>Block vs. Inline 예시</title>
  <style>
    /* 모든 div 요소에 적용 (Block 타입) */
    div {
      background-color: lightblue;
      border: 2px solid blue;
      padding: 15px;
      margin: 10px;
    }

    /* 모든 span 요소에 적용 (Inline 타입) */
    span {
      background-color: lightcoral;
      border: 2px solid red;
      padding: 10px;
      margin: 30px;
      /* 상하 마진은 다른 요소를 밀어내지 못함 */
    }

    /* width 속성 비교를 위한 div */
    .custom-width {
      width: 300px;
      /* block 타입은 width 지정 가능 */
    }
  </style>
</head>

<body>

  <h2>Block 타입 예시 (div)</h2>
  <div>
    첫 번째 div 블록입니다. width를 지정하지 않으면, <strong>한 줄 전체 너비</strong>를 차지합니다.
  </div>
  <div class="custom-width">
    두 번째 div 블록입니다. <strong>width를 300px로 지정</strong>했습니다. 블록 요소는 너비 지정이 가능합니다.
  </div>
  <div>
    세 번째 div 블록입니다. block 요소들은 <strong>자동으로 줄바꿈</strong>이 됩니다.
  </div>

  <hr>

  <h2>Inline 타입 예시 (span)</h2>
  <p>
    문장 속에서
    <span>첫 번째 span</span>
    처럼 흐름에 따라 자연스럽게 배치됩니다.
    <span>두 번째 span</span>
    처럼 줄바꿈 없이 이어지며, <strong>자신의 내용만큼만 공간을 차지</strong>합니다.
    span에 적용된 상하 여백(margin)은 다른 줄에 영향을 주지 못하는 것을 확인해 보세요.
  </p>

</body>

</html>
```

### Normal flow
일반적인 흐름 또는 레이아웃을 변경하지 않은 경우 웹 페이지 요소가 배치되는 방식

### 기타 dispaly 속성
1. inline-block 타입
inline과 block의 특징을 모두 가진 특별한 display 속성
2. none 타입
요소를 화면에 표시하지 않고, 공간조차 부여되지 않음

---
## CSS position
### 1. static
- 요소를 Normal Flow에 따라 배치
- top, right, botton, left 속성이 적용되지 않음

```html
    .static {
      position: static;
      background-color: lightcoral;
    }
```
### 2. relative (상대 위치)
- 요소를 Normal Flow에 따라 배치
- 자신의 원래 위치(static)을 기준으로 이동
- top, right, botton, left 속성으로 위치를 조정
- 다른 요소의 레이아웃에 영향을 주지 않음\
(요소가 차지하는 공간은 static일 때와 같음)

```html
    .relative {
      position: relative;
      background-color: lightblue;
      top: 100px;
      left: 100px;
    }
```

### 3. absolute (절대 위치)
- 요소를 Normal Flow에서 제거
- 가장 가까운 relative 부모 요소를 기준으로 이동
```html
    .container {
      position: relative;
      height: 300px;
      width: 300px;
      border: 1px solid black;
    }
    
# 만족하는 부모 요소가 없다면,
  body 태그를 기준으로 함
```

- top, right, botton, left 속성으로 위치를 조정
- 문서에서 요소가 차지하는 공간이 없어짐
```html
    .absolute {
      position: absolute;
      background-color: lightgreen;
      top: 100px;
      left: 100px;
    }
```
### 4. fixed
- 요소를 Noramal Flow에서 제거
- 현재 화면영역(viewport)을 기준으로 이동
- 스크롤해도 항상 같은 위치에 유지됨
- top, right, bottom, left 속성으로 위치를 조정
- 문서에서 요소가 차지하는 공간이 없어짐
```html
    .fixed {
      position: fixed;
      background-color: gray;
      top: 0;
      right: 0;
    }
```

### 5. sticky
- relative와 fixed의 특성을 결합한 속성
- 스크롤 위치가 임계점에 도달하기 전에는 relative처럼 동작
- 스크롤 위치가 임계점에 도달하면 fixed처럼 화면에 고정
- 다음 sticky 요소가 나오면 이전 sticky 요소의 자리를 대체
```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    body {
      height: 1500px;
    }

    .sticky {
      position: sticky;
      top: 0;
      background-color: lightblue;
      padding: 20px;
      border: 2px solid black;
    }
  </style>
</head>

<body>
  <h1>Sticky positioning</h1>
  <div>
    <div class="sticky">첫 번째 Sticky</div>
    <div>
      <p>내용1</p>
      <p>내용2</p>
      <p>내용3</p>
    </div>
    <div class="sticky">두 번째 Sticky</div>
    <div>
      <p>내용4</p>
      <p>내용5</p>
      <p>내용6</p>
    </div>
    <div class="sticky">세 번째 Sticky</div>
    <div>
      <p>내용7</p>
      <p>내용8</p>
      <p>내용9</p>
    </div>
  </div>
</body>

</html>
```
### z-index
요소의 쌓임 순서를 정의하는 속성

---
## CSS Flexbox (inner)
요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
```
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .container {
      height: 500px;
      border: 1px solid black;
      display: flex;
      /* flex-direction: row; */
      /* flex-direction: column; */
      /* flex-direction: row-reverse; */
      /* flex-direction: column-reverse; */

      /* flex-wrap: nowrap; */
      /* flex-wrap: wrap; */
      /* flex-wrap: wrap-reverse; */

      /* justify-content: flex-start; */
      /* justify-content: center; */
      /* justify-content: flex-end; */

      /* align-content: flex-start; */
      /* align-content: center; */
      /* align-content: flex-end; */

      /* align-items: flex-start; */
      /* align-items: center;  */
      /* align-items: flex-end; */
    }

    .post {
      background-color: grey;
      border: 1px solid black;
      margin: 0.5rem;
      padding: 0.5rem;
    }

    .item1 {
      /* align-self: center; */
    }

    .item2 {
      /* align-self: flex-end; */
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="post item1">
      <h2>Post Title 1</h2>
      <p>Post Content 1</p>
    </div>
    <div class="post item2">
      <h2>Post Title 2</h2>
      <p>Post Content 2</p>
    </div>
    <div class="post item3">
      <h2>Post Title 3</h2>
      <p>Post Content 3</p>
    </div>
    <div class="post item4">
      <h2>Post Title 4</h2>
      <p>Post Content 4</p>
    </div>
  </div>

</body>

</html>
```