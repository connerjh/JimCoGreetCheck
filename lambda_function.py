import logging
import jimcodb

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# -----------------------------------------------------------------------------

# {
#     "Details": {
#         "ContactData": {
#             "Attributes": {},
#             "Channel": "VOICE",
#             "ContactId": "4a573372-1f28-4e26-b97b-XXXXXXXXXXX",
#             "CustomerEndpoint": {
#                 "Address": "+12108548842",
#                 "Type": "TELEPHONE_NUMBER"
#             },
#             "InitialContactId": "4a573372-1f28-4e26-b97b-XXXXXXXXXXX",
#             "InitiationMethod": "INBOUND | OUTBOUND | TRANSFER | CALLBACK",
#             "InstanceARN": "arn:aws:connect:aws-region:1234567890:instance/c8c0e68d-2200-4265-82c0-XXXXXXXXXX",
#             "PreviousContactId": "4a573372-1f28-4e26-b97b-XXXXXXXXXX",
#             "Queue": "QueueName",
#             "SystemEndpoint": {
#                 "Address": "+1234567890",
#                 "Type": "TELEPHONE_NUMBER"
#             }
#         },
#         "Parameters": {
#             "sentAttributeKey": "sentAttributeValue"
#         }
#     },
#     "Name": "ContactFlowEvent"
# }


def get_messages(individual):

    messages = []

    def sort_key(message):
        return message['Priority']

    for account in individual['Accounts']:
        messages.append(account['Messages'])

    messages = [m for x in messages for m in x]

    return sorted(messages, key=sort_key, reverse=False)


def lambda_handler(event, context):

    logger.info("event: {}".format(event))
    logger.info("context: {}".format(context))

    preferences = jimcodb.get_greet_check_preferences(event['Details']['ContactData']['CustomerEndpoint']['Address'])
    individual = jimcodb.get_individual_by_id(preferences['IndividualId'])

    logger.info('individual: {}'.format(individual))

    messages = get_messages(individual)

    logger.info('Messages: {}'.format(messages))

    if len(messages) > 0:
        return {
            "GreetingType": "Greeting",
            "Greeting": preferences['Greeting'],
            'MessagePriority': messages[0]['Priority'],
            "Message": messages[0]['AccountMessage']
        }

    else:
        return {
            "GreetingType": "Greeting",
            "Greeting": preferences['Greeting'],
            'MessagePriority': 'None',
            "Message":  ''
        }

