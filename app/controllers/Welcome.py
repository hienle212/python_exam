from system.core.controller import *
class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('Model')
    def index(self):
        return self.load_view('main.html')
    def main(self):
        quotes = self.models['Model'].show_quotes()
        return self.load_view('quote_page.html', quotes = quotes)
    def add_quote(self):
        self.models['Model'].add_quote(request.form)
        return redirect ('/main')
    def delete_quote(self):
        self.models['Model'].remove_quote(request.form)
        return redirect ('/main')
    def create_quote(self):
        quote = self.models['Model'].create_quote(request.form)
        if quote['status'] == True:
            return redirect('/main')
        else:
            for message in quote['errors']:
                flash(message)
            return redirect('/main')
    def quote_info(self,user_id):
        quote_info = self.models['Model'].quote_info(user_id)
        return self.load_view('quote_info.html', quote_info = quote_info)
    def register(self):
        user_info = self.models['Model'].register(request.form)
        if user_info['status'] == True:
            session['id'] = user_info['user']['id'] 
            session['name'] = user_info['user']['name']            
            return redirect('/main')
        else:
            for message in user_info['errors']:
                flash(message)
            return redirect('/')
    def login(self):
        login_info = self.models['Model'].login(request.form)
        if login_info['status'] == True:
            session['id'] = login_info['user']['id'] 
            session['name'] = login_info['user']['name']
            return redirect('/main')
        else:
            for message in login_info['errors']:
                flash(message)
            return redirect('/')
    def logoff(self):
        session.clear()
        return redirect('/')
