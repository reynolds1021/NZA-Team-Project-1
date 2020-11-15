from app import app, db
from app.models import User, CaseNotes




if __name__ == "__main__":
    app.run(debug=True)

@app.shell_context_processor
def maske_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
