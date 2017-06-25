from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class API(Resource):
    def get(self):
        return {
            'Galaxies': ['Milkyway', 'Andromeda',
            'Large Magellanic Cloud (LMC)',
            'Small Magellanic Cloud (SMC)',
            'Kevin is a Boss!!!'
            ]
        }

# Create routes
api.add_resource(API, '/',  methods=['GET'])

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
