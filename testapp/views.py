from django.shortcuts import render
import requests

#
# def token():
#     # Azure AD Application Details
#     client_id = 'd15b5bc6-0b5f-4e80-98af-328a0dc6c143'
#     client_secret = '_Q98Q~p2001gPeIi2prckiapzD8mAlJE7TnU.b8i'
#     tenant_id = '48400f30-5eac-4eb2-8ddf-2ac07c488a4b'  # This is your Azure AD tenant ID
#     scope = 'https://graph.microsoft.com/.default'  # Scope for Microsoft Graph API
#
#     # Azure AD Token Endpoint
#     token_url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
#
#     # Token Request Data
#     token_data = {
#         'grant_type': 'client_credentials',
#         'client_id': client_id,
#         'client_secret': client_secret,
#         'scope': scope,
#     }
#
#     # Make the Token Request
#     token_response = requests.post(token_url, data=token_data)
#
#     # Parse the Token Response
#     if token_response.status_code == 200:
#         # Access Token
#         access_token = token_response.json().get('access_token')
#         print("Access Token:", access_token)
#         return access_token
#
#
#
#     else:
#         print("Token Request Failed. Status Code:", token_response.status_code)
#         print("Error Response:", token_response.text)
#
#
# def get_user():
#     graph_api_url = 'https://graph.microsoft.com/v1.0/me'
#
#     # Define your access token obtained after authenticating your app
#     access_token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IlZDM3I4enQwNzJPbFh4dGUzNFZnclpfME0xaDZheGxuYUlSdll6bVFSREUiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC82MDI3YzliYS0yOTBkLTQxZjAtODFhNi0wMzVmM2EzZDFhNmUvIiwiaWF0IjoxNjk2MjUyMzQ0LCJuYmYiOjE2OTYyNTIzNDQsImV4cCI6MTY5NjMzOTA0NCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhVQUFBQTVSM21LZmVsL2dsZGNZVjFEU3crR09xZnRvKzJWR1N1R1FEZTJnaGpsOW52dDQvWWZKUGhpL0lSdmxIeTJxOHRpYVFVa2pvcER1V0U5RnRLZjFKLzcyM0Z5VVF5NTR3UHIwNnhWdVhxa1BjPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiR2FuZ2FkYXJhIiwiZ2l2ZW5fbmFtZSI6Ik1hbm9qIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMjYwMTo4Nzo1OjM0MDo1ODM5OmYyZTY6Njk5Njo2ZTc1IiwibmFtZSI6Ik1hbm9qIEdhbmdhZGFyYSIsIm9pZCI6IjM2NTkyYWRlLTg1N2UtNDNmNS1hMjkwLWQzODhjZmQ2NDhkNCIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMkFBQzQ4N0MyIiwicmgiOiIwLkFTb0F1c2tuWUEwcDhFR0JwZ05mT2owYWJnTUFBQUFBQUFBQXdBQUFBQUFBQUFBcUFNRS4iLCJzY3AiOiJDaGF0LkNyZWF0ZSBDaGF0LlJlYWQgQ2hhdC5SZWFkV3JpdGUgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgb3BlbmlkIFByZXNlbmNlLlJlYWQgUHJlc2VuY2UuUmVhZC5BbGwgcHJvZmlsZSBTaXRlcy5SZWFkLkFsbCBTaXRlcy5SZWFkV3JpdGUuQWxsIFRhc2tzLlJlYWQgVGVhbS5SZWFkQmFzaWMuQWxsIFRlYW1TZXR0aW5ncy5SZWFkLkFsbCBUZWFtU2V0dGluZ3MuUmVhZFdyaXRlLkFsbCBVc2VyLlJlYWQgVXNlci5SZWFkLkFsbCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6ImNZdzlURVotdm9OQ1g1VmFHXy1JUC1xTXBRNTVKamJYeU1EYU9aazExT1kiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQVMiLCJ0aWQiOiI2MDI3YzliYS0yOTBkLTQxZjAtODFhNi0wMzVmM2EzZDFhNmUiLCJ1bmlxdWVfbmFtZSI6Im1hbm9qLmdhbmdhZGFyYUBzbWFydGltcy5jb20iLCJ1cG4iOiJtYW5vai5nYW5nYWRhcmFAc21hcnRpbXMuY29tIiwidXRpIjoiWXdHLVprTUNHa3VubkltbXRwd2RBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX3NzbSI6IjEiLCJ4bXNfc3QiOnsic3ViIjoiZmt0cUdSYnBYZmxDYkY5aGpQY1cxdVpxUU0xcFRkVVNKUjVqd0JNLXZpZyJ9LCJ4bXNfdGNkdCI6MTQyMjU1MzUzOH0.tHMaM2O8nQs_0bcga64lY_xFp3Sfw4nffx2Fk_r2srMBMJWfiHgTZGg3wkIS5DnOGF0PFWgLqHdIVuOzKQ3hxQqG6k76nWAg6-cU-_xIhNIhQkgOYCy0-DGvUwkugj6R32WASpDUWpje4E5ae_iASNNhyETMK1PWOHeq8POpWP7bRnsOvi6Z71LvvJfGVV9IlSLfN0oKswTJSzyw8veQ7BFa_7x5EFuoHDAmKdfZn5rkRtsB527_5YECFcxXzFFy1OfwCxhAEtceaayfHuVq8rwcHW43ibI57kMAvxXHU-SCY6_MybT9iDgsPBOOtmPJOeOk15IGt_AYywDFuW31_g'
#
#     # Define headers with the access token
#     headers = {
#         'Authorization': f'Bearer {str(access_token)}',
#         'Content-Type': 'application/json'
#     }
#
#     # Make the API request to retrieve users
#     response = requests.get(graph_api_url, headers=headers)
#     contact = {}
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         users_data = response.json()
#         print(users_data)


