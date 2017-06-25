from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class Rest(Resource):
    def get(self):
        return {
            'Galaxies': ['Milkyway', 'Andromeda',
            'Large Magellanic Cloud (LMC)',
            'Small Magellanic Cloud (SMC)'
            ]
        }

# Create routes
api.add_resource(Rest, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
from flask import Flask
from flask_restful import Resource, Api

# Instantiate the app
app = Flask(__name__)
api = Api(app)

class Rest(Resource):
    def get(self):
        return {
            'Galaxies': ['Milkyway', 'Andromeda',
            'Large Magellanic Cloud (LMC)',
            'Small Magellanic Cloud (SMC)'
            ]
        }

# Create routes
api.add_resource(Rest, '/')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
