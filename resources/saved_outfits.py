from flask_restful import Resource, reqparse, abort, marshal_with

from extension import db
from model import CustomerSavedOutfits
from schema import SavedOutfitField

favorite_args = reqparse.RequestParser()
favorite_args.add_argument('customer_id', type=int, required=True, help="Customer ID is required")
favorite_args.add_argument('outfit_id', type=int, required=True, help="Outfit ID is required")


class SavedOutfitResource(Resource):
    @marshal_with(SavedOutfitField)
    def get(self):
        saved_outfit = CustomerSavedOutfits.query.all()
        return saved_outfit

    @marshal_with(SavedOutfitField)
    def post(self):
        args = favorite_args.parse_args()
        saved_outfit = CustomerSavedOutfits(outfit_id=args['outfit_id'], customer_id=args['customer_id'])
        db.session.add(saved_outfit)
        db.session.commit()
        return saved_outfit, 201


class SavedOutfitList(Resource):
    @marshal_with(SavedOutfitField)
    def get(self, saved_outfit_id):
        existing = CustomerSavedOutfits.query.filter_by(saved_outfit_id=saved_outfit_id).first()
        if not existing:
            abort(404, messages='saved outfits not found')
        return existing, 200
