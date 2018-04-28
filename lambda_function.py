import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# -----------------------------------------------------------------------------


def lambda_handler(event, context):

    logger.info("event: {}".format(event))
    logger.info("context: {}".format(context))

    return {
        "Name": "CustomerName",
        "Address": "1234 Main Road",
        "CallerType": "Patient"
    }
