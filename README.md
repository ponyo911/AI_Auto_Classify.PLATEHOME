# 🍽️ AI_AUTO_CLASSIFY | PLATE & HOME

> 풀스택 쇼핑몰 프로젝트 | FastAPI + MySQL + OpenAI RAG +  AI 챗봇 + AI 상품 분류 및 매칭 시스템

<br>

## 🔗 링크

| 구분 | URL |
|---|---|
| GitHub Pages (화면 확인) | https://ponyo911.github.io/Plate-Home/ |
| GitHub Repository | https://github.com/ponyo911/AI_Auto_Classify.PLATEHOME |

> ※ GitHub Pages는 정적 호스팅 환경으로 화면 구성 확인 용도입니다.
> 로그인 · 장바구니 · AI 챗봇 등 백엔드 연동 기능은 로컬 실행 환경에서 동작합니다.

<br>

---

## 📌 프로젝트 개요

HTML/CSS/Vanilla JS로 제작한 테이블웨어 쇼핑몰에 FastAPI 백엔드 + MySQL DB를 연동한 풀스택 프로젝트입니다.
GPT-4o-mini Vision을 활용한 **AI 자동 상품 분류 시스템**과 RAG 기반 **AI 챗봇**을 핵심 기능으로 포함합니다.

<br>

---

## 🛠️ 기술 스택

| 구분 | 기술 | 역할 |
|---|---|---|
| Frontend | HTML / CSS / JavaScript | 화면 구성 및 사용자 인터페이스 |
| Backend | Python / FastAPI | REST API 서버, 비즈니스 로직 |
| Database | MySQL (pymysql) | 회원 / 장바구니 / 주문 / 상품 데이터 |
| AI 분류 | OpenAI GPT-4o-mini Vision | 이미지 분석 후 상품명 / 카테고리 / 가격 자동 분류 |
| AI 챗봇 | OpenAI GPT-4o-mini + RAG | 문서 기반 상품 추천 및 고객 상담 |
| 인증 | bcrypt + localStorage | 비밀번호 암호화, 로그인 상태 유지 |
| 환경 변수 | .env + python-dotenv | DB 정보, API 키 보호 |

<br>

---

## 📁 프로젝트 구조

```
auto-classify-plate-home/
├── main.py              # FastAPI 서버 (API 엔드포인트 전체)
├── database.py          # MySQL DB 연결
├── models.py            # Pydantic 데이터 모델
├── category.py          # AI 분류 카테고리 검증 로직
├── .env                 # 환경변수 (비공개 - .gitignore 처리)
├── requirements.txt     # 의존성 패키지
│
├── css/                 # 스타일시트
├── js/
│   ├── app.js           # 상품 렌더링 및 메인 페이지 로직
│   └── header.js        # 공통 헤더 (로그인 상태 반응형)
│
├── json/
│   └── data.json        # 배너 데이터 (상품은 DB로 이전됨)
│
├── rag_docs/            # AI 챗봇 학습 문서
├── img/                 # 상품 이미지
│
├── index.html           # 메인 페이지
├── sub.html             # 상품 상세 페이지
├── cart.html            # 장바구니
├── order_list.html      # 주문 내역
├── login.html           # 로그인 / 회원가입
├── admin.html           # 관리자 페이지
└── chatbot.html         # AI 챗봇
```

<br>

---

## ✨ 주요 기능


### 👤 회원 시스템
- 회원가입 (bcrypt 비밀번호 암호화)
- 로그인 / 로그아웃 (localStorage 상태 유지)
- 비회원 접근 시 장바구니 → 로그인 페이지 강제 이동

### 🛒 장바구니 & 주문
- 상품 담기 / 수량 변경 / 삭제
- 주문 생성 및 주문 내역 조회
- MySQL orders / order_items 테이블 연동

### 🤖 AI 자동 분류 시스템 (핵심)
- 이미지 업로드 → GPT-4o-mini Vision 분석
- 상품명 / 카테고리 / 가격 자동 생성
- category.py 검증 후 MySQL products 테이블에 저장
- 등록된 상품이 메인 페이지 해당 섹션에 자동 반영

### 🔍 상품 검색
- 키워드 입력 시 전체 상품 대상 실시간 필터링
- 검색어 없으면 전체 목록 표시 / 초기화 버튼 제공

### 🛠️ 관리자 페이지
- 주문 관리 — 전체 주문 내역 조회 및 상태 관리
- 상품 관리 — 전체 상품 목록 조회 / 수정 / 삭제
- 회원 관리 — 가입 회원 목록 조회
- AI 자동 분류 — 이미지 업로드로 상품 자동 등록

