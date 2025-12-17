import json
import pdfplumber
from langchain_openai import ChatOpenAI
from pydantic import BaseModel
import os

class IRO(BaseModel):
    esrs: str
    subtopic: str
    subsubtopic: str
    iro_type: str
    iro_description: str
    source_page: int

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.1)

def extract_csrd_iros(pdf_path, schema_path="config/esrs_schema.json"):
    """EulerESG-inspired: PDF → chunks → schema-guided LLM"""
    with open(schema_path) as f:
        schema = json.load(f)
    
    with pdfplumber.open(pdf_path) as pdf:
        all_iros = []
        for page_num, page in enumerate(pdf.pages, 1):
            text = page.extract_text() or ""
            if any(kw in text.lower() for kw in ["esrs", "iro", "materiality"]):
                prompt = f"""
You are CSRD expert. Extract material IROs per ESRS AR16 from:
{text[:4000]}  # truncated

Schema: {json.dumps(schema)}
Output ONLY valid JSON array matching schema. Verbatim descriptions.
                """
                response = llm.invoke(prompt)
                try:
                    iros = json.loads(response.content)
                    for iro in iros:
                        iro["source_page"] = page_num
                        all_iros.append(iro)
                except:
                    print(f"JSON parse fail page {page_num}")
    return all_iros

# Test
if __name__ == "__main__":
    iros = extract_csrd_iros("data/raw/test_csrd.pdf")
    print(f"Extracted {len(iros)} IROs:", iros[:2])
