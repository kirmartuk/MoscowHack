import json
import enum

from flask import Flask, jsonify
from dataclasses import dataclass
from app import db

class AnimalPhoto(db.Model):
    __tablename__ = 'animal_photo'
    id = db.Column(db.Integer, primary_key=True)
    link_to_photo = db.Column(db.String(80), nullable=False)

    def get_all_photos():
        return AnimalPhoto.query.all()

    def get_photo(_id):
        return AnimalPhoto.query.filter_by(id=_id).first()

    def add_photo(_link):
        new_photo = AnimalPhoto(link_to_photo=_link)
        db.session.add(new_photo)
        try:
            db.session.commit()
        except DatabaseError:
            db.session.rollback()

    def delete_photo(_id):
        result = AnimalPhoto.query.filter_by(id=_id).delete()
        try:
            db.session.commit()
        except:
            db.session.rollback()
        return bool(result)

    def update_photo(_id, _link):
        AnimalPhoto.query.filter_by(id=_id).first().link_to_photo = _link
        try:
            db.session.commit()
        except:
            db.session.rollback()

    def __repr__(self):
        return "item with id{0} ".format(self.id)

class AnimalType(db.Model):
    __tablename__ = 'animal_type'
    id = db.Column(db.Integer, primary_key=True)
    atype = db.Column(db.String(15), index=True, nullable=False)

    def get_all_types():
        return AnimalType.query.all()

    def get_type(_id):
        return AnimalType.query.filter_by(id=_id).first()

    def get_id_by_type(_atype):
        return AnimalType.query.filter_by(atype=_atype).first().id

    def add_type(_type):
        new_type = AnimalType(atype=_type)
        db.session.add(new_type)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def delete_type(_id):
        result = AnimalType.query.filter_by(id=_id).delete()
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return bool(result)

    def update_type(_id, _type):
        AnimalType.query.filter_by(id=_id).first().atype = _type
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def __repr__(self):
        return "item with id {0} has type {1}".format(self.id, self.atype)

@dataclass
class AnimalBreed(db.Model):
    id: int
    breed: str
    animal_type: str
    
    __tablename__ = 'animal_breed'
    id = db.Column(db.Integer, primary_key=True)
    breed = db.Column(db.String(48), nullable=False)
    animal_type = db.Column(db.Integer, db.ForeignKey('animal_type.id'), nullable=False)

    def get_all_breeds():
        return AnimalBreed.query.all()

    def get_breed(_id):
        return AnimalBreed.query.filter_by(id=_id).first()

    def get_id_by_breed(_breed):
        return AnimalBreed.query.filter_by(breed=_breed).first().id

    def add_breed(_breed, _animal_type):
        new_breed = AnimalBreed(breed=_breed, animal_type=_animal_type)
        db.session.add(new_breed)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def delete_breed(_id):
        result = AnimalBreed.query.filter_by(id=_id).delete()
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return bool(result)

    def update_breed(_id, _breed, _animal_type):
        animal = AnimalBreed.query.filter_by(id=_id).first()
        animal.breed = _breed
        animal.animal_type = _animal_type
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def __repr__(self):
        return "item with id{0} ".format(self.id)

@dataclass
class Shelter(db.Model):
    id: int
    address: str
    daddy: str
    director: str
    cares: str
    name: str
    submission: str
    phone: str
    
    __tablename__ = 'shelter'
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(127), index=True)
    daddy = db.Column(db.String(127), index=True)
    director = db.Column(db.String(63), index=True)
    cares = db.Column(db.String(63), index=True)
    name = db.Column(db.String(63), index=True)
    submission = db.Column(db.String(127), index=True)
    phone = db.Column(db.String(31), index=True)

    def get_all_shelters():
        return Shelter.query.all()

    def get_by_id(_id):
        return Shelter.query.filter_by(id=_id).first()

    def get_id_by_address(_address):
        return Shelter.query.filter_by(address=_address).first().id

    def get_id_by_name(_name):
        return Shelter.query.filter_by(name=_name).first().id

    def set_shelters(shelters):        
        for sh in shelters["shelters"]:
            print(sh)
            new_shelter = Shelter(address=sh['address'], name=sh['shortName'], submission=sh['subortination'], phone=sh['phoneNumber'])
            db.session.add(new_shelter)
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
    
    def add_json(sh):
        new_shelter = Shelter(address=sh.address, name=sh.shortName, submission=sh.subortination, phone=sh.phoneNumber)
        db.session.add(new_shelter)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def add_shelter(_address, _daddy, _director, _cares):
        new_shelter = Shelter(name=_name, daddy=_daddy, director=_director, cares=_cares)
        db.session.add(new_shelter)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def delete_shelter(_id):
        result = Shelter.query.filter_by(id=_id).delete()
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return bool(result)

