#-*- coding:utf-8 -*-


class EnumElem(object):
    u'''
    列挙体の要素
    '''

    def __init__(self, enum, name):

        self.enum = enum
        self.name = name


    def __eq__(self, other):
        u'''
        同値性
        '''

        return self is other or self.enum is other.enum and self.name == other.name


    def __hash__(self):
        u'''
        set, dict で使えるように
        '''

        return id(self.enum) + hash(self.name)


    def __str__(self):

        return self.name



class Enum(object):
    u'''
    列挙体もどき
    '''

    def __init__(self, *names):

        self.__objs = set()

        for name in names:
            obj = EnumElem(self, name)
            setattr(self, name, obj)

            self.__objs.add(obj)


        self.__names = names


    def elements(self):
        u'''
        列挙体の中身をリスト
        '''

        return list(self)


    def __iter__(self):
        u'''
        列挙体の中身をイテレート
        '''

        for name in self.__names:

            yield getattr(self, name)


    def __contains__(self, elem):
        u'''
        列挙体に含まれるかどうか
        '''

        return elem in self.__objs


    def from_str(self, s):
        u'''
        文字列から列挙体の要素を取得
        '''

        obj = EnumElem(self, s)

        if obj in self.__objs:
            return getattr(self, s)

        raise AttributeError(s + ' is not contains in enum object')


