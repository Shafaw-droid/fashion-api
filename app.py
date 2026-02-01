from flask import Flask
from flask_restful import Api
from extension import db
from flask_migrate import Migrate
from model import Brand, Customer, CustomerFavoriteBrands, CustomerSavedOutfits,Clothing




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate=Migrate()

migrate.init_app(app,db)

api = Api(app)

with app.app_context():
    db.create_all()

from resources.brands import BrandResource,BrandResourceList
from resources.clothings import ClothingResources,ClothingList
from resources.customers import CustomerResources,CustomerList
from resources.outfits import OutfitResources,OutfitList
from resources.preferences import PreferenceResource,PreferenceList


api.add_resource(PreferenceResource,'/api/preference/')
api.add_resource(OutfitResources,'/api/outfits/')
api.add_resource(CustomerResources,'/api/customers/')
api.add_resource(ClothingResources,'/api/clothing/')
api.add_resource(ClothingList,'/api/clothing/<int:clothing_id>')
api.add_resource(BrandResource,'/api/brands/')
api.add_resource(BrandResourceList,'/api/brands/<int:brand_id>')

@app.route('/')
def journey():
    return'one step at a time'

if __name__=='__main__':
    app.run(debug=True)