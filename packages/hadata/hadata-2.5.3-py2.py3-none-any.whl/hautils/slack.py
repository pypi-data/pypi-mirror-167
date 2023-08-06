from slack_sdk.webhook import WebhookClient


def slack_notify(message):
    url = "https://hooks.slack.com/services/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"
    webhook = WebhookClient(url)
    response = webhook.send(text=message)
    assert response.status_code == 200
    assert response.body == "ok"