### 💬 AI 챗봇
- rag_docs 기반 문서 학습
- 상품 질문 응답 및 추천 기능
- 전체화면 전환 지원

<br>

---

## 🗄️ DB 구조

```sql
-- 회원
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255),
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 장바구니
CREATE TABLE cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    product_id VARCHAR(100),
    product_name VARCHAR(200),
    price INT,
    quantity INT DEFAULT 1
);

-- 주문
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50),
    total_price INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 주문 상세
CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_name VARCHAR(200),
    price INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(id)
);

-- 상품 (AI 자동 분류로 등록)
CREATE TABLE products (
    id VARCHAR(100) PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    price INT NOT NULL DEFAULT 0,
    category VARCHAR(50) NOT NULL,
    image VARCHAR(200),
    description TEXT,
    badge VARCHAR(50),
    registered_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

<br>

---

## 🔌 API 엔드포인트

| Method | Endpoint | 설명 |
|---|---|---|
| POST | `/api/signup` | 회원가입 |
| POST | `/api/login` | 로그인 |
| GET | `/api/products` | 전체 상품 목록 조회 |
| GET | `/api/products/search` | 상품 검색 |
| POST | `/api/products` | AI 자동 상품 등록 |
| PUT | `/api/products/{id}` | 상품 수정 |
| DELETE | `/api/products/{id}` | 상품 삭제 |
| GET | `/api/cart/{user_id}` | 장바구니 조회 |
| POST | `/api/cart` | 장바구니 담기 |
| DELETE | `/api/cart/{id}` | 장바구니 삭제 |
| POST | `/api/orders` | 주문 생성 |
| GET | `/api/orders/{user_id}` | 주문 내역 조회 |
| GET | `/api/admin/orders` | 관리자 전체 주문 조회 |
| GET | `/api/admin/users` | 관리자 회원 목록 조회 |
| POST | `/api/chat` | AI 챗봇 응답 |

<br>

---

## 🚀 로컬 실행 방법

```bash
# 1. 저장소 클론
git clone https://github.com/ponyo911/auto-classify-plate-home.git
cd auto-classify-plate-home

# 2. 가상환경 생성 및 활성화
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Mac/Linux

# 3. 패키지 설치
pip install -r requirements.txt

# 4. .env 파일 생성 후 아래 내용 입력
OPENAI_API_KEY=your_openai_api_key
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_db_password
DB_NAME=plate_home_db

# 5. MySQL에서 DB 생성
CREATE DATABASE plate_home_db;
# 위의 DB 구조 SQL 실행

# 6. 서버 실행
uvicorn main:app --reload

# 7. 브라우저에서 접속
# http://127.0.0.1:8000
```

<br>

---

## 📊 시스템 아키텍처

```
[Browser - Vanilla JS]
        │  fetch()
        ▼
[FastAPI Server - main.py]
  ├── 인증 라우터 (bcrypt)
  ├── 상품 라우터 (MySQL products)
  ├── 장바구니 / 주문 라우터
  ├── AI 분류 (GPT-4o-mini Vision)
  └── AI 챗봇 (GPT-4o-mini + RAG)
        │
        ▼
[MySQL DB]                    [OpenAI API]
  ├── users                     ├── Vision 분석
  ├── cart                      └── RAG 챗봇
  ├── orders
  ├── order_items
  └── products (AI 등록)
```

<br>

---

## 📎 발표 자료

> PPT 슬라이드 이미지는 아래와 같이 추가하세요.

```markdown
![slide1](slides/slide_01.png)
![slide2](slides/slide_02.png)
...
```

또는 PDF 파일을 레포에 포함 후 링크 연결:

```markdown
[📄 프로젝트 발표 자료 (PDF)](PLATE_HOME.pdf)
```

<br>

---

## 🎥 기능 시연

> GIF 파일 준비 후 아래 형식으로 교체하세요.

| 기능 | 시연 |
|---|---|
| AI 자동 상품 분류 | ![ai-classify](gif/ai_classify.gif) |
| 장바구니 & 주문 | ![cart](gif/cart_order.gif) |
| AI 챗봇 | ![chatbot](gif/chatbot.gif) |
| 관리자 페이지 | ![admin](gif/admin.gif) |

<br>

---

## 👨‍💻 개발자

| 이름 | GitHub |
|---|---|
| ponyo911 | https://github.com/ponyo911 |