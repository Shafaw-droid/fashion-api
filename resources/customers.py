from flask_restful import Resource, reqparse, marshal_with, abort
from extension import db
from schema import CustomerField
from model import Customer

customer_args = reqparse.RequestParser()
customer_args.add_argument('customer_name', type=str, required=True, help='Customer name is required')
customer_args.add_argument('contact', type=str, required=True)
customer_args.add_argument('gender', type=str, choices=('male', 'female', 'other'), required=True)
customer_args.add_argument('age', type=int, required=True)


class CustomerResources(Resource):
    @marshal_with(CustomerField)
    def get(self):
        customer = Customer.query.all()
        return customer

    @marshal_with(CustomerField)
    def post(self):
        args = customer_args.parse_args()
        customer = Customer(customer_name=args['customer_name'], contact=args['contact'], gender=args['gender'],
                            age=args['age'])
        db.session.add(customer)
        db.session.commit()
        return Customer.query.all(), 201


class CustomerList(Resource):
    @marshal_with(CustomerField)
    def get(self, customer_id):
        customer = Customer.query.filter_by(customer_id=customer_id).first()
        if not customer:
            abort(404, message='customer not found')
        return customer

    @marshal_with(CustomerField)
    def patch(self, customer_id):
        args = customer_args.parse_args()
        customer = Customer.query.filter_by(customer_id=customer_id).first()
        if not customer:
            abort(404, message='customer does not exist')
        customer.customer_name = args['customer_name']
        customer.contact = args['contact']
        customer.gender = args['gender']
        customer.age = args['age']
        db.session.commit()
        return customer, "Update successful", 200

    @marshal_with(CustomerField)
    def delete(self, customer_id):
        customer = Customer.query.filter_by(id=customer_id).first()
        if not customer:
            abort(404, message="Customer does not exist")

        db.session.delete(customer)
        db.session.commit()
        return "Customer deleted successfully", 200
