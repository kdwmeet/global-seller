# Global Seller Copilot (글로벌 셀러 AI)

## 1. 프로젝트 개요

Global Seller Copilot은 해외 시장 진출을 희망하는 국내 셀러를 위해 개발된 이커머스 리스팅 최적화 솔루션입니다.

단순한 언어 번역을 넘어, 타겟 국가(미국, 일본 등)의 문화적 맥락과 플랫폼별 검색 엔진 최적화(SEO) 알고리즘을 반영하여 '판매 전환율'을 극대화하는 마케팅 문구를 자동으로 생성합니다. OpenAI의 **gpt-5-mini** 모델을 활용하여 아마존(Amazon)의 키워드 중심 알고리즘과 라쿠텐(Rakuten)의 신뢰 중심 알고리즘에 각각 최적화된 전략적 콘텐츠를 제공합니다.

### 주요 기능
* **플랫폼별 맞춤 전략:** 미국 아마존(혜택 중심, SEO 키워드)과 일본 라쿠텐(상세한 스펙, 정중한 어조) 등 마켓 특성에 따른 차별화된 리스팅 생성.
* **다국어 마케팅 카피라이팅:** 한국어 상품 정보를 입력하면, 현지 원어민 마케터 수준의 자연스러운 영어 및 일본어 상세 페이지 문구 작성.
* **SEO 키워드 추출:** 각 국가의 소비자가 실제로 검색하는 롱테일 키워드(Long-tail Keywords)를 분석하여 제목과 태그에 반영.
* **구조화된 데이터 출력:** 상품명, 불릿 포인트(Bullet Points), 상세 설명, 검색어 태그를 JSON 형식으로 반환하여 즉시 업로드 가능.

## 2. 시스템 아키텍처

본 시스템은 사용자 입력을 바탕으로 국가별 페르소나를 호출하고, LLM을 통해 최적화된 콘텐츠를 생성하는 파이프라인으로 구성됩니다.

1.  **Target Selection:** 사용자가 진출하고자 하는 타겟 마켓(미국/일본)을 선택.
2.  **Prompt Engineering:** 선택된 마켓에 따라 사전에 정의된 '시스템 프롬프트(System Prompt)'를 로드.
    * *Amazon US:* Top Seller 페르소나, 강한 어조, 혜택 강조.
    * *Rakuten JP:* 신뢰할 수 있는 판매자 페르소나, 정중한 어조, 안전성 강조.
3.  **AI Inference:** **gpt-5-mini** 모델이 한국어 입력을 분석하고, 타겟 언어와 문화에 맞춰 재창작(Transcreation) 수행.
4.  **Response Formatting:** 생성된 텍스트를 JSON 구조로 파싱하여 UI에 렌더링.

## 3. 기술 스택

* **Language:** Python 3.10 이상
* **AI Model:** OpenAI **gpt-5-mini**
* **Web Framework:** Streamlit
* **Configuration:** python-dotenv

## 4. 프로젝트 구조

국가별 프롬프트 전략과 비즈니스 로직을 분리하여 확장성을 고려한 모듈형 구조입니다.

```text
global-seller/
├── .env                  # 환경 변수 (API Key)
├── requirements.txt      # 의존성 패키지 목록
├── main.py               # 애플리케이션 진입점 및 대시보드 UI
└── app/                  # 백엔드 핵심 모듈
    ├── __init__.py
    ├── config.py         # 국가별(미국/일본) 시스템 프롬프트 및 JSON 스키마 정의
    └── generator.py      # OpenAI API 통신 및 다국어 생성 로직
```
## 5. 설치 및 실행 가이드
### 5.1. 사전 준비
Python 환경이 설치되어 있어야 합니다. 터미널에서 저장소를 복제하고 프로젝트 디렉토리로 이동하십시오.

```Bash
git clone [레포지토리 주소]
cd global-seller
```
### 5.2. 의존성 설치
필요한 라이브러리를 설치합니다.

```Bash
pip install -r requirements.txt
```
### 5.3. 환경 변수 설정
프로젝트 루트 경로에 .env 파일을 생성하고, 유효한 OpenAI API 키를 입력하십시오.

```Ini, TOML
OPENAI_API_KEY=sk-your-api-key-here
```
### 5.4. 실행
Streamlit 애플리케이션을 실행합니다.

```Bash
streamlit run main.py
```
## 6. 출력 데이터 사양 (JSON Schema)
AI 모델은 플랫폼 업로드에 최적화된 다음과 같은 JSON 구조로 데이터를 반환합니다.

```JSON
{
  "title": "Premium Roasted Seaweed Snacks (20 Packs) - Olive Oil Glazed, Low Sodium, Keto & Vegan Friendly",
  "bullets": [
    "HEALTHY & GUILT-FREE: Low calorie, no MSG, vegan certified.",
    "PERFECT CRUNCH: Roasted twice for the ultimate crispiness.",
    "GREAT FOR LUNCHBOXES: Conveniently limits portion size."
  ],
  "description": "<p>Experience the authentic taste of Korea...</p>",
  "keywords": "seaweed snacks, nori sheets, healthy vegan snacks, keto food, korean bbq"
}
```

## 7. 실행 화면
<img width="1268" height="658" alt="스크린샷 2026-02-09 051343" src="https://github.com/user-attachments/assets/ff228f64-3ca7-4671-96d7-6918340f3831" />
