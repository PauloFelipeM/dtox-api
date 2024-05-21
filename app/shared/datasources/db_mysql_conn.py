import mysql
from sqlalchemy import create_engine

from ..config import config

mysql_engine = create_engine('mysql+mysqlconnector://'+config['DB']['MYSQL']['USERNAME']+':'+config['DB']['MYSQL']['PASSWORD']+'@'+config['DB']['MYSQL']['HOST']+':'+config['DB']['MYSQL']['PORT']+'/'+config['DB']['MYSQL']['DATABASE'])