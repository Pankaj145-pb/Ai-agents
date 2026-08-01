from google.adk.agents.llm_agent import Agent
from google.genai import types
from google.adk.agents import LlmAgent

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='data_extractor',
    description='Extract factual information with high consistency',
    instruction=""" You are a precise data extractor', 
    Extract fact exactly as stated. Do not:
    - Add information not present in the input
    - Make assumptions or inference
    - Use Creative language
    Be accurate concise, and deterministic """,

    generate_content_config= types.GenerateContentConfig(
        temperature=0.1,
        max_output_tokens=500,
        top_p=0.8,
        top_k=10,
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE
            )
        ]
    )

)

#Agent 2

creative_agent = LlmAgent(
    model="gemini-2.5-flash",
    name="creative_brainstomer",
    description="Generates creative ideas and explore possiblities",
    instruction="""You are a creative brainstorming partner.


Generate innovative, diverse, and imaginative ideas. Feel free to:

- Think outside the box

- Combine unexpected concepts

- Explore unconventional approaches


Be creative, varied, and thought-provoking.""",

generate_content_config=types.GenerateContentConfig(

        temperature=0.9,  # High for creativity

        max_output_tokens=2000,  # Allow detailed ideas

        top_p=0.95,

        top_k=40,

        safety_settings=[

            types.SafetySetting(

                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,

                threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE

            )

        ]

    )

)

