import lambda_function
import jimcodb

event1 = {'Details':
              {'ContactData':
                   {
                        'Attributes': {},
                        'Channel': 'VOICE',
                        'ContactId': 'a33663f2-215b-40de-a969-f38c1c3eb84b',
                        'CustomerEndpoint': {'Address': '+12108548842', 'Type': 'TELEPHONE_NUMBER'},
                        'InitialContactId': 'a33663f2-215b-40de-a969-f38c1c3eb84b',
                        'InitiationMethod': 'INBOUND',
                        'InstanceARN': 'arn:aws:connect:us-east-1:832433821903:instance/148d3298-163b-4d8e-807b-b9b78b1a31ee',
                        'PreviousContactId': 'a33663f2-215b-40de-a969-f38c1c3eb84b',
                        'Queue': None,
                        'SystemEndpoint': {'Address': '+12066078565', 'Type': 'TELEPHONE_NUMBER'}
                    },
               'Parameters': {}
               },
          'Name': 'ContactFlowEvent'}

context = None

# print(jimcodb.get_account_messages(12345))

print(lambda_function.lambda_handler(event1, context))

