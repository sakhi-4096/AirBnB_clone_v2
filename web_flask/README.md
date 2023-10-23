# AirBnB clone - Web framework
Web applications have changed that usability and interactivity they provide rival that of a native application. Expertise to build tailored solutions that reach this level of proficiency is demanding. There are tools that make application development easier, like web app framework.

![Flask](https://res.cloudinary.com/practicaldev/image/fetch/s--8UWnZMxs--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://external-content.duckduckgo.com/iu/%3Fu%3Dhttps%253A%252F%252Fimage.slidesharecdn.com%252Fflaskpython-130201154928-phpapp01%252F95%252Fflask-python-2-638.jpg%253Fcb%253D1359733858%26f%3D1%26nofb%3D1)

## Features
A web application framework is a software framework designed to aid in the development of web applications, simplifying common tasks and providing a structured way to build web applications.
Key components and concepts related to web app frameworks:
1. **Minimal Application**: typically consists of an entry point or main script that initializes the framework and starts the application. Might include basic routing and rendering functionality.
2. **Routing**: defines how the application responds to different URLs or routes. It maps specific routes to functions or handles that will be executed when a user visits those routes. *Example: you can map the URL '/about' to a function that renders the About page.*
3. **Rendering Templates**: Templates are used to separate the presentation (HTML) from the logic of your application. These templates can be populated with dynamic data and then rendered to produce the final HTML that's sent to the client's browser.
4. **Synopsis**: or summary is an overview of what the application does, the routes it supports, and any special features. *Typically used for documentation or reference*.
5. **Variables**: are used to store data that can be passed to templates or used in the application's logic. Allow for dynamic content to be generated and displayed to users.
6. **Comments**: used for documentation and clarification is source code.
7. **Whitespace Control**: allows developers to manage the indentation and spacing in templated for better code readability and aesthetics.
8. **List of Control Structures**: conditional statements, and other constructs that enable developers to make decisions and control flow of application.

## Usage
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Sakhile and the World!"

if __name__ == '__main__':
    app.run()
```
```HTML
<!-- template.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>hELLO, {{ name }}!</h1>
</body>

```

## Credits
 * [A Minimal Application](https://flask.palletsprojects.com/en/2.3.x/quickstart/)
 * [Template Designer Documentation](https://jinja.palletsprojects.com/en/3.0.x/templates/)
 * [Flask Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
