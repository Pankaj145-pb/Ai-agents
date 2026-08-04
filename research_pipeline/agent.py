from google.adk.agents import LlmAgent, SequentialAgent


# Step 1 Resarch agent on a topic

researcher = LlmAgent(
    model="gemini-2.5-flash",
    name="researcher",
    output_key="research_findings",
    instruction="""
Research the given topic throughly.

Provide 
- 3-5 key facts
- Important statistic or data
- Current Trends or develepoment

Be factual and informative
"""
)

# Step 2 Writer reads research and create article
writer = LlmAgent(
    model="gemini-2.5-flash",
    name="writer",
    output_key="draft_article",
    instruction=""" 
Write a short article based on research:

{research_findings}

Structure
- Engaging Introduction
- Key Findings (2-3 paragraphs)
- Brief conclusion

Keepi it under 300 words
"""
)

# Step 3: Editor reads article and polishes

editor = LlmAgent(

 model='gemini-2.5-flash',

 name='editor',

 instruction='''

 Edit and polish this article:


 {draft_article}


 Fix any grammar issues, improve flow, and ensure clarity.

 Return the final polished version.

 '''

)

root_agent = SequentialAgent(
    name='article_pipeline',
    sub_agents=[researcher, writer, editor]
)
