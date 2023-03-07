from flask import Blueprint, render_template,session,redirect,url_for,flash,request,jsonify
import uuid
import json
from models import storage
from models.user import User
from models.service_category import ServiceCategory
from models.service_request import ServiceRequest
from models.town import Town
from models.region import Region
from models.notification import Notification

views = Blueprint('views',__name__)


@views.route('/home',strict_slashes=False)
@views.route('/home/<string:id>',strict_slashes=False,methods=['GET','POST'])
def home(id=None):

    users = storage.all('User').values()
    #print(users)

    regions = storage.all(Region).values()
    regions = sorted(regions, key=lambda k:k.name)
    region_town=[]

    for region in regions:
        region_town.append([region, sorted(region.towns, key=lambda k: k.name)])

    categories = storage.all(ServiceCategory).values()
    categories = sorted(categories, key=lambda k:k.category_name)
    #print(categories)

    notifications = storage.all(Notification)
    my_notifications = []
    noti_count = 0

    if not session:
        noti_count = 0
    else:
        for note in notifications.values():
            if note.user_id == session['userId'] and note.read_status == "unread":
                my_notifications.append(note.text)
                noti_count += 1

        session['numnotis'] = noti_count

    return render_template('home.html',cache_id=uuid.uuid4(),
                           users=users,
                           noti = my_notifications,
                           regions=region_town,
                           nc = noti_count,
                           categories=categories)


@views.route('/profile_view/<string:id>',strict_slashes=False)
def profile_view(id):
    if not id:
        return
    else:
        user = storage.get(User,id)

        return render_template('view_profile.html',user=user,
                           cache_id=uuid.uuid4())                                             


@views.route('/edit_profile/<string:id>',strict_slashes=False,methods=['GET','POST','PUT'])
def profile_edit(id):
    
    user = storage.get(User,id)

    if request.method == 'POST' and 'save' in request.form:
        name = request.form.get('full_name')
        username = request.form.get('username')
        # email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmpassword')
        phone = request.form.get('phone')
        avatar = request.form.get('dp')
        address = request.form.get('address')
        town = request.form.get('town')
        region = request.form.get('region')
        skill = request.form.get('skill')
        gender = request.form.get('gender')
        bio = request.form.get('about')
        longitude = request.form.get('longitude')
        latitude = request.form.get('latitude')
        country = request.form.get('country')

        if password != confirm_password:
            flash("Your passwords do not match!",category="error")
        else:
            ignore = ['id', 'email', 'created_at', 'updated_at']

            edited_user = User(full_name=name,user_name=username,password=password,phone=phone,dp=avatar,
                               adress=address,town=town,region=region,skill=skill,gender=gender,about=bio,
                               longitude=longitude,latitude=latitude,country=country)
            
            data = edited_user.to_dict()
            for key, value in data.items():
                if key not in ignore:
                    try:
                        setattr(user, key, value)
                    except Exception:
                        pass
                    finally:
                        storage.save()
            return redirect(f'/profile_user/{user.id}')
        

    if not id:
        flash('You have to login first',category='error')
        return redirect('/auth.login')
    else:
        return render_template('edit_profile.html',user=user,
                           cache_id=uuid.uuid4())                                             


#@views.route('/profile_user',strict_slashes=False)
@views.route('/profile_user/<string:id>',strict_slashes=False)
def profile_user(id=None):
    if id == None:
        return redirect(url_for('/auth/login'),200)
    else:
        user = storage.get(User,id)

        notifications = storage.all(Notification)
        my_notifications = []
        noti_count = 0

        if not session:
            noti_count = 0
        else:
            for note in notifications.values():
                if note.user_id == session['userId'] and note.read_status == "unread":
                    my_notifications.append(note.text)
                    noti_count += 1
    
        return render_template('user_profile.html',user=user,
                               notis = my_notifications,
                           cache_id=uuid.uuid4())
    

@views.route('/request_service/<string:id>',strict_slashes=False, methods=['GET','POST'])
def request_service(id):
    
    if session['userId'] == "" or session['userId'] == None:
        flash('Kindly login first!')
        return redirect(url_for('auth.login'),200)
    else:
        provider= storage.get(User,id)
        consumer= storage.get(User,session['userId'])
        status = "initiated"

        return render_template('request.html',providerDict=provider,
                            consumerDict=consumer,
                            data=status,
                           cache_id=uuid.uuid4())


