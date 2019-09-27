from google.cloud import ndb

NOT_SET = 'NOT SET'


class Settings(ndb.Model):
    name = ndb.StringProperty()
    value = ndb.StringProperty()

    @classmethod
    def get(cls, name):
        entity = cls.query(Settings.name == name).get()

        if entity is None:
            entity = cls()
            entity.name = name
            entity.value = NOT_SET
            entity.put()

        if entity.value == NOT_SET:
            raise ValueError(name)

        return entity.value
