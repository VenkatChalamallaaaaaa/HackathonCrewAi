class tasks():
  def researhder_tasks1():
     return Task(
       
        description=f"""
            Identify the next big trend in {topic}.
            Focus on identifying pros and cons and the overall narrative.

            Your final report should clearly articulate the key points, 
            its market opportunities, and potential risks.
        """,

        expected_output=" A 3 paragraphs long report on the latest AI trends.", 

        max_iter=1, 

        tools=[search_tool], 
        
        agent=researcher
    )
  

  def researcher_tasks2():
    return Task(
        description=f"""
            Compose an insightful article on {topic}.
            Focus on the latest trends and how it's impacting the industry.
            This article should be easy to understand, engaging and positive.
        """,
        expected_output=f"A 5 paragraph article on {topic} advancements", 
        tools=[search_tool],
        agent=writer
    )