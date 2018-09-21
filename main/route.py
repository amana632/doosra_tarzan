from flask import request, jsonify
from main import app
from main.model import User, user_schema, users_schema, UserSchema, serviceprovider_schema, serviceproviders_schema, ServiceProvider, ServiceProviderSchema
from flask_marshmallow import Marshmallow
from main import db


@app.route("/serviceproviderupdate/<emailid>", methods=["PUT"])
def serviceprovider_update(emailid):
    serviceprovider = ServiceProvider.query.filter_by(emailid=emailid).first_or_404()

    emailid = request.json['emailid']
    service_advisor_name = request.json['name']
    service_advisor_no = request.json['phone']
    workshop_no = request.json['workshop_no']
    latitude = request.json['lat']
    longitude = request.json['long']
    user_pic = request.json['userpic']
    workshop_pic = request.json['workshoppic']
    gst = request.json['gst']
    service_category = request.json['category']
    pickup_facility = request.json['pickup_facility']
    twentyfourhour_facility = request.json['24hr']
    general_service = request.json['general_service']
    roadside_assistance = request.json['roadside_assistance']
    maintenence_repair = request.json['maintenence_repair']
    dent_repairing = request.json['dent_repairing']
    car_wash = request.json['car_wash']
    disc_general_service = request.json['disc_general_service']
    disc_roadside_assistance = request.json['disc_roadside_assistance']
    disc_maintenence_repair = request.json['disc_maintenence_repair']
    disc_dent_repairing = request.json['disc_dent_repairing']
    disc_car_wash = request.json['disc_car_wash']
    bank_name = request.json['bank_name']
    branch_name = request.json['branch_name']
    ifsc_code = request.json['ifsc_code']
    account_number = request.json['account_number']
    hb_twotosix = request.json['hb_twotosix']
    hb_sixtoten = request.json['hb_sixtoten']
    hb_tenabove = request.json['hb_tenabove']
    sedan_sixtoten = request.json['sedan_sixtoten']
    sedan_tentotwentyfive = request.json['sedan_tentotwentyfive']
    sedan_twentyfiveabove = request.json['sedan_twentyfiveabove']
    suv_twelvetotwenty = request.json['suv_twelvetotwenty']
    suv_twentytoforty = request.json['suv_twentytoforty']
    suv_fortyabove = request.json['suv_fortyabove']
    muv_fifteentoforty = request.json['muv_fifteentoforty']
    muv_fortyabove = request.json['muv_fortyabove']


    serviceprovider.emailid = emailid
    serviceprovider.service_advisor_name = service_advisor_name
    serviceprovider.service_advisor_no = service_advisor_no
    serviceprovider.workshop_no = workshop_no
    serviceprovider.latitude = latitude
    serviceprovider.longitude = longitude
    serviceprovider.user_pic = user_pic
    serviceprovider.workshop_pic = workshop_pic
    serviceprovider.gst = gst
    serviceprovider.service_category = service_category
    serviceprovider.pickup_facility = pickup_facility
    serviceprovider.twentyfourhour_facility = twentyfourhour_facility
    serviceprovider.general_service = general_service
    serviceprovider.roadside_assistance = roadside_assistance
    serviceprovider.maintenence_repair = maintenence_repair
    serviceprovider.dent_repairing = dent_repairing
    serviceprovider.car_wash = car_wash
    serviceprovider.disc_general_service = disc_general_service
    serviceprovider.disc_roadside_assistance = disc_roadside_assistance
    serviceprovider.disc_maintenence_repair = disc_maintenence_repair
    serviceprovider.disc_dent_repairing = disc_dent_repairing
    serviceprovider.disc_car_wash = disc_car_wash
    serviceprovider.bank_name = bank_name
    serviceprovider.branch_name = branch_name
    serviceprovider.ifsc_code = ifsc_code
    serviceprovider.account_number = account_number
    serviceprovider.hb_twotosix = hb_twotosix
    serviceprovider.hb_sixtoten = hb_sixtoten
    serviceprovider.hb_tenabove = hb_tenabove
    serviceprovider.sedan_sixtoten = sedan_sixtoten
    serviceprovider.sedan_tentotwentyfive = sedan_tentotwentyfive
    serviceprovider.sedan_twentyfiveabove = sedan_twentyfiveabove
    serviceprovider.suv_twelvetotwenty = suv_twelvetotwenty
    serviceprovider.suv_twentytoforty = suv_twentytoforty
    serviceprovider.suv_fortyabove = suv_fortyabove
    serviceprovider.muv_fifteentoforty = muv_fifteentoforty
    serviceprovider.muv_fortyabove = muv_fortyabove
 

    db.session.commit()
    return serviceprovider_schema.jsonify(serviceprovider)


