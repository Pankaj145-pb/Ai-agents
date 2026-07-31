"""
Product Extractor agent with structured JSON output

"""
from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

class ProductInfo(BaseModel):
    product_name: str = Field(description="The Full name of the product")
    price: str = Field(description="The Price of the product")
    storage: str = Field(description="Storage Capacity")
    color: str = Field(default="Not Specified", description="Product color if mentioned")

"""
Step 2
Create Agent with output schema
"""
root_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="Product_Extractor",
    description="Extract product information from user message and give structured JSON",
    instruction="""You are a product information extractor
    
    Your task:
    - Read the user's message about a product
    - Extract: product_name, price, storage, and color (if mentioned)
    - Respond ONLY with valid JSON matching this format:

    {
    "product_name": "One Plus 11",
    "price": 999.99,
    "storage": "256GB",
    "color": "Space Black"
    }


Rules:
- price must be a number (no dollar signs)
- storage must include unit (GB, TB)
- If color not mentioned, use "Not specified"
- Output ONLY the JSON, no explanation text""",

    output_schema=ProductInfo,  # Enforce this exact structure
    output_key="extracted_product"  # Store result in session state
)