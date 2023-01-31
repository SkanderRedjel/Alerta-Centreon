from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase
import json

class CentreonWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        # Default parameters
        environment = 'Production'
        severity ='ok'
        group ='Centreon'
        text = ''
        tags = []
        attributes = {}
        origin = ''

        return Alert(
            resource=payload['resource'],
            event=payload['event'],
            environment=payload.get('environment', environment),
            severity=payload.get('severity', severity),
            service=['centreon'],
            group=payload.get('group', group),
            value='BAN',
            text=payload.get('message', text),
            tags=payload.get('tags', tags),
            attributes=payload.get('attributes', attributes),
            origin=payload.get('hostname', origin),
            raw_data=json.dumps(payload, indent=4)
        )
