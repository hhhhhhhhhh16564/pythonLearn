class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntergerField(Field):
    def __init__(self, name):
        super(IntergerField, self).__init__(name, 'bigint')

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name =='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found mapping: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v
                print('Found mapping:%s  ==>  %s' % (k,v ))
        for k in mappings.keys():
            attrs.pop(k)
        #保存属性和列的映射关系
        attrs['__mappings__'] = mappings
        #假设表名和类名一致
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, key):
        try:
            return  self[key]
        except KeyError:
            return AttributeError(r" 'Model' object has no attribute '%s' " % key)
    def __setattr__(self, key, value):
        self[key] = value
    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mappings__.items():
            #字段名
            fields.append(v.name)
            params.append('?')

            #获得字段的值
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ', '.join(fields), ','.join(params))
        print('SQL:  %s' % sql)
        print('ARGS: %s' % str(args))


class User(Model):
    id = IntergerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')
u = User(id = 12345, name = 'Michael', email = 'test.org', password= 'my-pwd')
u.save()

