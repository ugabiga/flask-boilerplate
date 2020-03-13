import marshmallow as ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "nickname")
