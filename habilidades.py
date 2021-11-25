from flask_restful import Resource

listahabilidades = ['Python', 'Flask', 'PHP', 'Django']
class Habilidades(Resource):
    def get(self):
        return listahabilidades
