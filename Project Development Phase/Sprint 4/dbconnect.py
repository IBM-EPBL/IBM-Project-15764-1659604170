import ibm_db
dsn_hostname = "55fbc997-9266-4331-afd3-888b05e734c0.bs2io90l08kqb1od8lcg.databases.appdomain.cloud" 
dsn_uid = "qjp14993"        
dsn_pwd = "kIfq04NKDM3zUnCd"     
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "bludb"            
dsn_port = "31929"               
dsn_protocol = "TCPIP"           
dsn_security = "SSL"              
dsn_cert="DigiCertGlobalRootCA.crt"
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};"
    "SSLServerCertificate={8};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security,dsn_cert)
try:
    conn = ibm_db.connect(dsn, "", "")
    print("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)
except:
    print("Unable to connect: ", ibm_db.conn_errormsg())
print(dsn)
