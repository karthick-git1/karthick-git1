from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '<html><head>
	<meta name="viewport" content="width=device-width">
	<link href="styles/style.css" rel="stylesheet">
</head>


	<body>
		<meta charset="utf-8">
		<h1>Hello! This is my first Web App!</h1> 
			<h2 style="
    color: chocolate;
"> I am updating this from my mobile </h2> 

<p style="
    COLOR: darkblue;
">  This website is designed for my son Tholkaapiyan </p>

<img src="images/IMG_9714.jpg" alt="My test image" style="max-width: 50%;
    
">

<ul>
  <li>Monthly_birthdays</li>
  <li>Picnics</li>
  <li>With_parents</li>
</ul>

<p>Enjoy…</p>


	
</body></html>	\n'
