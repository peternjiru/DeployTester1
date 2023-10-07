from config import app, Resource, api

class Program(Resource):
    def get(self):
        return "Habari!"

api.add_resource(Program, '/')

if __name__ == '__main__':
    app.run()
