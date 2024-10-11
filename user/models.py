from main.settings import DATABASE

class User(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer(), primary_key = True)
    email = DATABASE.Column(DATABASE.String(255))
    password = DATABASE.Column(DATABASE.String(20))

    def __repr__(self) -> str:
        return f"id: {self.id}"