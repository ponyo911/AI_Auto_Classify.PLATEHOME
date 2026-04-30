# category.py
# GPT Vision 분석 결과 → 쇼핑몰 카테고리 데이터로 변환 및 검증

# 유효한 카테고리 목록 및 한글 표시명
CATEGORY_MAP = {
    "featured": {
        "label": "featured",
        "display": "Best Items",
        "description": "플레이트앤홈이 추천하는 베스트 상품입니다.",
        "badge": "BEST"
    },
    "new": {
        "label": "new",
        "display": "New",
        "description": "새롭게 선보이는 신상품입니다.",
        "badge": "NEW"
    },
    "collection": {
        "label": "collection",
        "display": "Collection",
        "description": "특별 컬렉션 상품입니다.",
        "badge": "NEW"
    },
    "mug": {
        "label": "mug",
        "display": "Mug",
        "description": "매일 손이 가는 머그 상품입니다.",
        "badge": "NEW"
    },
    "plate": {
        "label": "plate",
        "display": "Plate",
        "description": "음식을 깔끔하게 담아내는 접시입니다.",
        "badge": "NEW"
    },
    "tableware": {
        "label": "tableware",
        "display": "Tableware",
        "description": "식탁 구성을 완성하는 테이블웨어입니다.",
        "badge": "NEW"
    },
}

# GPT가 반환한 카테고리 값 정규화 (소문자 + 공백 제거)
def normalize_category(gpt_category: str) -> str:
    if not gpt_category:
        return "featured"
    return str(gpt_category).strip().lower()

# 카테고리 정보 반환 — 유효하지 않으면 featured로 대체
def get_category_info(gpt_category: str) -> dict:
    label = normalize_category(gpt_category)
    return CATEGORY_MAP.get(label, CATEGORY_MAP["featured"])

# GPT 분석 결과 전체 검증 및 보정
def validate_gpt_result(result: dict) -> dict:
    category_info = get_category_info(result.get("category", ""))

    return {
        "name": result.get("name", "신규 상품"),
        "category": category_info["label"],
        "display_category": category_info["display"],
        "price": max(int(result.get("price", 0)), 0),
        "description": result.get("description", category_info["description"]),
        "badge": category_info["badge"],
    }