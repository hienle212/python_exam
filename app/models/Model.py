from system.core.model import *
import re  

class Model(Model):
    def __init__(self):
        super(Model, self).__init__()
    def register(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')
        errors = []
        if len(info['name']) < 2 or not info['name'].isalpha():
            errors.append("Invalid Name. (Letters only, at least 2 characters.)")
        if len(info['alias']) < 2 or not info['alias'].isalpha():
            errors.append("Invalid alias. (Letters only, at least 2 characters.)")
        if len(info['email']) < 1 or not EMAIL_REGEX.match(info['email']):
            errors.append ("Invalid Email Address!")    
        if len(info['password']) < 8 :
            errors.append("Password should be more than 8 characters")
        if info['password'] != info['confirm_password']:
            errors.append('Password and confirm password must match!')
        if PASSWORD_REGEX.match(info['confirm_password']):
            errors.append("Password requires to have at least 1 uppercase letter and 1 numeric value ")   
        if errors:
            return {"status":False, "errors":errors}            
        else: 
            query = "INSERT INTO users (name, alias, email, password, birthday, created_at, updated_at) VALUES (:name, :alias, :email,  :pw_hash,:birthday, NOW(), NOW())" 
            data = {'name' : info['name'],'alias' : info['alias'],'email' : info['email'],'pw_hash' : self.bcrypt.generate_password_hash(info['password']),'birthday' : info['birthday']}
            self.db.query_db(query, data)
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return {"status": True, "user": users[0]}
    def login(self,info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        PASSWORD_REGEX = re.compile(r'^([^0-9]*|[^A-Z]*)$')
        errors = []
        if len(info['email']) < 1 or not EMAIL_REGEX.match(info['email']):
            errors.append ("Invalid Email Address!")    
        if len(info['password']) < 8 :
            errors.append("Password should be more than 8 characters")
        if errors:
            return {"status":False, "errors":errors}            
        else:  
            query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            data = {'email' : info['email']}
            users = self.db.query_db(query,data) 
            return {"status": True, "user": users[0]}
    def show_quotes(self):
        query = "select favorite_quote.user_id as favorite_userid, users.name as name, quote, quote_by, quotes.id as quotes_id, users_id as poster_id from quotes left join favorite_quote on favorite_quote.quote_id = quotes.id left join users on users.id = quotes.users_id"
        return self.db.query_db(query)
    def add_quote(self, info):
        query = "insert into favorite_quote (user_id, quote_id ) values (:user_id, :quote_id)"
        data = {'user_id' : info['user_id'], 'quote_id' : info['quote_id']}
        return self.db.query_db(query,data)
    def remove_quote(self, info):
        query = "DELETE FROM favorite_quote WHERE user_id = :user_id AND quote_id =:quote_id"
        data = {'user_id' : info['user_id'], 'quote_id' : info['quote_id']}
        return self.db.query_db(query,data)
    def create_quote(self,info):
        errors = []
        if len(info['quote_by']) < 3 :
            errors.append("Quoted by must be more than 3 characters. ")
        if len(info['quote']) < 10 :
            errors.append("Quote must be more than 10 characters. ")
        if errors:
            return {"status":False, "errors":errors}            
        else:      
            query = "insert into quotes (quote, quote_by, created_at, updated_at,users_id ) values (:quote, :quote_by, NOW(),NOW(), :users_id)"
            data = {'quote' : info['quote'], 'quote_by' : info['quote_by'],'users_id' : info['users_id']}
            self.db.query_db(query,data)
            return {"status": True}

    def quote_info(self, user_id):
        query = "select users.name as name, count(quotes.id) as count ,quote, quote_by from quotes left join users on users.id = quotes.users_id where users_id = :user_id"
        data = {'user_id' : user_id}
        return self.db.query_db(query,data)











