## Code
To begin, let's make some imports:

```
import dash
import dash_core_components as dcc
import dash_html_components as html
```

Here, we're just importing things like the dash lib, various components (things like graph components), and then HTML components (things like div tags...etc). Next, we begin our app:

```
app = dash.Dash()
```

Since Dash is built around the Flask framework, many of these app settings and setups should look familiar if you are familiar with Flask. Next, we create a layout:

```
app.layout = html.Div('Dash Tutorials')
```

this would make an app that simply said "Dash Tutorials" on page load. Nothing amazing, but nice and simple! To's run this:

```
app.layout = html.Div('Dash Tutorials')
```
