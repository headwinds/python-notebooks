INDEX = """<!DOCTYPE html>
<style>
body {
font-family: "Helvetica"
}
</style>
<title>champions</title>
<div>
<h1>Champions: miner or lumberjack</h1>
<div>
<h1>Are you suited for space travel? Can you survive the 400 sq feet challenge?</h1>
<h2>You might just fall in love with tiny living</h2>

<div>
Bears Den
</div>

<div>
Attn: Fish - live in your aquarium
</div>

<div>
Attn: Owner - Maintain your aquarium
you want to make a profit but not to the point of squeezing your tentant.
Within market limits, we want to set a fair price.
What are the social consequences of high prices?
Low prices?

</div>
<p><b>Self Help</b></p>
<p>
<ul>
<li>Family</li>
<li>Home</li>
<li>Fitness</li>
<li>Nutrition</li>
<li>Travel</li>
</ul>
</p>
<p><b>Classification</b></p>
<p>classify twitter users into 4 D&D classes: warrior, archer, cleric, and wizard
Who are they championing and fighting?!
Further classify them as Astronaut or Landlocked - would they go or remain at home</p>
<p><b>Regression</b></p>
<p>Determine the probability that they will follow you
Determine the probability that there next tweet will be on brand to their class</p>
</div>
<div>
<p>JSON (and JSON-P) API for analyzing the url of twitter user.
<ul>
    <li><a href="/?url=https://twitter.com/headwinds">/?url=https://twitter.com/headwinds</a>
    <li><a href="/?url=https://twitter.com/headwinds/&amp;callback=foo">/?url=https://twitter.com/headwinds/&amp;callback=foo</a>
    <li><a href="/?url=https://twitter.com/headwinds/&amp;url=https://twitter.com/elonmusk">/?url=https://twitter.com/headwinds/&amp;url=https://twitter.com/elonmusk</a>
</ul>
</div>
<div>
<h2>Example</h2>
<p>https://champions.now.sh/?url=https://twitter.com/headwinds will return:</p>
<p>
<pre>
<code>
[
    {
        "ok": true,
        "headers": {
            "Date": "Sat, 14 Oct 2017 18:37:52 GMT",
            "Content-Type": "text/html; charset=utf-8",
            "Connection": "keep-alive",
            "Set-Cookie": "__cfduid=dd0b71b4e89bbaca5b27fa06c0b95af4a1508006272; expires=Sun, 14-Oct-18 18:37:52 GMT; path=/; domain=.simonwillison.net; HttpOnly; Secure",
            "Cache-Control": "s-maxage=200",
            "X-Frame-Options": "SAMEORIGIN",
            "Via": "1.1 vegur",
            "CF-Cache-Status": "HIT",
            "Vary": "Accept-Encoding",
            "Server": "cloudflare-nginx",
            "CF-RAY": "3adca70269a51e8f-SJC",
            "Content-Encoding": "gzip"
        },
        "data":{
            "class": "Archer",
            "probability": "0.94",
        }
        "status": 200,
        "url": "https://simonwillison.net/"
    }
]
</code>
</pre>
</p>
</div>

<div>
<h2>Credit</h2>
<p>Background: <a href="https://simonwillison.net/2017/Oct/14/async-python-sanic-now/">Deploying an asynchronous Python microservice with Sanic and Zeit Now</a></p>
<p>Source code: <a href="https://github.com/simonw/json-head">github.com/simonw/json-head</a></p>
</div>
"""
