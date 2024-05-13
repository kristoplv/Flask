from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import Koolitus, Tooted
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user



inject = Blueprint("inject", __name__)

injectable2 = {
    0:{
        "name":"fluffy dog",
        "data": "Karvane koer su karvasele koerale!",
        "qty": 10,
        "img":"../static/pictures/fluff.jpg",
        "tag": "toy"
    },
    1:{
        "name":"Kummist kont",
        "data": "Lase oma kutsul närida midagi su käe asemel!",
        "qty": 5,
        "img":"../static/pictures/rubber.jpg",
        "tag": "toy"
    },
    2:{
        "name":"Prääksu",
        "data": "Ära muretse, sul polegi öösel magada vaja!",
        "qty": 16,
        "img":"../static/pictures/quack.jpg",
        "tag": "toy"
    },
    3:{
        "name":"Burger",
        "data": "Maitseb nagu päris burger (ei maitse)",
        "qty": 100,
        "img":"../static/pictures/fluff.jpg",
        "tag": "toy"
    },
    4:{
        "name":"Carnilove Salmon&Turkey",
        "data": "Parim toit kutsikatele!",
        "qty": 1,
        "img":"../static/pictures/carni.png",
        "tag": "food"
    },
    5:{
        "name":"Maiused Carnilove",
        "data": "Carnilove maiused metssea maitsega.",
        "qty": 12,
        "img":"../static/pictures/boar.jpg",
        "tag": "food"
    },
    6:{
        "name":"Carnilove Täissööt",
        "data": "Carnilove täissööt põhjapõdra lihast täiskasvanud koertele",
        "qty": 5,
        "img":"../static/pictures/rein.jpg",
        "tag": "food"
    },
    7:{
        "name":"Punutud rihm",
        "data": "Parimast materjalist punutud rihm. 100% tõmbevastane!",
        "qty": 54,
        "img":"../static/pictures/rope.jpg",
        "tag": "misc"
    },

}



injectable = {
    0:{
        "name":"Sotsiaalne jalutamine",
        "data":"Sotsiaaljalutamise koolitus on oluline osa koera treenimisest ja tema heaolu tagamisest. Õpetades koerale korralikku jalutamiskäitumist, saab omanik luua tugeva sideme oma neljajalgse sõbraga ning tagada turvalise ja nauditava kogemuse nii endale kui ka koerale.",
        "when": "01.04.2024 - 01.06.2024",
        "img":"../static/pictures/sots.jpg"
    },
    1:{
        "name":"Baaskäskluste koolitus",
        "data":"Tere tulemast kergemate käskluste koolitusele koertele! See koolitus on loodud selleks, et õpetada teie neljajalgsele sõbrale olulisi ja kasulikke käsklusi, mis aitavad suhelda teie ja teie koera vahel ning luua tugevam side.",
        "when": "23.06.2024",
        "img":"../static/pictures/kask.png"
    },
    2:{
        "name":"Toitumine ja tervis",
        "data":"Koerte toitumine on oluline osa nende üldisest tervisest ja heaolust. Õige toitumine aitab säilitada teie koera energiataset, tugevdada immuunsüsteemi ning tagada tervisliku naha ja karvkatte. Oluline on valida kvaliteetne ja tasakaalustatud toit, mis vastab teie koera vanusele, suurusele, aktiivsuse tasemele ja tervislikule seisundile",
        "when": "28.07.2024",
        "img":"../static/pictures/toit.png"
    },
    3:{
        "name":"Koera kehakeel",
        "data":"Koerte kehakeel on nende peamine viis suhelda, nii omavahel kui ka inimestega. Õppides tundma ja mõistma erinevaid koerte kehakeele märke, saate paremini aru sellest, mida teie koer tunneb, soovib ja vajab.",
        "when": "17.05.2024",
        "img":"../static/pictures/kehakeel.png"
    }
}

@inject.route("/send")
def send():
    for i in range(len(injectable)):
        name1 = injectable[i]["name"]
        data1 = injectable[i]["data"]
        when1 = injectable[i]["when"]
        img1 = injectable[i]["img"]
        new_data = Koolitus(name=name1, data=data1, when=when1, img=img1)
        db.session.add(new_data)
        db.session.commit()
        print("worked")
    return render_template("send.html")

@inject.route("/send_item")
def sender():
    for i in range(len(injectable2)):
        name1 = injectable2[i]["name"]
        data1 = injectable2[i]["data"]
        qty1 = injectable2[i]["qty"]
        img1 = injectable2[i]["img"]
        tag1 = injectable2[i]["tag"]
        new_data = Tooted(name=name1, data=data1, qty=qty1, img=img1, tag=tag1)
        db.session.add(new_data)
        db.session.commit()
        print("worked")

    return render_template("send.html")
