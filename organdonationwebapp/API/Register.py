
import organdonationwebapp.API.UserTypeFactory as factory

class Register(object):
    def __init__(self,registerJson, logger,certificate=None, usertype= None):
        self.certificate = certificate
        self.usertype = usertype
        self.json = registerJson
        self.logger = logger


    def registerEntity(self):
        objectFactory = factory.UserTypeFactory(self.json,self.logger,self.certificate, self.usertype)
        inst = objectFactory.createObject()
        valid, url = inst.register()
        return valid, url