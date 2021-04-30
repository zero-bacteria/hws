[toc]



# Javascript 시작



### 기원



* 필요한 이유
  * 브라우저 화면을 동적으로 만들기 위함
  * 브라우저를 조작할 수 있는 유일한 언어
* 브라우저 (browser)
  * 웹 서버에서 이동하며 클라리언트와 서버간 양방향으로 통신하고, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어
  * 인터넷 컨텐츠를 검색 및 열람하도록 함
  * '웹 브라우저' 라고도 함
  * 주요 브라우저 - 크롬, 모질라 파이어폭스, ms edge, opera, safari



* 자바스크립트의 기원?
  * 핵심인물
    * 팀 버너스리 - 웹의 아버지 (WWW, URL, HTTP, HTML)
    * 브랜던 아이크 - js 최초 설계자, 모질라재단 설립자



### DOM, BOM

* DOM

  * HTML, XML 등과 같은 문서를 다루기 위한 언어 독립적인 문서 모델 인터페이스

  * 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델

  * 문서가 구조화되어 있으며 각 요소는 객체로 취급

    * 브라우저의 구성요소들 title, image, content 등을 하나의 객체로 취급

  * 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능

  * 주요객체 

    * window : DOM을 표현하는 창, 가장 최상위 객체(작성시 생략 가능)
    * document : 페이지 콘텐츠의 Entry Point 역할을 하며, <body>등과 같은 수많은 다른 요소들을 포함
    * navigator, location, history, screen

    ![image-20210428102401740](javascript_01.assets/image-20210428102401740.png)



* DOM 해석
  * Parsing
    * 구문분석, 해석
    * 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정



* BOM
  * Browser Object Model
  * 자바스크립트가 브라우저와 소통하기 위한 모델
  * 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수당
  * window 객체는 모든 브라우저로부터 지원받으며 브라우저 window 자체를 지칭





### DOM (Document Object Model) 조작 



* Document는 문서 한 장(HTML)에 해당하고 이를 조작
* DOM 조작 순서
  1. select
  2. manipulation



* DOM 관련 객체의 상속 구조
  * EventTarget
    * Event Listner를 가질 수 있는 객체가 구현하는 DOM 인터페이스
  * Node
    * 여러가지 DOM 타입들이 상속하는 인터페이스
  * Elment
    * Document안의 모든 객체가 상속하는 가장 범용적인 기반 클래스
    * 부모인 Node와  그 부모인 EventTarget의 속성을 상속
  * Document
    * 브라우저가 불러온 웹 페이즈를 나타냄
    * DOM 트리의 진입점 (entry point)역할을 수행
  * HTMLElement
    * 모든 종류의 HTML 요소
    * 부모인 element의 속성 상속



* DOM 선택 - 선택 관련 메서드
  * Documnet.querySelector()
    * 제공한 선택자와 일치하는 element 하나 선택
    * 제공한 CSS selector를 만족하는 첫번째 element 객체를 반환 (없다면 null)
  * Documnet.querySelectorAll()
    * 제공한 선택자와 일치하는 여러 element를 선택
    * 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    * 지정된 셀렉터에 일치하는 NodeList를 반환
  * id, class 그리고 tag 선택자 등을 모두 사용가능하기 때문에 다른 선택자에 비해서 더 구체적이고 유연하게 선택가능하여 위의 두 명령어를 사용한다.



* DOM 선택 - 선택 메서드별 반환 타입
  * 단일 element
    * getElementById()
    * querySelector()
  * HTMLCollection
    * getElementsByTagName()
    * getElemnetsByClassName()
  * NodeList
    * querySelectorAll()



* HTMLCollection & NodeList
  * 둘다 배열과 같이 각 항목을 접근하기 위한 인덱스를 제공 **(유사배열)**
  * HTMLCollection
    * name, id, 인덱스 속성으로 각 항목들에 접근 가능
  * NodeList
    * 인덱스 번호로만 각 항목들에 접근 간으
    * 단, HTMLCollection과 달리 배열에서 사용하는 for each 함수 및 다양한 메서드 사용가능
  * 둘다 Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만, querySelectorAll()에 의해 반환되는 NodeList는 Static Collection



* Collection
  * Live Collection
    * 문서가 바뀔 때 실시간으로 업데이트
    * DOM의 변경사항을 실시간으로 collection에 반영
    * ex) HTMLCollection, NodeList
  * Static Collection (non-live)
    * DOM이 변경되어도 collection 내용에는 영향을 주지 않음
    * querySelectorAll()의 반환 NodeList만 static



* DOM 변경 - 변경관련 메서드

  * Document.createElement()
    * 주어진 태그명을 사용해 HTML 요소를 만들어 반환
  * ParentNode.append()
    * 특정 부모 노드의 자식 노드 리스트 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입 (반환값 없음)
    * 여러 개의 Node 객체, DOMString을 추가 할 수 있음
  * Node.appendChild()
    * 한 노드를 특정 부모 노드의 자식 노드 리스트 중 마지막 자식으로 삽입(Node만 추가가능)
    * 만약 주어진 노드가 이미 문서에서 존재하는 다른 노드를 참조한다면 새로운 위치로 이동
  * ChildNode.remove()
    * 이를 포함하는 트리로부터 특정 객체를 제거
  * Node.removeChild()
    * DOM에서 자식노드를 제거하고 제거 된 노드를 반환
    * Node는 인자로 들어간느 자식 노드의 부모 노드

  ![image-20210428104506513](javascript_01.assets/image-20210428104506513.png)



* DOM 변경 - 변경 관련 속성 (property)
  * Node.innerText
    * 노드와 그 자손의 텍스트 건텐츠(DOMString)를 표현 (해당 요소 내부의 raw text)
    * 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는등 최종적으로 스타일링이 적용 된 모습을 표현
  * Element.innerHTML
    * 요소(element) 내에 포함 된 HTML 마크업을 반환
    * XSS공격에 취약점이 있으므로 사용시 주의



* XSS (Cross-site scripting)
  * 공격자가 웹 사이트 클라리언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법
  * 이 코드의 실행은 피해자가 하며 공격자가 엑세스 제어를 우회하고 사용자를 가장 할 수 있도록 함



* DOM 변경 - 관련 메서드 (method)
  * Element.setAttribute(name, value)
    * 지정된 요소의 값을 설정
    * 속성이 이미 존재하면 값을 업데이트, 그렇지 않으면 지정된 이름과 값으로 새 속성 추가
  * Element.getAttribute()
    * 해당 요소의 지정된 값(문자열)을 반환
    * 인자는 값을 얻고자 하는 속성의 이름

























