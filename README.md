## 🍽️ AI_AUTO_CLASSIFY | PLATE & HOME ##

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
<img width="700" alt="로그인" src="https://github.com/user-attachments/assets/d40228f9-d7d8-41c9-8d19-5118091ce998" />
<br>
<br>
<img width="700" alt="회원가입" src="https://github.com/user-attachments/assets/7e9a7df3-7977-481b-ad1d-439b1d69ef5b" />
<br>

### 🛒 장바구니 & 주문
- 상품 담기 / 수량 변경 / 삭제
- 주문 생성 및 주문 내역 조회
- MySQL orders / order_items 테이블 연동
<img width="700" alt="장바구니" src="https://github.com/user-attachments/assets/7ba20410-69cc-4af5-98d5-2b679061f052" />
<br>
<br>
<img width="700" alt="상품구매" src="https://github.com/user-attachments/assets/6a76cc48-9690-4dd1-90c3-c0e925cdb5ea" />

<br>

### 🛠️ 관리자 페이지
- 주문 관리 — 전체 주문 내역 조회 및 상태 관리
- 상품 관리 — 전체 상품 목록 조회 / 수정 / 삭제
- 회원 관리 — 가입 회원 목록 조회
- AI 자동 분류 — 이미지 업로드로 상품 자동 등록
<img width="700" alt="관리자모드" src="https://github.com/user-attachments/assets/3c64389a-102e-4496-96f7-2fdbed77c5e2" />

<br>

### 🤖 AI 자동 분류 시스템 (핵심)
- 이미지 업로드 → GPT-4o-mini Vision 분석
- 상품명 / 카테고리 / 가격 자동 생성
- category.py 검증 후 MySQL products 테이블에 저장
<img width="700" alt="자동화" src="https://github.com/user-attachments/assets/f1333ef0-c1ed-4cd4-82db-8f357282e3e2" />
<br>

### 🔍 상품 검색
- 키워드 입력 시 전체 상품 대상 실시간 필터링
- 검색어 없으면 전체 목록 표시 / 초기화 버튼 제공
<img width="700" alt="검색" src="https://github.com/user-attachments/assets/c105a381-af1b-4ce8-b52f-72f0ca03cf0f" />
<br>

### 💬 AI 챗봇
- rag_docs 기반 문서 학습
- 상품 질문 응답 및 추천 기능
- 전체화면 전환 지원
<img width="700" alt="챗봇_1" src="https://github.com/user-attachments/assets/390cea81-d2a6-40b8-852a-fcd5663e078d" />
<br>
<br>
<img width="700" alt="챗봇 전체화면" src="https://github.com/user-attachments/assets/414306be-ef14-4891-9b13-296722be29f7" />



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

