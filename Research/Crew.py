#                    The Researching and Writing Crew

# We will Now talk about the Researching and Writting Crew. This crew ass 4 agents 
# - Research agent - researchs online and browses information and retreives it to writer agent
# - Writer agents formats and the information and organizes the and filters out the nessassary information 


#Google Scholar Agents is being used 
# -help researchers find and manage scholarly articles more efficiently
# -searching, analyzing, and organizing academic literature 

#File Writer Agent is also being used
# -This agent is responsible for writing data or information to files
#- facilitating data storage and management operations


writer = Agents.writer_agent()
reasearcher = Agents.researcher_agent()

def crew_combine():
  # Here we're defining a method called crew_combine. 
  
  return Crew(
      # We're returning a Crew object with some attributes.
      
      agents=[researcher, writer],
      # We have some agents, like researchers and writers
      
      tasks=[research_task, write_task],
      # And we've got tasks lined up for them, like research_task and write_task. 
  
      process=Process.sequential
      # And we'll tackle these tasks one after the other, in a sequential process.
  )
