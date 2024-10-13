from main.settings import DATABASE

class Tour(DATABASE.Model):

    id=DATABASE.Column(DATABASE.Integer(), primary_key=True)
    title=DATABASE.Column(DATABASE.String(255))
    date=DATABASE.Column(DATABASE.String(255))
    country=DATABASE.Column(DATABASE.String(255))
    price=DATABASE.Column(DATABASE.Integer())
    description=DATABASE.Column(DATABASE.TEXT)

    def __repr__(self) -> str:
        return 'title'