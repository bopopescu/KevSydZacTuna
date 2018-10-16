import mysql.connector
from scraper import ReadDoc


def scrape_date():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="fuckthis",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    # Creates a new table in the current database
    '''
    mycursor.execute("CREATE TABLE kevin_experience ("
                     "organization VARCHAR(255), "
                     "location VARCHAR(255),"
                     "position VARCHAR(255), "
                     "dates VARCHAR(255), "
                     "bullet1 TEXT, "
                     "bullet2 TEXT, "
                     "bullet3 TEXT)")
    '''
    '''
    mycursor.execute("SHOW TABLES")

    # mycursor.execute("ALTER TABLE kevin_experience ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

    # Inserts data into the table pulling from the data collected collected from my resume and
    # organized by methods in ReadDoc.
    sql = "INSERT INTO kevin_experience (organization, location, position_, dates, bullet1, bullet2) VALUES (%s, %s, %s, %s, %s, %s)"
    val = ReadDoc.get_leadership_experience('scraper/gardnerkevinresume.docx')[0]
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    '''
    # Prints out every row in the table

    mycursor.execute("SELECT * FROM kevin_experience")
    myresult = mycursor.fetchall()

    for x in myresult:
        mycursor.close()
        return x

    '''
    search_string = ('%Present%',)
    sql = "SELECT * FROM kevin_experience WHERE dates LIKE %s"

    mycursor.execute(sql, search_string)
    myresult = mycursor.fetchall()
    
    for x in myresult:
        return x
    
    for x in myresult:
        print(x)
    '''