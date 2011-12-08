import os
import getpass
import ConfigParser

print "enter the database connection information:"

host = raw_input( "    host: " )
port = raw_input( "    port: " )
user = raw_input( "    user: " )
passw = getpass.getpass( "    passw: " )
name = raw_input( "    name: " )

config = ConfigParser.RawConfigParser()
config.add_section( 'database' )
config.set( 'database', 'host', host )
config.set( 'database', 'port', port )
config.set( 'database', 'user', user )
config.set( 'database', 'passw', passw )
config.set( 'database', 'name', name )

with open('./config/database.cfg', 'wb') as configfile:
    config.write(configfile)

print "setup complete."