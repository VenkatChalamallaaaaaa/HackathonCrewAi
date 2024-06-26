#                             Event Planning Crew 
#In this Crew we are trying to plan a schedule plan for students. Consits of 3 agents
# 1. city_selection_agent:
# -This agent helps in selecting the destination city or cities for the trip based on user preferences and available options.

# 2. local_expert_agent:
# -The local_expert_agent acts as a guide or advisor, providing insights and recommendations about the selected destination(s). 
# -It offers information on local attractions, activities, dining options, and other relevant details to enhance the travel experience.

# 3. travel_concierge_agent:
# -This agent functions as a travel concierge, assisting with various aspects of trip planning and coordination. 
# -It may help with booking accommodations, arranging transportation, scheduling activities, and managing other travel-related tasks to ensure a smooth and enjoyable journey.


# First, we'll initialize our TripPlannerAgents.
agents = TripPlannerAgents()
city_selector_agent = agents.city_selection_agent()
local_expert_agent = agents.local_expert()
travel_concierge_agent = agents.travel_concierge()

# Now, we'll define the tasks needed for our trip.
tasks = TripTasks()
identify_task = tasks.identify_task(city_selector_agent, origin, cities, interests, date_range)

gather_task = tasks.gather_task(city_selector_agent, origin, interests, date_range)

plan_task = tasks.plan_task(city_selector_agent, origin, interests, date_range)

# Create a crew and kick off the planning process!
crew = Crew(
    agents=[city_selector_agent, local_expert_agent, travel_concierge_agent],
    tasks=[identify_task, gather_task, plan_task]
)
