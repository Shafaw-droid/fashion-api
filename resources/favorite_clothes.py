from flask_restful import Resource, reqparse, abort, marshal_with

from extension import db
from model import CustomerFavoriteClothing
from schema import FavoriteClothingField

favorite_args = reqparse.RequestParser()
favorite_args.add_argument('customer_id', type=int, required=True, help="Customer ID is required")
favorite_args.add_argument('clothing_id', type=int, required=True, help="clothes ID is required")


class FavoriteClothingResource(Resource):
    @marshal_with(FavoriteClothingField)
    def get(self):
        favorite_brands = CustomerFavoriteClothing.query.all()
        return favorite_brands

    @marshal_with(FavoriteClothingField)
    def post(self):
        args = favorite_args.parse_args()
        favorite_clothes = CustomerFavoriteClothing(customer_id=args['customer_id'], clothing_id=args['clothing_id'])
        db.session.add(favorite_clothes)
        db.session.commit()
        return favorite_clothes, 201


class FavoriteClothingList(Resource):
    @marshal_with(FavoriteClothingField)
    def get(self, favorite_clothing_id):
        existing = CustomerFavoriteClothing.query.filter_by(favorite_clothing_id=favorite_clothing_id).first()
        if not existing:
            abort(404, messages='favorite clothes not found')
        return existing, 200
