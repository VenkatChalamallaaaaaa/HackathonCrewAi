from crewai import Crew
from agents import TripPlannerAgents
from tasks import TripTasks

date_range = 'June-Sep 24'
origin = 'Berlin'
interests = 'Studying and food'
cities = 'Chennai'

result = crew.kickoff()
print(result)