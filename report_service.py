from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()

gpt_key = os.getenv("OPENAI_API_KEY")
print(f"GPT key is {"OPENAI_API_KEY" in os.environ}")

llm = ChatOpenAI(model="gpt-5-2025-08-07")


def investment_report(symbol, company, stock):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system", """
                    Want assistance provided by qualified individuals enabled with experience on understanding charts 
                    using technical analysis tools while interpreting macroeconomic environment prevailing across world 
                    consequently assisting customers acquire long term advantages requires clear verdicts 
                    therefore seeking same through informed predictions written down precisely!
                    """
            ),
            (
                "user", """
                    {company}에 주식을 투자하려고 합니다. 아래의 기본정보, 재무재표를 참고하여 마크다운 형식의 투자 보고서를 한글로 작성 할 것.
                    다만, 2025년 8월 22일 현재 기준, 전세계 경제 흐름을 참고하고 전 세계적으로 성공한 투자자의 방식을 근거로 할 것,
                    모든 답변을 도출 해 내는 과정에서는 단계적으로 도출 해내고, 출력 전에 다시 한 번 점검하여 거짓이 있는지 확인 할 것,
                    모든 단계에서 근거를 가지고 판단 할 것

                    - 기본정보 :
                    {business_info}
                    
                    - 재무재표
                    {financial_stat}
                """
            )
        ]
    )
    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser
    res = chain.invoke(
        {
            'company': company,
            'business_info': stock.get_basic_info(),
            "financial_stat": stock.get_financial_stat(),
            'symbol': symbol,
        }
    )
    return res