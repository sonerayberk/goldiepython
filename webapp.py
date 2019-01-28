""" Data visualization for voted records from DOU (developers of Ukraine). """

import developers

import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Developers of Ukraine'),

    dcc.Graph(
        id='salaries',
        figure={
            'data': [
                {
                    'x': list(developers.avg_salaries.keys()),
                    'y': [value for key, value in developers.avg_salaries.items()],
                    'type': 'bar', 'name': 'SF'
                },
            ],
            'layout': {
                'title': 'Salaries Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
