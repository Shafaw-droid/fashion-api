from flask_restful import Resource, reqparse, marshal_with,abort
from model import Brand
from extension import db
from schema import BrandField, ClothingField

brand_args = reqparse.RequestParser()
brand_args.add_argument("brand_name", type=str, required=True, help="Group number is required")
brand_args.add_argument('brand_country',type=str,required=True)
brand_args.add_argument('founder_yr',type=int,required=True)



class BrandResource(Resource):

    @marshal_with(BrandField)
    def get(self):
        return Brand.query.all()


    @marshal_with(BrandField)
    def post(self):
        args=brand_args.parse_args()
        brand=Brand(brand_name=args['brand_name'],brand_country=args['brand_country'],founder_yr=args['founder_yr'])
        db.session.add(brand)
        db.session.commit()
        return Brand.query.all(), 201

class BrandResourceList(Resource):
    @marshal_with(BrandField)
    def get(self,brand_id):
        brands=Brand.query.filter_by(brand_id=brand_id).first()
        if not brands:
            abort(404,message='brand not found')
        return brands



    @marshal_with(BrandField)
    def patch(self,brand_id):
        args=brand_args.parse_args()
        brands=Brand.query.filter_by(brand_id=brand_id).first()
        if not brands:
            abort(404,message='brand cannot be found')
        brands.brand_name=args['brand_name']
        brands.brand_country=args['brand_country']
        brands.founder_yr=args['founder_yr']
        db.session.add(brands)
        db.session.commit()
        return brands,'Brand Resources successfully created'











