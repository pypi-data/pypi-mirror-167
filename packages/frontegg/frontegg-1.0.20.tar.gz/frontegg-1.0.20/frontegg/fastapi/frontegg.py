from fastapi import FastAPI, Request, Response
from frontegg.baseConfig.frontegg_proxy import FronteggProxy
import typing
import frontegg.fastapi.secure_access as secure_access
from fastapi.concurrency import run_in_threadpool
from requests import Response as ResponseType

class Frontegg(FronteggProxy):
    def __init__(self):
        pass

    def init_app(
            self,
            app: FastAPI,
            client_id: str,
            api_key,
            context_provider: typing.Callable = None,
            authentication_middleware=None,
            with_secure_access: bool = False,
            middleware_prefix: str = None,
    ):

        if with_secure_access:
            context_provider = context_provider or secure_access.context_provider
            authentication_middleware = authentication_middleware or secure_access.authentication_middleware

        super(Frontegg, self).__init__(client_id, api_key, context_provider, authentication_middleware, middleware_prefix)

        @app.api_route(
            path="/" + self.middleware_prefix + "{application_path:path}",
            methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
            include_in_schema=False,
        )
        async def proxy_frontegg_requests(
                application_path: str,
                request: Request,
        ) -> Response:
            body = await request.body()
            host = request.headers.get('host') or request.client.host
            host = host.split(':')[0]
            response = await run_in_threadpool(
                self.proxy_request,
                request=request, method=request.method, path=application_path,
                host=host, body=body, headers=request.headers,
                params=request.query_params
            )
            fast_api_response = Response(content=response.content, status_code=response.status_code, headers=response.headers)
            if isinstance(response, ResponseType):
                for cookieKey in response.cookies.keys():
                    cookie_val = response.cookies.get(cookieKey).OutputString()
                    if cookie_val.endswith(','):
                        cookie_val = cookie_val[:-1]
                    fast_api_response.headers.append('set-cookie',  cookie_val)
            return fast_api_response


frontegg = Frontegg()