@app.route("/register_serviceprovider", methods=["POST"])
def register_serviceprovider():
    emailid = request.json['emailid']
    service_advisor_name = request.json['name']
    service_advisor_no = request.json['phone']
    workshop_no = request.json['workshop_no']
    latitude = request.json['lat']
    longitude = request.json['long']
    user_pic = request.json['userpic']
    workshop_pic = request.json['workshoppic']
    gst = request.json['gst']
    service_category = request.json['category']
    pickup_facility = request.json['pickup_facility']
    twentyfourhour_facility = request.json['twentyfourhour_facility']
    general_service = request.json['general_service']
    roadside_assistance = request.json['roadside_assistance']
    maintenence_repair = request.json['maintenence_repair']
    dent_repairing = request.json['dent_repairing']
    car_wash = request.json['car_wash']
    disc_general_service = request.json['disc_general_service']
    disc_roadside_assistance = request.json['disc_roadside_assistance']
    disc_maintenence_repair = request.json['disc_maintenence_repair']
    disc_dent_repairing = request.json['disc_dent_repairing']
    disc_car_wash = request.json['disc_car_wash']
    bank_name = request.json['bank_name']
    branch_name = request.json['branch_name']
    ifsc_code = request.json['ifsc_code']
    account_number = request.json['account_number']
    hb_twotosix = request.json['hb_twotosix']
    hb_sixtoten = request.json['hb_sixtoten']
    hb_tenabove = request.json['hb_tenabove']
    sedan_sixtoten = request.json['sedan_sixtoten']
    sedan_tentotwentyfive = request.json['sedan_tentotwentyfive']
    sedan_twentyfiveabove = request.json['sedan_twentyfiveabove']
    suv_twelvetotwenty = request.json['suv_twelvetotwenty']
    suv_twentytoforty = request.json['suv_twentytoforty']
    suv_fortyabove = request.json['suv_fortyabove']
    muv_fifteentoforty = request.json['muv_fifteentoforty']
    muv_fortyabove = request.json['muv_fortyabove']

    
    
    new_service_provider = ServiceProvider(emailid, service_advisor_name, service_advisor_no, workshop_no, latitude, longitude, user_pic, workshop_pic, gst, service_category, pickup_facility, twentyfourhour_facility, general_service, roadside_assistance, maintenence_repair, dent_repairing, car_wash, disc_general_service, disc_roadside_assistance, disc_maintenence_repair, disc_dent_repairing, disc_car_wash, bank_name, branch_name, ifsc_code, account_number, hb_twotosix, hb_sixtoten, hb_tenabove, sedan_sixtoten, sedan_tentotwentyfive, sedan_twentyfiveabove, suv_twelvetotwenty, suv_twentytoforty, suv_fortyabove, muv_fifteentoforty, muv_fortyabove)

    db.session.add(new_service_provider)
    db.session.commit()


# endpoint to show all users
@app.route("/service_provider", methods=["GET"])
def get_service_provider():
    all_serviceproviders = ServiceProvider.query.all()
    result = serviceproviders_schema.dump(all_serviceproviders)
    return jsonify(a=result.data)

@app.route('/service_provider/<emailid>')
def show_service_provider(emailid):
    serviceprovider = ServiceProvider.query.filter_by(emailid=emailid).first_or_404()
    return serviceprovider_schema.jsonify(serviceprovider)

@app.route("/user", methods=["POST"])
def add_user():
    password = request.json['password']
    email = request.json['emailid']
    user_type = request.json['user_type']
    
    
    new_user = User(password, email, user_type)

    db.session.add(new_user)
    db.session.commit()
    return user_schema.jsonify(new_user)


@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(a=result.data)

@app.route('/user/<email>')
def show_user(email):
    user = User.query.filter_by(email=email).first_or_404()
    return user_schema.jsonify(user)




