import marshmallow as ma


class TaskSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "title", "contents")
