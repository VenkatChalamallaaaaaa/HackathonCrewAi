class ReserachAgents():
    def researh_agent():
       return Agent(
            role='Senior Student Researcher', 
            goal=f"Uncover groundbreaking technologies around {topic}",
            backstory="Driven by curiosity, you're at the forefront of innovation",
            verbose=True,
            llm=llm
        )
    
    def writer_agent():
        return Agents(
            role="Writer", 
            goal=f"Narrate compelling tech stories about {topic}",
            backstory="With a flair for simplifying complex topics, you craft engaging narratives.",
            verbose=True,
            llm=llm
        )

 