@app.route("/generalservicepricing/<emailid>", methods=["PUT"])
def generalservicepricing_update(emailid):
    serviceprovider = ServiceProvider.query.filter_by(emailid=emailid).first_or_404()
 
    hb_twotosix = request.json['hb_twotosix']
    hb_sixtoten = request.json['hb_sixtoten']
    hb_tenabove = request.json['hb_tenabove']
    sedan_sixtoten = request.json['sedan_sixtoten']
    sedan_tentotwentyfive = request.json['sedan_tentotwentyfive']
    sedan_twentyfiveabove = request.json['sedan_twentyfiveabove']
    suv_twelvetotwenty = request.json['suv_twelvetotwenty']
    suv_twentytoforty = request.json['suv_twentytoforty']
    suv_fortyabove = request.json['suv_fortyabove']
    muv_fifteentoforty = request.json['muv_fifteentoforty']
    muv_fortyabove = request.json['muv_fortyabove']


    serviceprovider.hb_twotosix = hb_twotosix
    serviceprovider.hb_sixtoten = hb_sixtoten
    serviceprovider.hb_tenabove = hb_tenabove
    serviceprovider.sedan_sixtoten = sedan_sixtoten
    serviceprovider.sedan_tentotwentyfive = sedan_tentotwentyfive
    serviceprovider.sedan_twentyfiveabove = sedan_twentyfiveabove
    serviceprovider.suv_twelvetotwenty = suv_twelvetotwenty
    serviceprovider.suv_twentytoforty = suv_twentytoforty
    serviceprovider.suv_fortyabove = suv_fortyabove
    serviceprovider.muv_fifteentoforty = muv_fifteentoforty
    serviceprovider.muv_fortyabove = muv_fortyabove
 

    db.session.commit()
    return serviceprovider_schema.jsonify(serviceprovider)


@app.route("/bank_details/<emailid>", methods=["PUT"])
def bank_details_update(emailid):
    serviceprovider = ServiceProvider.query.filter_by(emailid=emailid).first_or_404()
 
    bank_name = request.json['bank_name']
    branch_name = request.json['branch_name']
    ifsc_code = request.json['ifsc_code']
    account_number = request.json['account_number']

    serviceprovider.bank_name = bank_name
    serviceprovider.branch_name = branch_name
    serviceprovider.ifsc_code = ifsc_code
    serviceprovider.account_number = account_number
 

    db.session.commit()
    return serviceprovider_schema.jsonify(serviceprovider)


@app.route("/discount/<emailid>", methods=["PUT"])
def discount_update(emailid):
    serviceprovider = ServiceProvider.query.filter_by(emailid=emailid).first_or_404()
 
    disc_general_service = request.json['disc_general_service']
    disc_roadside_assistance = request.json['disc_roadside_assistance']
    disc_maintenence_repair = request.json['disc_maintenence_repair']
    disc_dent_repairing = request.json['disc_dent_repairing']
    disc_car_wash = request.json['disc_car_wash']

    serviceprovider.disc_general_service = disc_general_service
    serviceprovider.disc_roadside_assistance = disc_roadside_assistance
    serviceprovider.disc_maintenence_repair = disc_maintenence_repair
    serviceprovider.disc_dent_repairing = disc_dent_repairing
    serviceprovider.disc_car_wash = disc_car_wash
 

    db.session.commit()
    return serviceprovider_schema.jsonify(serviceprovider)


@app.route("/dropdown/<emailid>", methods=["PUT"])
def dropdown_update(emailid):
    serviceprovider = ServiceProvider.query.filter_by(emailid=emailid).first_or_404()
 
    general_service = request.json['general_service']
    roadside_assistance = request.json['roadside_assistance']
    maintenence_repair = request.json['maintenence_repair']
    dent_repairing = request.json['dent_repairing']
    car_wash = request.json['car_wash']

    serviceprovider.general_service = general_service
    serviceprovider.roadside_assistance = roadside_assistance
    serviceprovider.maintenence_repair = maintenence_repair
    serviceprovider.dent_repairing = dent_repairing
    serviceprovider.car_wash = car_wash
 

    db.session.commit()
    return serviceprovider_schema.jsonify(serviceprovider)




