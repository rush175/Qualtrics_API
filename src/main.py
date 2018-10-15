import os
import json
from qualtrics import Qualtrics


# CA
# apiToken = os.environ["Q_API_TOKEN"]     
# dataCenter = os.environ["Q_DATA_CENTER"] 
# library = os.environ["Q_LIBRARY"] 

# CO
apiToken = os.environ["Q_API_TOKEN_1"]     
dataCenter = os.environ["Q_DATA_CENTER_1"]
# library = os.environ["Q_LIBRARY_1"] 


# apiToken = "test"
# dataCenter = "test"

qualtrics = Qualtrics(apiToken, dataCenter)


qualtrics.download_responses(surveyId="SV_cC8qHYlPlC0koZL", format="csv", lastResponseId="R_1o5b6zC3jCk0WD0", useLabels=True, limit=3)

# qualtrics.retake_response("SV_429KwiiOkFTCucR", "R_8Dls5pWKJcAuPfT", delete=False)

# qualtrics.retake_response("SV_b2QprbVgmMwO2fr", "R_cu0qZTqV5zMkYnv")

# qualtrics.retake_unfinished_responses("SV_bEJ7SqCPmZq83wF")


# qualtrics.list_directorry_contacts()
# qualtrics.get_partials()

# qualtrics.list_groups()

# qualtrics.get_group("GR_1ELD578yYpROTlj")

# qualtrics.get_all_surveys()

# Get JSON of survey
# print (json.dumps(qualtrics.get_survey("SV_b3eYEKqCcIHwbhX"), indent=4))

# Get all surveyIds from projects page
# print (qualtrics.get_all_surveys())


#Download all responses for single survey
# result = qualtrics.download_responses("SV_b2QprbVgmMwO2fr", format_type="json", download=False)
# result = qualtrics.download_responses_new("SV_cC8qHYlPlC0koZL", download=False)
# print (json.dumps(result, indent=4))


# Download all repsonses for all surveys in project page
# qualtrics.download_all_responses()


# Try to download shared project
# qualtrics.download_responses_new("SV_eLPcHbH0EAg3yrX")
# print (json.dumps(qualtrics.get_survey("SV_5aufmvWxteSDxJz"), indent=4))


# Create new survey session
# session = qualtrics.create_sesssion("SV_eDwgadvLh4MLhf7")
# print (json.dumps(session, indent=4))
# sessionId = session['result']['sessionId']


# Update an existing session
# sessionId = "FS_Q51Cum30LK1z85j"
# session_update_response = qualtrics.update_session("FS_8crClCLWYZNwBKV","SV_eDwgadvLh4MLhf7")
# print (json.dumps(session_update_response, indent=4))


# Get an exisitng session
# sessionId = "FS_Q51Cum30LK1z85j"
# session_get_response = qualtrics.get_session("FS_Q51Cum30LK1z85j","SV_eDwgadvLh4MLhf7")
# print (json.dumps(session_get_response, indent=4))



# Close an existing session
# sessionId = "FS_8crClCLWYZNwBKV"
# session_close_response = qualtrics.close_session("FS_8crClCLWYZNwBKV","SV_eDwgadvLh4MLhf7")
# print (json.dumps(session_close_response, indent=4))


# Create new completedResponse event to ping server on completed responses
# status = qualtrics.create_completedResponse_event("SV_b3eYEKqCcIHwbhX", "http://f4b63c7c.ngrok.io")
# print (status)

# Update Response
# update_response = qualtrics.update_response("SV_0jFSMFGDOcSzZB3", "R_1gzrJOwkdmiPVG6", '{"Round": 100, "NewRound": 200}')
# print (update_response)


# Delete Response
# delete_response = qualtrics.delete_response("SV_0jFSMFGDOcSzZB3", "R_27VecyogvdbtZtQ", True)
# print (delete_response)


# Delete All Responses
# errors = qualtrics.delete_all_responses("")
# print (errors)







