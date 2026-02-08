from flask_restful import Resource, reqparse, marshal_with, abort
from sqlalchemy import result_tuple

from model import Outfit
from extension import db
from schema import OutfitField

outfit_args = reqparse.RequestParser()
outfit_args.add_argument('outfit_name', type=str, required=True, help='outfit name cannot be blank')
outfit_args.add_argument('occasion', type=str, required=True)
outfit_args.add_argument('season', type=str, required=True)


class OutfitResources(Resource):
    @marshal_with(OutfitField)
    def get(self):
        outfit = Outfit.query.all()
        return outfit

    @marshal_with(OutfitField)
    def post(self):
        args = outfit_args.parse_args()
        outfit = Outfit(outfit_name=args['outfit_name'], occasion=args['occasion'], season=args['season'])
        db.session.add(outfit)
        db.session.commit()
        return outfit, 201


class OutfitList(Resource):
    @marshal_with(OutfitField)
    def get(self, outfit_id):
        outfit = Outfit.query.filter_by(outfit_id=outfit_id).first()
        if not outfit:
            abort(404, messaage='outfit cannot be found')
        return outfit

    @marshal_with(OutfitField)
    def patch(self, outfit_id):
        args = outfit_args.parse_args()
        outfit = Outfit.query.filter_by(outfit_id=outfit_id).first()
        if not outfit:
            abort(404, message='outfit does not exist')
        outfit.outfit_name = args['outfit_name']
        outfit.occasion = args['occasion']
        outfit.season = args['season']
        db.session.commit()
        return outfit, 'outfit is successfully updated', 201

    @marshal_with(OutfitField)
    def delete(self, outfit_id):
        outfit = Outfit.query.filter_by(outfit_id=outfit_id).first()
        if not outfit:
            abort(404, message='does not exist')
        db.session.delete(outfit)
        db.session.commit()
        return ' outfit is successfully deleted', 200
