from extension import db

class Brand(db.Model):
    __tablename__='brands'

    brand_id=db.Column(db.Integer,primary_key=True)
    brand_name=db.Column(db.String(80),index=True,nullable=False)
    brand_country=db.Column(db.String(80),index=True,nullable=False)
    founder_yr=db.Column(db.Integer,index=True,nullable=True)

    clothing=db.relationship('Clothing',back_populates='brand',cascade='all,delete-orphan')
    favorite_brands= db.relationship('CustomerFavoriteBrands', back_populates='brands',cascade='all,delete-orphan')


    def __repr__(self):
        return f"<Brand {self.brand_name}>"


class Clothing(db.Model):
    __tablename__='clothing'
    clothing_id=db.Column(db.Integer,primary_key=True)
    brand_id=db.Column(db.Integer,db.ForeignKey('brands.brand_id'),nullable=False)

    clothing_name=db.Column(db.String(80),index=True,nullable=False)
    category=db.Column(db.String(80),index=True,nullable=False)
    size=db.Column(db.String(20),index=True,nullable=False)
    colour=db.Column(db.String(50),index=True,nullable=False)
    price=db.Column(db.Float,index=True,nullable=False)

    brand=db.relationship('Brand',back_populates='clothing')
    outfit_clothes=db.relationship('OutfitClothing', back_populates='clothing', cascade='all,delete-orphan')
    favorite_clothes = db.relationship('CustomerFavoriteClothing', back_populates='clothing', cascade='all,delete-orphan')

    def __repr__(self):
        return f"<Clothing{self.clothing_name}>"


class Outfit(db.Model):
    __tablename__='outfits'
    outfit_id=db.Column(db.Integer,primary_key=True)

    outfit_name=db.Column(db.String(80),index=True,nullable=False)
    occasion=db.Column(db.String(80),index=True,nullable=False)
    season=db.Column(db.String(80),index=True,nullable=False)

    outfit_clothes=db.relationship('OutfitClothing', back_populates='outfit',cascade='all,delete-orphan')
    saved_outfits=db.relationship('CustomerSavedOutfits', back_populates='outfits',cascade='all,delete-orphan')


    def __repr__(self):
        return f"<Outfit {self.outfit_name}>"


class OutfitClothing(db.Model):
    __tablename__='outfit_clothes'
    outfit_clothing_id=db.Column(db.Integer,primary_key=True)
    outfit_id=db.Column(db.String(80), db.ForeignKey('outfits.outfit_id'),nullable=False)
    clothing_id=db.Column(db.Integer,db.ForeignKey('clothing.clothing_id'),nullable=False)

    clothing=db.relationship('Clothing',back_populates='outfit_clothes')
    outfit=db.relationship('Outfit', back_populates='outfit_clothes')




class Customer(db.Model):
    __tablename__='customers'

    customer_id=db.Column(db.Integer,primary_key=True)
    customer_name=db.Column(db.String(80),index=True,nullable=False)
    contact=db.Column(db.String(80),index=True,nullable=False)
    gender=db.Column(db.String(80),index=True,nullable=False)
    age=db.Column(db.String(80),index=True,nullable=False)

    favorite_brands=db.relationship('CustomerFavoriteBrands', back_populates='customer',cascade='all,delete-orphan')
    favorite_clothes=db.relationship('CustomerFavoriteClothing', back_populates='customer',cascade='all,delete-orphan')
    saved_outfits=db.relationship('CustomerSavedOutfits', back_populates='customer',cascade='all,delete-orphan')
    preferences=db.relationship('CustomerStylingPreference', back_populates='customer',cascade='all,delete-orphan')

    def __repr__(self):
        return f"<Customer {self.customer_name}>"


class CustomerStylingPreference(db.Model):
    __tablename__='preferences'

    preference_id=db.Column(db.Integer,primary_key=True)
    customer_id =db.Column(db.Integer,db.ForeignKey('customers.customer_id'),nullable=False)
    preferred_style=db.Column(db.String(80))
    preferred_colour=db.Column(db.String(80))
    preferred_fit=db.Column(db.String(80))
    preferred_season=db.Column(db.String(80))
    budget_range=db.Column(db.String(80))

    customer=db.relationship('Customer', back_populates='preferences')



class CustomerFavoriteBrands (db.Model):
    __tablename__='favorite_brands'

    favorite_brand_id=db.Column(db.Integer,primary_key=True)

    customer_id=db.Column(db.Integer,db.ForeignKey('customers.customer_id'))
    brand_id=db.Column(db.Integer,db.ForeignKey('brands.brand_id'))

    brands= db.relationship('Brand', back_populates='favorite_brands')
    customer=db.relationship('Customer', back_populates='favorite_brands')




class CustomerFavoriteClothing(db.Model):
    __tablename__ = 'favorite_clothes'

    favorite_clothing_id=db.Column(db.Integer,primary_key=True)

    customer_id=db.Column(db.Integer,db.ForeignKey('customers.customer_id'))
    clothing_id=db.Column(db.Integer,db.ForeignKey('clothing.clothing_id'))

    customer=db.relationship('Customer', back_populates='favorite_clothes')
    clothing = db.relationship('Clothing', back_populates='favorite_clothes')



class CustomerSavedOutfits(db.Model):
    __tablename__='saved_outfits'

    saved_outfit_id = db.Column(db.Integer, primary_key=True)

    customer_id=db.Column(db.Integer,db.ForeignKey('customers.customer_id'))
    outfit_id=db.Column(db.Integer,db.ForeignKey('outfits.outfit_id'))

    outfits = db.relationship('Outfit', back_populates='saved_outfits')
    customer=db.relationship('Customer', back_populates='saved_outfits')















