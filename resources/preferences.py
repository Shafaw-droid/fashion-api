from flask_restful import Resource, reqparse, marshal_with,abort
from model import CustomerStylingPreference
from extension import db
from schema import StylingPreferenceField



preference_args= reqparse.RequestParser()
preference_args.add_argument('customer_id', type=int, required=True)
preference_args.add_argument('preferred_style', type=str, required=True)
preference_args.add_argument('preferred_color', type=str, required=True)
preference_args.add_argument('preferred_fit', type=str, required=True)
preference_args.add_argument('preferred_season', type=str, required=True)
preference_args.add_argument('budget_range', type=str, required=True)


class PreferenceResource(Resource):
    @marshal_with(StylingPreferenceField)
    def get(self):
        preference=CustomerStylingPreference.query.all()
        return preference

    @marshal_with(StylingPreferenceField)
    def post(self):
        args=preference_args.parse_args()
        preference=CustomerStylingPreference(preferred_style=args['preferred_style'],preferred_color=['preferred_color'],preferred_fit=args['preferred_fit'],preferred_season=args['preferred_season'],budget_range=args['budget_range'])
        db.session.add(preference)
        db.session.commit()
        return CustomerStylingPreference.query.all()


class PreferenceList(Resource):
    @marshal_with(StylingPreferenceField)
    def get(self,preferred_id):
        preference=CustomerStylingPreference.query.filter_by(id=preferred_id).first()
        if not preference:
            abort(404,message='Customer styling preference not found')
        return preference,200

    @marshal_with(StylingPreferenceField)
    def patch(self,preferred_id):
        args=preference_args.parse_args()
        preference=CustomerStylingPreference.query.filter_by(id=preferred_id).first()
        if not preference:
            abort(404,message='Customer styling preference does not exist')
        preference.preferred_style=args['preferred_style']
        preference.preferred_color=args['preferred_color']
        preference.preferred_fit=args['preferred_fit']
        preference.preferred_season=args['preferred_season']
        preference.budget_range=args['budget_range']









