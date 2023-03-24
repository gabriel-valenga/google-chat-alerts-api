from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build

# Specify required scopes.
SCOPES = ['https://www.googleapis.com/auth/chat.bot']

# Specify service account details.
CREDENTIALS = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account.json', SCOPES)

# Build the URI and authenticate with the service account.
chat = build('chat', 'v1', http=CREDENTIALS.authorize(Http()))

# Create a Chat message.
result = chat.spaces().messages().create(

    # The space to create the message in.
    #
    # REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD replies to an existing thread
    # if one exists, otherwise it starts a new one.
    #
    # Replace SPACE with a space name.
    # Obtain the space name from the spaces resource of Chat API,
    # or from a space's URL.
    parent='spaces/SPACE',

    # Whether to start a thread or reply to an existing one.
    #
    # Required when threading is enabled in a space unless starting a
    # thread.  Ignored in other space types. Threading is enabled when
    # space.spaceThreadingState is THREADED_MESSAGES.
    messageReplyOption='REPLY_MESSAGE_FALLBACK_TO_NEW_THREAD',

    # The message body.
    body={

        # The message to create.
        'text': 'Start or reply to another message in a thread!',

        # The thread to start or reply to.
        'thread': {
            'threadKey': 'nameOfThread'
        }
    }

).execute()

print(result)