@dataclass
class Animal(db.Model):
    id: int
    idcard: str
    age: int
    weight: int
    nickname: str
    male: int
    special_signs: str
    character: str
    animal_type: int
    animal_breed: int
    shelter: int
    color: str
    fur: str
    ears: str
    tail: str
    size: str
    cell: int
    idmark: str
    sterilized: str
    veterinarian: str
    ready: int
    
    __tablename__ = 'animal'
    id = db.Column(db.Integer, primary_key=True)
    idcard = db.Column(db.String(15), index=True, nullable=False)
    age = db.Column(db.String(63), index=True, nullable=False)
    weight = db.Column(db.Integer, index=True, nullable=False)
    nickname = db.Column(db.String(45), index=True, nullable=False)
    male = db.Column(db.Integer, index=True, nullable=False)
    special_signs = db.Column(db.String(250))
    character = db.Column(db.String(45))
    animal_type = db.Column(db.Integer, db.ForeignKey('animal_type.id'), nullable=False)
    animal_breed = db.Column(db.Integer, db.ForeignKey('animal_breed.id'), nullable=False)
    shelter = db.Column(db.Integer, db.ForeignKey('shelter.id'), nullable=False)
    color = db.Column(db.String(31), index=True, nullable=False)
    fur = db.Column(db.String(15), index=True, nullable=False)
    ears = db.Column(db.String(15), index=True, nullable=False)
    tail = db.Column(db.String(15), index=True, nullable=False)
    size = db.Column(db.String(15), index=True, nullable=False)
    cell = db.Column(db.Integer, index=True, nullable=False)
    idmark = db.Column(db.String(31), index=True, nullable=False)
    sterilized = db.Column(db.String(63), index=True, nullable=False)
    veterinarian = db.Column(db.String(63), index=True, nullable=False)
    ready = db.Column(db.Integer, index=True, nullable=False)

    def get_all():
        return Animal.query.all()

    def filter(limit, offset, filters = {}):
        query = db.session.query(Animal)
        for attr, value in filters.items():
            try:
                query = query.filter(getattr(Animal, attr) == value)
            except:
                pass
        count = len(query.all())
        query = query.limit(limit)
        query = query.offset(offset)
        return query.all(), count

    def get_socialized(limit, offset, filters = {}):
        query = db.session.query(Animal)
        filters['ready'] = 1
        for attr, value in filters.items():
            try:
                query = query.filter(getattr(Animal, attr) == value)
            except:
                pass
        count = len(query.all())
        query = query.limit(limit)
        query = query.offset(offset)
        return query.all(), count

    def get_by_id(_id):
        return Animal.query.filter_by(id=_id).first()

    def add_animal(_idcard, _age, _weight, _nickname, _male, _special_signs, _character, _animal_type, _animal_breed, _shelter, _color, _fur, _ears, _tail, _size, _cell, _idmark, _sterilized, _veterinarian, _ready):
        new_animal = Animal(idcard=_idcard, age=_age, weight=_weight,  nickname=_nickname, male=_male, special_signs=_special_signs, character=_character, animal_type=_animal_type, animal_breed=_animal_breed, shelter=_shelter, color=_color, fur=_fur, ears=_ears, tail=_tail, size=_size, cell=_cell, idmark=_idmark, sterilized=_sterilized, veterinarian=_veterinarian, ready=_ready)
        db.session.add(new_animal)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def add_json(an):
        if an['sex'] == "Мужской":
            an['male'] = 1
        else:
            an['male'] = 0
        new_animal = Animal(idcard=an['cardId'], age=an['age'], weight=an['weight'], nickname=an['nickname'], male=an['male'], special_signs=an['specialSigns'], character=an['character'], animal_type=an['animal_type'], animal_breed=an['animal_breed'], shelter=an['shelter'], color=an['color'], fur=an['wool'], ears=an['ears'], tail=an['tail'], size=an['size'], cell=an['cell'], idmark=an['idMarker'], sterilized=an['sterilized'], veterinarian=an['veterinarian'], ready=an['readyToPickUp'])
        db.session.add(new_animal)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def delete(_id):
        result = Animal.query.filter_by(id=_id).delete()
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return bool(result)

    def update_json(_id, an):
        if an['sex'] == "Мужской":
            an['male'] = 1
        else:
            an['male'] = 0
        new_animal = Animal(idcard=an['cardId'], age=an['age'], weight=an['weight'], nickname=an['nickname'], male=an['male'], special_signs=an['specialSigns'], character=an['character'], animal_type=an['animalType'], animal_breed=an['animalBreed'], shelter=an['shelter'], color=an['color'], fur=an['wool'], ears=an['ears'], tail=an['tail'], size=an['size'], cell=an['cell'], idmark=an['idMarker'], sterilized=an['sterilized'], veterinarian=an['veterinarian'], ready=an['readyToPickUp'])
        to_replace = Animal.query.filter_by(id=_id).first()
        to_replace = new_animal
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def update(_id, _idcard, _age, _weight, _nickname, _male, _special_signs, _character, _animal_type, _animal_breed, _shelter, _color, _fur, _ears, _tail, _size, _cell, _idmark, _sterilized, _veterinarian, _ready):
        new_animal = Animal.query.filter_by(id=_id).first()
        new_animal.idcard=_idcard
        new_animal.age=_age
        new_animal.weight=_wight
        new_animal.nickname=_nickname
        new_animal.male=_male
        new_animal.special_signs=_special_signs
        new_animal.character=_character
        new_animal.animal_type=_animal_type
        new_animal.animal_breed=_animal_breed
        new_animal.shelter=_shelter
        new_animal.color=_color
        new_animal.fur=_fur
        new_animal.ears=_ears
        new_animal.tail=_tail
        new_animal.size=_size
        new_animal.cell=_cell
        new_animal.idmark=_idmark
        new_animal.sterilized=_sterilized
        new_animal.veterinarian=_veterinarian
        new_animal.ready=_ready
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

