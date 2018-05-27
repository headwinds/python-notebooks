from sanic import Sanic
from sanic import response
import aiohttp
import asyncio
import re
import json
from pages.index import INDEX

app = Sanic(__name__)

callback_re = re.compile(r'^[a-zA-Z_](\.?[a-zA-Z0-9_]+)+$')
is_valid_callback = callback_re.match

async def head(session, url):
    try:
        async with session.head(url) as response:
            return {
                'ok': True,
                'headers': dict(response.headers),
                'status': response.status,
                'url': url,
            }
    except Exception as e:
        return {
            'ok': False,
            'error': str(e),
            'url': url,
        }


@app.route('/')
async def handle_request(request):
    urls = request.args.getlist('url')
    callback = request.args.get('callback')
    if urls:
        if len(urls) > 10:
            return response.json([{
                'ok': False,
                'error': 'Max 10 URLs allowed'
            }], status=400)
        async with aiohttp.ClientSession() as session:
            head_infos = await asyncio.gather(*[
                head(session, url) for url in urls
            ])
            if callback and is_valid_callback(callback):
                return response.text(
                    '{}({})'.format(callback, json.dumps(head_infos, indent=2)),
                    content_type='application/javascript',
                    headers={'Access-Control-Allow-Origin': '*'},
                )
            else:
                return response.json(
                    head_infos,
                    headers={'Access-Control-Allow-Origin': '*'},
                )
    else:
        return response.html(INDEX)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
