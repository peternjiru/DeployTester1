from config import app, Resource, api

# test dictionary to replace with acrual db
programs = {
    'after school 1': {'name': 'happy kids inc.'},
    'after school 2': {'name': 'hebrew school'}
}

class Program(Resource):
    def get(self):
        return programs

api.add_resource(Program, '/')

if __name__ == '__main__':
    app.run()
