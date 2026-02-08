from flask_restful import Resource, reqparse, marshal_with, abort

from model import Clothing
from extension import db
from schema import ClothingField

clothing_args = reqparse.RequestParser()
clothing_args.add_argument('brand_id', type=int, required=True, help="brand_id is required")
clothing_args.add_argument('clothing_name', type=str, required=True, help='clothing name cannot be blank ')
clothing_args.add_argument('category', type=str, required=True)
clothing_args.add_argument('size', type=str, required=True)
clothing_args.add_argument('colour', type=str, required=True)
clothing_args.add_argument('price', type=float, required=True)


class ClothingResources(Resource):
    @marshal_with(ClothingField)
    def get(self):
        clothing = Clothing.query.all()
        return clothing

    @marshal_with(ClothingField)
    def post(self):
        args = clothing_args.parse_args()
        clothing = Clothing(brand_id=args['brand_id'], clothing_name=args['clothing_name'], category=args['category'],
                            size=args['size'], colour=args['colour'], price=args['price'])
        db.session.add(clothing)
        db.session.commit()
        clothes = Clothing.query.all()
        return clothes, 201


class ClothingList(Resource):
    @marshal_with(ClothingField)
    def get(self, clothing_id):
        get_cloth = Clothing.query.filter_by(clothing_id=clothing_id).first()
        if not get_cloth:
            abort(404, message='clothes not found')
        return get_cloth

    @marshal_with(ClothingField)
    def patch(self, clothing_id):
        args = clothing_args.parse_args()
        get_cloth = Clothing.query.filter_by(clothing_id=clothing_id).first()
        if not get_cloth:
            abort(404, message='clothes not found')
        get_cloth.name = args['clothing_name']
        get_cloth.category = args['category']
        get_cloth.size = args['size']
        get_cloth.colour = args['colour']
        get_cloth.price = args['price']
        db.session.commit()
        return get_cloth, 'update is successful'
