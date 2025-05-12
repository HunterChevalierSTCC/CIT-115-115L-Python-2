
import sqlite3


conn = sqlite3.connect('retirement.db')
cursor = conn.cursor()

# Drop tables if they exist
cursor.execute('DROP TABLE IF EXISTS Employee')
cursor.execute('DROP TABLE IF EXISTS Pay')
cursor.execute('DROP TABLE IF EXISTS SocialSecurityMin')

# Create tables
cursor.execute('''
    CREATE TABLE Employee (
        EmployeeID INTEGER PRIMARY KEY,
        Name TEXT
    )
''')
cursor.execute('''
    CREATE TABLE Pay (
        EmployeeID INTEGER,
        Year INTEGER,
        Earnings REAL
    )
''')
cursor.execute('''
    CREATE TABLE SocialSecurityMin (
        Year INTEGER PRIMARY KEY,
        Minimum REAL
    )
''')

# Import Employee.txt
with open('Employee.txt', 'r') as f:
    next(f, None)  # skip header
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 2:
            cursor.execute('INSERT INTO Employee (EmployeeID, Name) VALUES (?, ?)', (int(parts[0]), parts[1]))

# Import Pay.txt
with open('Pay.txt', 'r') as f:
    next(f, None)
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 3:
            cursor.execute('INSERT INTO Pay (EmployeeID, Year, Earnings) VALUES (?, ?, ?)', (int(parts[0]), int(parts[1]), float(parts[2])))

# Import SocialSecurityMinimum.txt
with open('SocialSecurityMinimum.txt', 'r') as f:
    next(f, None)
    for line in f:
        parts = line.strip().split(',')
        if len(parts) == 2:
            cursor.execute('INSERT INTO SocialSecurityMin (Year, Minimum) VALUES (?, ?)', (int(parts[0]), float(parts[1])))

conn.commit()



query = '''
SELECT Employee.Name, Pay.Year, Pay.Earnings, SocialSecurityMin.Minimum
FROM Employee
JOIN Pay ON Employee.EmployeeID = Pay.EmployeeID
JOIN SocialSecurityMin ON Pay.Year = SocialSecurityMin.Year
ORDER BY Employee.Name, Pay.Year
'''

cursor.execute(query)
results = cursor.fetchall()

print(f"{'Name':<20} {'Year':<6} {'Earnings':<10} {'Minimum':<10} {'Include'}")


for name, year, earnings, minimum in results:
    include = "Yes" if earnings >= minimum else "No"
    print(f"{name:<20} {year:<6} {earnings:<10.2f} {minimum:<10.2f} {include}")

conn.close()