@views.route('/accept_request/<string:id>',strict_slashes=False, methods=['GET','POST'])
def accept_request(id):
    request_data = storage.get(ServiceRequest,id)
    provider= storage.get(User,request_data.provider_id)
    consumer= storage.get(User,session['userId'])

    # accept = ServiceCategory()
    # data = accept.to_dict()
    # setattr(data, "status","accepted")
    # storage.save()
    
    return render_template('accept_request.html',providerDict=provider,
                           consumerDict=consumer,
                           requestDict =request_data,
                           cache_id=uuid.uuid4())


@views.route('/decline_request/<string:id>',strict_slashes=False, methods=['GET','POST'])
def decline_request(id):

    return render_template('decline_request.html',providerId=id,
                           cache_id=uuid.uuid4())


@views.route('/our_story',strict_slashes=False)
def our_story():
    return render_template('about_us.html',cache_id=uuid.uuid4())


@views.route('/meet_the_team',strict_slashes=False)
def the_team():
    return render_template('the_team.html',cache_id=uuid.uuid4())


@views.route('/confirm_request',strict_slashes=False,methods=['GET','POST'])
def confirm_req():
    pid = request.args.get('provider')
    cid = request.args.get('consumer')
    stat = request.args.get('stat')

    write_confirm = ServiceRequest(provider_id=pid,consumer_id=cid,status=stat)
    # flash('Request made Successfully',category="success")
    request_id = write_confirm.id
    storage.new(write_confirm)
    storage.save()

    notify_consumer = Notification(read_status = "unread",user_id=cid,text=f'You made a request: <a href="/profile_view/{pid}">View</a>',other_data=request_id)
    storage.new(notify_consumer)
    storage.save()

    url = f"'/accept_request/{request_id}'"

    notify_provider = Notification(read_status = "unread",user_id=pid,text=f'You have a request:<a href="javascript:newPopup({ url });">Accept Service Request</a>',other_data=request_id)
    storage.new(notify_provider)
    storage.save() 

    return redirect('/success')

@views.route('/edit_request',strict_slashes=False,methods=['GET','POST'])
def edit_req():
    pid = request.args.get('provider')
    cid = request.args.get('consumer')
    rid = request.args.get('request')
    nid = request.args.get('notification')
    stat = request.args.get('stat')

    accept = storage.get(ServiceRequest,rid)
    p_user = storage.get(User,pid)


    notifications = storage.all(Notification)
    for note in notifications.values():
                if note.other_data == rid and note.read_status == "unread":
                    accept = ServiceRequest()
                    data = accept.to_dict()
                    #setattr(data, "status","accepted")
                    #data['status'] = "accepted"
                    #storage.save()
                        
                    notify_consumer = Notification(read_status = "unread",user_id=cid,text=f'{p_user.user_name} accepted your request: <a href=""><i class="fal fa-window-close"></i></a>',other_data=cid)
                    storage.new(notify_consumer)
                    storage.save()                    

    return redirect('/success')


@views.route('/success',strict_slashes=False)
def success():
    return render_template('success.html',cache_id=uuid.uuid4())


@views.route('/search',strict_slashes=False,methods=['GET','POST'])
def filter_users():
    users = storage.all(User)

    town = request.args.get('town')
    ser = request.args.get('service')

    filtered_users = []

    for user in users.values():
        # if town == None and ser.lower() == user.skill.lower():
        #     filtered_users.append(user.to_dict())
        # elif ser == None and town == None and ser.lower():
        #     filtered_users.append(user.to_dict())
        # elif town.lower() == user.town.lower() and ser.lower() == user.skill.lower():
        #     filtered_users.append(user.to_dict())
        if town is None:
            if ser.lower() == user.skill.lower():
                filtered_users.append(user.to_dict())
        elif ser is None:
            if town.lower() == user.town.lower():
                filtered_users.append(user.to_dict())
        else:
            if town.lower() == user.town.lower() and ser.lower() == user.skill.lower():
                filtered_users.append(user.to_dict())

    return jsonify(filtered_users)