def get_users(request):
    import requests

    # Define the Microsoft Graph API endpoint
    graph_api_url = 'https://graph.microsoft.com/v1.0/users'
    # graph_api_url1 = 'https://graph.microsoft.com/v1.0/me'
    #
    # Define your access token obtained after authenticating your app
    access_token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IlZDM3I4enQwNzJPbFh4dGUzNFZnclpfME0xaDZheGxuYUlSdll6bVFSREUiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC82MDI3YzliYS0yOTBkLTQxZjAtODFhNi0wMzVmM2EzZDFhNmUvIiwiaWF0IjoxNjk2MjUyMzQ0LCJuYmYiOjE2OTYyNTIzNDQsImV4cCI6MTY5NjMzOTA0NCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhVQUFBQTVSM21LZmVsL2dsZGNZVjFEU3crR09xZnRvKzJWR1N1R1FEZTJnaGpsOW52dDQvWWZKUGhpL0lSdmxIeTJxOHRpYVFVa2pvcER1V0U5RnRLZjFKLzcyM0Z5VVF5NTR3UHIwNnhWdVhxa1BjPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiR2FuZ2FkYXJhIiwiZ2l2ZW5fbmFtZSI6Ik1hbm9qIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMjYwMTo4Nzo1OjM0MDo1ODM5OmYyZTY6Njk5Njo2ZTc1IiwibmFtZSI6Ik1hbm9qIEdhbmdhZGFyYSIsIm9pZCI6IjM2NTkyYWRlLTg1N2UtNDNmNS1hMjkwLWQzODhjZmQ2NDhkNCIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMkFBQzQ4N0MyIiwicmgiOiIwLkFTb0F1c2tuWUEwcDhFR0JwZ05mT2owYWJnTUFBQUFBQUFBQXdBQUFBQUFBQUFBcUFNRS4iLCJzY3AiOiJDaGF0LkNyZWF0ZSBDaGF0LlJlYWQgQ2hhdC5SZWFkV3JpdGUgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgb3BlbmlkIFByZXNlbmNlLlJlYWQgUHJlc2VuY2UuUmVhZC5BbGwgcHJvZmlsZSBTaXRlcy5SZWFkLkFsbCBTaXRlcy5SZWFkV3JpdGUuQWxsIFRhc2tzLlJlYWQgVGVhbS5SZWFkQmFzaWMuQWxsIFRlYW1TZXR0aW5ncy5SZWFkLkFsbCBUZWFtU2V0dGluZ3MuUmVhZFdyaXRlLkFsbCBVc2VyLlJlYWQgVXNlci5SZWFkLkFsbCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6ImNZdzlURVotdm9OQ1g1VmFHXy1JUC1xTXBRNTVKamJYeU1EYU9aazExT1kiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQVMiLCJ0aWQiOiI2MDI3YzliYS0yOTBkLTQxZjAtODFhNi0wMzVmM2EzZDFhNmUiLCJ1bmlxdWVfbmFtZSI6Im1hbm9qLmdhbmdhZGFyYUBzbWFydGltcy5jb20iLCJ1cG4iOiJtYW5vai5nYW5nYWRhcmFAc21hcnRpbXMuY29tIiwidXRpIjoiWXdHLVprTUNHa3VubkltbXRwd2RBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX3NzbSI6IjEiLCJ4bXNfc3QiOnsic3ViIjoiZmt0cUdSYnBYZmxDYkY5aGpQY1cxdVpxUU0xcFRkVVNKUjVqd0JNLXZpZyJ9LCJ4bXNfdGNkdCI6MTQyMjU1MzUzOH0.tHMaM2O8nQs_0bcga64lY_xFp3Sfw4nffx2Fk_r2srMBMJWfiHgTZGg3wkIS5DnOGF0PFWgLqHdIVuOzKQ3hxQqG6k76nWAg6-cU-_xIhNIhQkgOYCy0-DGvUwkugj6R32WASpDUWpje4E5ae_iASNNhyETMK1PWOHeq8POpWP7bRnsOvi6Z71LvvJfGVV9IlSLfN0oKswTJSzyw8veQ7BFa_7x5EFuoHDAmKdfZn5rkRtsB527_5YECFcxXzFFy1OfwCxhAEtceaayfHuVq8rwcHW43ibI57kMAvxXHU-SCY6_MybT9iDgsPBOOtmPJOeOk15IGt_AYywDFuW31_g'

    # Define headers with the access token
    headers = {
        'Authorization': f'Bearer {str(access_token)}',
        'Content-Type': 'application/json'
    }

    # Make the API request to retrieve users
    response = requests.get(graph_api_url, headers=headers)
    contact = {}
    # response1= requests.get(graph_api_url1, headers=headers)
    contact = {}
    # Check if the request was successful (status code 200)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        users_data = response.json().get('value', [])

        graph_api_url = f'https://graph.microsoft.com/v1.0/chats'

        # Define your access token obtained after authenticating your app





        access_token = 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IlZDM3I4enQwNzJPbFh4dGUzNFZnclpfME0xaDZheGxuYUlSdll6bVFSREUiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC82MDI3YzliYS0yOTBkLTQxZjAtODFhNi0wMzVmM2EzZDFhNmUvIiwiaWF0IjoxNjk2MjUyMzQ0LCJuYmYiOjE2OTYyNTIzNDQsImV4cCI6MTY5NjMzOTA0NCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhVQUFBQTVSM21LZmVsL2dsZGNZVjFEU3crR09xZnRvKzJWR1N1R1FEZTJnaGpsOW52dDQvWWZKUGhpL0lSdmxIeTJxOHRpYVFVa2pvcER1V0U5RnRLZjFKLzcyM0Z5VVF5NTR3UHIwNnhWdVhxa1BjPSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiR3JhcGggRXhwbG9yZXIiLCJhcHBpZCI6ImRlOGJjOGI1LWQ5ZjktNDhiMS1hOGFkLWI3NDhkYTcyNTA2NCIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiR2FuZ2FkYXJhIiwiZ2l2ZW5fbmFtZSI6Ik1hbm9qIiwiaWR0eXAiOiJ1c2VyIiwiaXBhZGRyIjoiMjYwMTo4Nzo1OjM0MDo1ODM5OmYyZTY6Njk5Njo2ZTc1IiwibmFtZSI6Ik1hbm9qIEdhbmdhZGFyYSIsIm9pZCI6IjM2NTkyYWRlLTg1N2UtNDNmNS1hMjkwLWQzODhjZmQ2NDhkNCIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMkFBQzQ4N0MyIiwicmgiOiIwLkFTb0F1c2tuWUEwcDhFR0JwZ05mT2owYWJnTUFBQUFBQUFBQXdBQUFBQUFBQUFBcUFNRS4iLCJzY3AiOiJDaGF0LkNyZWF0ZSBDaGF0LlJlYWQgQ2hhdC5SZWFkV3JpdGUgRGlyZWN0b3J5LlJlYWRXcml0ZS5BbGwgb3BlbmlkIFByZXNlbmNlLlJlYWQgUHJlc2VuY2UuUmVhZC5BbGwgcHJvZmlsZSBTaXRlcy5SZWFkLkFsbCBTaXRlcy5SZWFkV3JpdGUuQWxsIFRhc2tzLlJlYWQgVGVhbS5SZWFkQmFzaWMuQWxsIFRlYW1TZXR0aW5ncy5SZWFkLkFsbCBUZWFtU2V0dGluZ3MuUmVhZFdyaXRlLkFsbCBVc2VyLlJlYWQgVXNlci5SZWFkLkFsbCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6ImNZdzlURVotdm9OQ1g1VmFHXy1JUC1xTXBRNTVKamJYeU1EYU9aazExT1kiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQVMiLCJ0aWQiOiI2MDI3YzliYS0yOTBkLTQxZjAtODFhNi0wMzVmM2EzZDFhNmUiLCJ1bmlxdWVfbmFtZSI6Im1hbm9qLmdhbmdhZGFyYUBzbWFydGltcy5jb20iLCJ1cG4iOiJtYW5vai5nYW5nYWRhcmFAc21hcnRpbXMuY29tIiwidXRpIjoiWXdHLVprTUNHa3VubkltbXRwd2RBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19jYyI6WyJDUDEiXSwieG1zX3NzbSI6IjEiLCJ4bXNfc3QiOnsic3ViIjoiZmt0cUdSYnBYZmxDYkY5aGpQY1cxdVpxUU0xcFRkVVNKUjVqd0JNLXZpZyJ9LCJ4bXNfdGNkdCI6MTQyMjU1MzUzOH0.tHMaM2O8nQs_0bcga64lY_xFp3Sfw4nffx2Fk_r2srMBMJWfiHgTZGg3wkIS5DnOGF0PFWgLqHdIVuOzKQ3hxQqG6k76nWAg6-cU-_xIhNIhQkgOYCy0-DGvUwkugj6R32WASpDUWpje4E5ae_iASNNhyETMK1PWOHeq8POpWP7bRnsOvi6Z71LvvJfGVV9IlSLfN0oKswTJSzyw8veQ7BFa_7x5EFuoHDAmKdfZn5rkRtsB527_5YECFcxXzFFy1OfwCxhAEtceaayfHuVq8rwcHW43ibI57kMAvxXHU-SCY6_MybT9iDgsPBOOtmPJOeOk15IGt_AYywDFuW31_g'

        # Define headers with the access token
        headers = {
            'Authorization': f'Bearer {str(access_token)}',
            'Content-Type': 'application/json'
        }
        # for each in users_data:
        #     id = str(each['id'])

        payload = {
            "chatType": "oneOnOne",
            "members": [
                {
                    "@odata.type": "#microsoft.graph.aadUserConversationMember",
                    "roles": [
                        "owner"
                    ],
                    "user@odata.bind": "https://graph.microsoft.com/v1.0/users('36592ade-857e-43f5-a290-d388cfd648d4')"
                },
                {
                    "@odata.type": "#microsoft.graph.aadUserConversationMember",
                    "roles": [
                        "owner"
                    ],
                    "user@odata.bind": f"https://graph.microsoft.com/v1.0/users('499aae88-a407-4334-b19d-489fe8e8b8ac')"
                }
            ]
        }

        # Make the API request to retrieve users
        response = requests.post(graph_api_url, headers=headers, json=payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 201:
            chat_data = response.json()
            print(chat_data)
            # for each in users_data:
            #     users_data.append({'webUrl': chat_data['webUrl']})
            return render(request, 'home.html', {'users': users_data, 'chat_data': chat_data})





        else:
            # Handle the error (e.g., display an error message)
            error_message = response.text
            print(f"Error: {error_message}")
            # Extract employee names from the user data
            return render(request, 'home.html', {'users': users_data})



    else:
        # Handle the error (e.g., display an error message)
        error_message = response.text
        print(f"Error: {error_message}")
    # Pass the list of users to the template
    return render(request, 'home.html')