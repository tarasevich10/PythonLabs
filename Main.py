from flask import Flask, abort
from flask_restful import Resource, fields, reqparse, marshal, Api

app = Flask(__name__, static_url_path="")
api = Api(app)

tools = [
    {
        'Id': 0,
        'work': 'Default',
        'tool': 'Default',
        'madein': 'Default'
    }
]

tools_fields = {
    'id': fields.Integer,
    'work': fields.String,
    'tool': fields.String,
    'madein': fields.String
}


class Tool(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, required=True, help='No Id provided', location='json')
        self.reqparse.add_argument('work', type=str, location='json')
        self.reqparse.add_argument('tool', type=str, location='json')
        self.reqparse.add_argument('madein', type=str, location='json')
        super(Tool, self).__init__()  # super().__init__() / Good.__init__(self)

    def get(self, id):
        tool = [tool for tool in tools if tool.get('id') == id]
        if len(tool) == 0:
            abort(404)
        return {'Tool': marshal(tool[0], tools_fields)}

    def delete(self, id):
        tool = [tool for tool in tools if tool.get('id') == id]
        if len(tool) == 0:
            abort(404)
        tools.remove(tool[0])
        return {'result': True}

    def put(self):
        args = self.reqparse.parse_args()
        tool = {
            'Id': tools[-1]['Id'] + 1,
            'id': args['id'],
            'work': args['work'],
            'tool': args['tool'],
            'madein': args['madein']
        }
        tools.append(tool)
        return {'Tool': marshal(tool, tools_fields)}, 201

    def post(self):
        args = self.reqparse.parse_args()
        tool = [tool for tool in tools if tool.get('id') == args['id']]
        if len(tool) == 0:
            abort(404)
        tool = tool[0]
        args = self.reqparse.parse_args()
        for k, v in args.items():
            if v is not None:
                tool[k] = v


api.add_resource(Tool, '/tools', endpoint='tools')
api.add_resource(Tool, '/tools/<int:id>', endpoint='tool')

if __name__ == '__main__':
    app.run(debug=True)
