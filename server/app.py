from config import app, Resource, api, jsonify, make_response
from .models import Program


class AfterSchoolPrograms(Resource):
    def get(self):
        programs = [program.to_dict() for program in Program.query.all()]
        return make_response(jsonify(programs), 200)


api.add_resource(AfterSchoolPrograms, '/')

if __name__ == '__main__':
    app.run()
