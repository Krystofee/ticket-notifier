import requests

TEST_ENABLED = False

NIMROD_URL = 'https://www.nimrod-messenger.io/api/v1/message'
NIMROD_API_KEYS = ['71c906ad-8e09-4a7e-aca9-7983cb2eabfe', '8fa62c01-1f57-4afe-a584-4e637cc6d910']
RESULT_MESSAGE = "Don't worry, I'm still running :)"


for key in NIMROD_API_KEYS:
    requests.post(
        NIMROD_URL,
        data={
            'api_key': key,
            'message': RESULT_MESSAGE
        }
    )