@dataclass
class History(db.Model):
    id: int
    title: str
    body: str
    date: str
    doc: str
    animal: int
    
    __tablename__ = 'history'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(63), index=True)
    body = db.Column(db.String(1023))
    date = db.Column(db.String(31), index=True)
    doc = db.Column(db.String(511))
    animal = db.Column(db.Integer, db.ForeignKey('animal.id'), index=True)

    def get_by_id(_id):
        return History.query.filter_by(id=_id).first()

    def get_events_for(_animal):
        return History.query.filter_by(animal=_animal).all()

    def add(an):
        new_event = History(title=an['title'], body=an['body'], date=an['date'], doc=an['doc'], animal=an['animalId'])
        db.session.add(new_event)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(31), nullable=False)

    def add_role(_role):
        new_role = Role(role=_role)
        db.session.add(new_role)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def __repr__(self):
        return "role {0}".format(self.role)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(45), index=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(45), index=True, nullable=False)
    surname = db.Column(db.String(45), index=True, nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('role.id'), index=True)
    shelter = db.Column(db.Integer, db.ForeignKey('shelter.id'), nullable=False)

    def get_all_users():
        return User.query.all()

    def get_user(_id):
        return User.query.filter_by(id=_id).first()

    def add_user(_login, _password, _name, _surname, _role, _shelter):
        new_user = User(login=_login, password=_password, name=_name, surname=_surname, role=_role, shelter=_shelter)
        db.session.add(new_user)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def delete_user(_id):
        result = User.query.filter_by(id=_id).delete()
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return bool(result)

@dataclass
class PetRequest(db.Model):
    id: int
    name: str
    phone: str
    comment: str
    animal: str
    
    __tablename__ = 'pet_request'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), index=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    comment = db.Column(db.String(250), nullable=False)
    animal = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)

    def get_all_requests():
        return PetRequest.query.all()

    def get_request(_id):
        return PetRequest.query.filter_by(id=_id).first()

    def add_json(re):
        new_request = PetRequest(name=re['name'], phone=re['phone'], comment=re['comment'], animal=re['animal'])
        db.session.add(new_request)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def add_request(_name, _phone, _comment, _animal):
        new_request = PetRequest(name=_name, phone=_phone, comment=_comment, animal=_animal)
        db.session.add(new_request)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def delete_request(_id):
        result = PetRequest.query.filter_by(id=_id).delete()
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return bool(result)

class Catching(db.Model):
    __tablename__ = 'catching'
    id = db.Column(db.Integer, primary_key=True)
    act = db.Column(db.String(63), index=True, nullable=False)
    date = db.Column(db.DateTime, index=True, nullable=False)
    district = db.Column(db.String(31), index=True, nullable=False)
    act1 = db.Column(db.String(63), index=True, nullable=False)
    address = db.Column(db.String(127), index=True, nullable=False)
    animal = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)

class Moving(db.Model):
    __tablename__ = 'moving'
    id = db.Column(db.Integer, primary_key=True)
    act = db.Column(db.String(63), index=True, nullable=False)
    date = db.Column(db.String(31), index=True, nullable=False)
    reason = db.Column(db.String(63), index=True, nullable=False)
    contract = db.Column(db.String(63), index=True, nullable=False)
    animal = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)

class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    yurik = db.Column(db.String(511), nullable=False)
    fizik = db.Column(db.String(511), nullable=False)
    fio = db.Column(db.String(61), nullable=False)
    animal = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)

class DocumentType(db.Model):
    __tablename__ = 'document_type'
    id = db.Column(db.Integer, primary_key=True)
    dtype = db.Column(db.String(31), nullable=False)

    def add_doc_type(_dtype):
        new_doc_type = DocumentType(dtype=_dtype)
        db.session.add(new_doc_type)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

class Document(db.Model):
    __tablename__ = 'document'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True, nullable=False)
    link_to_document = db.Column(db.String(2000), nullable=False)
    animal = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)
    document_type = db.Column(db.Integer, db.ForeignKey('document_type.id'), nullable=False)

    def get_all_document():
        return Document.query.all()

    def get_document(_id):
        return Document.query.filter_by(id=_id).first()

    def add_document(_date, _link_to_document, _animal, _document_type):
        new_document = Document(date=_date, link_to_document=_link_to_document, animal=_animal, document_type=_document_type)
        db.session.add(new_animal)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def delete_document(_id):
        result = Document.query.filter_by(id=_id).delete()
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return bool(result)

    def __repr__(self):
        return "item with id{0} ".format(self.id)
