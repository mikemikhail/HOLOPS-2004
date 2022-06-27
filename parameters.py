# change parameters here for target NETCONF server

from datetime import datetime

# target NETCONF server
server = '198.18.1.114'

logfile = 'get_config.log'
tracefile = 'get_config.trace.log'

cap_cnf_file = server + '-cap-cnf-' + str(datetime.now().strftime('%Y%m%d')) + '.xml'

user ='cisco'
password ='cisco'

