__author__ = 'srgtolm'

import ConfigParser

config = ConfigParser.RawConfigParser()

#config.add_section('Razdel_01')
#config.add_section('Razdel_02')
#config.set('Razdel_02','st','word')
#config.set('Razdel_01','nast','1986')
#config.set('Razdel_01','bool','True')

#with open('example.cfg','wb') as configfile:
#    config.write(configfile)

'And read config'

#config.read('example.cfg')
#nast = config.getint('Razdel_01','nast')
#bool = config.getboolean('Razdel_01', 'bool')
#st = config.get('Razdel_02','st')
#print nast
#print bool
#print st
#print config.defaults()
#print config.sections()
#print config.options('Razdel_01')
config.read('exm.cfg')
a = config.get("SectionTwo","favoritecolor")
print a
print config.sections()
print config.options('SectionOne')
print config.options('SectionTwo')