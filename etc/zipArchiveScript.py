import zipfile
import sys
import os
import logging

logging.basicConfig(filename='file_ex.log', level = logging.DEBUG)

logging.info("checking to see if the backup.zip file exists")

if os.path.exists("backup.zip"):
        logging.info("it exists")
        try:
                zip_file = zipfile.ZipFile('backup.zip', 'a')
        except:
                err = sys.exc_info()
                logging.error("Unable to open backup.zip in append mode")
                logging.error("Error Num: " + str(error[1].args[0]))
                logging.error("Error Msg: " + err[1].args[1])
                sys.exit()
else:
        logging.info("creating backup.zip")
        try:
                zip_file = zipfile.ZipFile('backup.zip', 'w')
        except:
                err = sys.exc_info()
                logging.error("Unable to create backup.zip")
                logging.error("Error Num: " + str(error[1].args[0]))
                logging.error("Error Msg: " + err[1].args[1])
                sys.exit()

logging.info("adding test.txt to backup.zip")
try:
        zip_file.write('test.txt', 'test.txt', zipfile.ZIP_DEFLATED)

except:
        err = sys.exc_info()
        logging.error("Unable to create backup.zip in append mode")
        logging.error("Error Num: " + str(error[1].args[0]))
        logging.error("Error Msg: " + err[1].args[1])

zip_file.close()