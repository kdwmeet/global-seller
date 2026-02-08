from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from app.config import MODEL_NAME, MARKET_PROMPTS, OUTPUT_FORMAT

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_listing(product_name, features, market):
    """상품 정보를 받아 해당 국가 쇼핑몰용 리스팅 JSON 생성"""
    
    # 마켓에 맞는 프롬프트 가져오기
    system_prompt = MARKET_PROMPTS.get(market, MARKET_PROMPTS["Amazon US (미국) 🇺🇸"])

    # 사용자 입력 구성
    user_content = f"""
    [상품 정보 (한국어)]
    - 상품명: {product_name}
    - 주요 특징 및 장점: {features}
    
    위 정보를 바탕으로 {market} 시장에 맞는 판매글을 작성해줘.
    {OUTPUT_FORMAT}
    """

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ],
            reasoning_effort="medium",
            response_format={"type": "json_object"}
        )

        result_json = json.loads(response.choices[0].message.content)
        return result_json
    
    except Exception as e:
        return {"error": f"생성 중 오류 발생: {str(e)}"}