## 📎 프로젝트 SLIDE
<img width="700" alt="슬라이드1" src="https://github.com/user-attachments/assets/07eb01bf-204d-448b-9b1c-81b72d1f1a27" />
<br>
<br>
<img width="700" alt="슬라이드2" src="https://github.com/user-attachments/assets/7d841796-3b2f-40a7-bab6-9088f7e75f6f" />
<br>
<br>
<img width="700" alt="슬라이드3" src="https://github.com/user-attachments/assets/59522d57-4227-4fb7-aac5-80cd58addeda" />
<br>
<br>
<img width="700" alt="슬라이드4" src="https://github.com/user-attachments/assets/54eb990b-ce07-497a-9565-eee30181c0d3" />
<br>
<br>
<img width="700" alt="슬라이드5" src="https://github.com/user-attachments/assets/08c7870e-15de-42f7-9930-5bff08dcde10" />
<br>
<br>
<img width="700" alt="슬라이드6" src="https://github.com/user-attachments/assets/81c2da69-a66d-4f1a-9dea-e148b391b3d2" />
<br>
<br>
<img width="700" alt="슬라이드8" src="https://github.com/user-attachments/assets/f5c898ec-aa91-45e8-9299-8dacfe5e1e05" />
<br>
<br>
<img width="700" alt="슬라이드9" src="https://github.com/user-attachments/assets/0790e221-39e0-4aac-82e9-88eee33a8427" />
<br>
<br>
<img width="700" alt="슬라이드10" src="https://github.com/user-attachments/assets/fe160685-9a1c-47a3-9b3d-8c2c0a9e0c24" />
<br>
<br>
<img width="700" alt="슬라이드11" src="https://github.com/user-attachments/assets/53c869d8-3aba-4c90-b8d9-66ccbe4127e4" />
<br>
<br>
<img width="700" alt="슬라이드12" src="https://github.com/user-attachments/assets/55f923d4-467a-43d7-a304-a1a87137c367" />
<br>
<br>
<img width="700" alt="슬라이드13" src="https://github.com/user-attachments/assets/4b88f123-b4e9-444e-83cb-c557ac6ee23f" />
<br>
<br>
<img width="700" alt="슬라이드14" src="https://github.com/user-attachments/assets/89ec9bea-0b02-4d14-831a-596980e37dd1" />
<br>
<br>
<img width="700" alt="슬라이드15" src="https://github.com/user-attachments/assets/2f6a2287-2c0b-48d0-8fcc-2ec6e81643a9" />
<br>
<br>
<img width="700" alt="슬라이드17" src="https://github.com/user-attachments/assets/d702e4fe-7c19-406d-935a-08ff62f95331" />
<br>
<br>
<img width="700" alt="슬라이드18" src="https://github.com/user-attachments/assets/747442e2-c243-4c65-8a9d-f96ce7b760f5" />
<br>
<br>
<img width="700" alt="슬라이드19" src="https://github.com/user-attachments/assets/dc1a0908-54fa-4b2c-908f-b5e27297ea5a" />
<br>
<br>
<img width="700" alt="슬라이드20" src="https://github.com/user-attachments/assets/844440a5-ee43-45a9-b205-5401f7fd9377" />
<br>
<br>
<img width="700" alt="슬라이드21" src="https://github.com/user-attachments/assets/ec460717-32a4-4ecb-a8f8-87fd494f7505" />
<br>
<br>
<img width="700" alt="슬라이드22" src="https://github.com/user-attachments/assets/16e22dda-6a0d-423d-b5ab-b1feacf21b5f" />
<br>
<br>
<img width="700" alt="슬라이드23" src="https://github.com/user-attachments/assets/86782d94-c85f-46e3-bbcf-7b92e91b991a" />
<br>
<br>
<img width="700" alt="슬라이드24" src="https://github.com/user-attachments/assets/bcf4fb75-ab24-4473-91c7-fc1e038f9b0e" />
<br>
<br>
<img width="700" alt="슬라이드25" src="https://github.com/user-attachments/assets/95aa1741-a1a6-4153-8f9f-7b4a7d18fd66" />
<br>
<br>
<img width="700" alt="슬라이드26" src="https://github.com/user-attachments/assets/a29e5630-9aa4-4382-b779-dc64412348a0" />
<br>
<br>
<img width="700" alt="슬라이드27" src="https://github.com/user-attachments/assets/dd35fa5f-86a9-4cd0-b836-f4db3b22fe3f" />
<br>
<br>
<img width="700" alt="슬라이드28" src="https://github.com/user-attachments/assets/1a5d8bb1-aaf1-4345-8fe9-62150e0d0332" />
<br>
<br>
<img width="700" alt="슬라이드29" src="https://github.com/user-attachments/assets/bb5d7cfe-ae12-4437-a80d-ad7b8a4b24ec" />
<br>
<br>
<img width="700" alt="슬라이드30" src="https://github.com/user-attachments/assets/7fcc310e-448d-4cf8-ad73-98f986287b5b" />
<br>
<br>
<img width="700" alt="슬라이드31" src="https://github.com/user-attachments/assets/3a49c323-a084-4eeb-be05-1fa459afd908" />
<br>
<br>
<img width="700" alt="슬라이드32" src="https://github.com/user-attachments/assets/b09c0cb1-f058-44ec-a28a-cd2200262e81" />
<br>
<br>
<img width="700" alt="슬라이드33" src="https://github.com/user-attachments/assets/ebee9d49-5714-489d-8ebf-6ca38f96741a" />
<br>
<br>
<img width="700" alt="슬라이드34" src="https://github.com/user-attachments/assets/8558f646-ce63-4d8d-aa31-aa66b9f578d2" />
<br>
<br>
