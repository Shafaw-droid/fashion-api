from flask_restful import Resource, reqparse, abort, marshal_with

from extension import db
from model import CustomerFavoriteBrands
from schema import FavoriteBrandField

favorite_args = reqparse.RequestParser()
favorite_args.add_argument('customer_id', type=int, required=True, help="Customer ID is required")
favorite_args.add_argument('brand_id', type=int, required=True, help="Brand ID is required")


class FavoriteBandResource(Resource):
    @marshal_with(FavoriteBrandField)
    def get(self):
        favorite_brands = CustomerFavoriteBrands.query.all()
        return favorite_brands

    @marshal_with(FavoriteBrandField)
    def post(self):
        args = favorite_args.parse_args()
        favorite_brand = CustomerFavoriteBrands(customer_id=args['customer_id'], brand_id=args['brand_id'])
        db.session.add(favorite_brand)
        db.session.commit()
        return favorite_brand, 201


class FavoriteBrandList(Resource):
    @marshal_with(FavoriteBrandField)
    def get(self, favorite_brand_id):
        existing = CustomerFavoriteBrands.query.filter_by(favorite_brand_id=favorite_brand_id).first()
        if not existing:
            abort(404, messages='not found')
        return existing, 200
