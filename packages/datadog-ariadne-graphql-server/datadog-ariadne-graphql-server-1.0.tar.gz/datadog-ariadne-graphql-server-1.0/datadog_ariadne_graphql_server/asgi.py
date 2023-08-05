from ariadne.asgi import GraphQL as BaseGraphQL
from starlette.requests import Request
from ddtrace import tracer

class GraphQL(BaseGraphQL):
    def _instrument_datadog(self, request_dict: dict):
        if 'operationName' in request_dict.keys() and \
            isinstance(request_dict['operationName'], str) and \
            request_dict['operationName']:
            span = tracer.current_root_span()
            span.set_tag("operation_name", request_dict['operationName'])
            span.resource = f"POST /graphql?operationName={request_dict['operationName']}"

    # Hook into the already processed request data for setting up Datadog APM
    async def extract_data_from_request(self, request: Request):
        request_dict = await super().extract_data_from_request(request)
        self._instrument_datadog(request_dict)
        return request_dict