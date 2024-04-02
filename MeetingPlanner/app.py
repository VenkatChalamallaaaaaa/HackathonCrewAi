

OpenAI_API_KEY = ''
os.environ["OPENAI_API_KEY"] = OpenAI_API_KEY


tasks = MeetingPreparationTasks()
agents = MeetingPreparationAgents()




print("## Welcome to Student Meeting Scheduler")
print("------------------------------------")

participants = input("What are the emails for the participants (other than you) in the meeting?\n")

emails_array = participants.split(',')

# all the emails
emails_array = [email.strip() for email in emails_array]

##context
context = input("What is the context of the meeting?\n")

#objective
objective = input("What is your objective for this meeting?\n")


print(f"participants: {participants} | context: {context} | objective: {objective}")


game = crew.kickoff()

print("## Here is the result ##")
print(game)