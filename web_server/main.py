import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4]

@app.get('/contact', response_class=HTMLResponse)
def get_contact():
    return """
    <h1>hello I'm a website</h1>
    <p>And I'm a paragraph</p>
    <p>This paragraph came from Docker!</p>
    """

def run():
    store.get_catgories()

if __name__ == '__main__':
    run()