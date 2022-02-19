#Program Perpustakaan untuk Peminjaman Buku

program = True

dataBuku = {
    'A1': {
        'Title' : 'Wolf Hall',
        'Author' : 'Hilary Mantel',
        'Year' : '2009',
        'Genre' : 'History Fiction',
        'Status' : 'Available'
    },
    'B1': {
        'Title' : 'Gilead',
        'Author' : 'Marilynne Robinson',
        'Year' : '2004',
        'Genre' : 'Novel',
        'Status' : 'Avalaible'
    },
    'A2': {
        'Title' : 'Never Let Me Go',
        'Author' : 'Kazuo Ishiguro',
        'Year' : '2005',
        'Genre' : 'Science Fiction',
        'Status' : 'Available'
    },
}

def tampilkanData():
    if(len(dataBuku)!=0 or len(dataBuku)<0):
        print ('Book List')
        nomer = 1
        for i in dataBuku :
            print (f"{nomer}. Code: {i}, Title: {dataBuku[i]['Title']}, Author: {dataBuku[i]['Author']}, Year: {dataBuku[i]['Year']}, Genre: {dataBuku[i]['Genre']}, Status: {dataBuku[i]['Status']}")
            nomer+=1               
    else:
        print("****No Data****")

def tampilkanDataPilihan():
    inputKode = input("Input Book Code: ")
    print (f"Book Data with Code: {inputKode}")

    if(inputKode in dataBuku):
        print (f"Code: {inputKode}, Title: {dataBuku[inputKode]['Title']}, Author: {dataBuku[inputKode]['Author']}, Year: {dataBuku[inputKode]['Year']}, Genre: {dataBuku[inputKode]['Genre']}, Status: {dataBuku[inputKode]['Status']}")  
    else:
        print("****No Book Data****")

def createData():
    inputKode = input("Input Book Code: ")

    if(inputKode in dataBuku):
        print("Data Already Exist")
    else:
        inputJudul= input("Input Title: ")
        inputPenulis= input("Input Author: ")
        inputTahun= input("Input Year: ")
        inputJenis= input("Input Genre: ")

        dataTambah = {
            inputKode : { 
                'Title': inputJudul,
                'Author': inputPenulis,
                'Year' : inputTahun,
                'Genre' : inputJenis,
                'Status' : 'Available'
            }
        }

        while(True):    
            inputConf = input("Will the Data be Saved? (Y/N): ")
            inputConf = inputConf.upper()
                        
            if(inputConf=='Y'):
                dataBuku.update(dataTambah)
                print("Data is Saved")
                tampilkanData()
                break
            elif(inputConf=='N'):
                print("Data is not Saved")
                break
            else:
                continue

def updateData():
    inputKode = input("Input Book Code to be Updated: ")

    if(inputKode not in dataBuku):
        print("Data does not Exist")
    else:
        print (f"Code: {inputKode}, Title: {dataBuku[inputKode]['Title']}, Author: {dataBuku[inputKode]['Author']}, Year: {dataBuku[inputKode]['Year']}, Genre: {dataBuku[inputKode]['Genre']}, Status: {dataBuku[inputKode]['Status']}")  
                        
        while(True):
            inputConf = input("Press Y to continue to update the data or N if you would like to cancel the update (Y/N): ")
            inputConf = inputConf.upper()

            if(inputConf=='Y'):
                inputColumn = input("Input the Column/Description to be Edited: " )
                inputValue = input("Please Input the Value: ")

                while(True):
                    inputConf = input("Confirm the Data be Updated? (Y/N): ")
                    inputConf = inputConf.upper()
                                
                    if(inputConf=='Y'):
                        dataBuku[inputKode][inputColumn] = inputValue
                        print("Data is Updated")
                        tampilkanData()
                        break
                    elif(inputConf=='N'):
                        print("Data is not Updated")
                        break
                    else:
                        continue
                break                    
            elif(inputConf=='N'):
                print("Data is not Updated")
                break
            else:
                continue

def deleteData():
    inputKode = input("Input Book Code: ")

    if(inputKode not in dataBuku):
        print("Data does not Exist")
    else:
        while(True):
            inputConf = input("Will the Data be Deleted? (Y/N): ")
            inputConf = inputConf.upper()

            if(inputConf=='Y'):
                del dataBuku[inputKode]
                print("Data Deleted")
                tampilkanData()
                break
            elif(inputConf=='N'):
                print("Data is not Deleted")
                break
            else:
                continue

#Start
while (program==True):
#Main Menu
    print ('''
        Welcome to Purwadhika Library!

        List Menu:
        1. Open Library Book Data
        2. Return Book
        3. Update Book Data
        4. Borrow Book
        5. Exit Program
    ''')

    pilih=int(input("Choose the Main Menu [1-5]: "))

#Read
    if(pilih == 1):
        #Sub Menu 1
        while(True):
            print ('''
            +++++++Library Book Data+++++++

            List Menu :
            1. Open Library Book Data
            2. Open Specific Book Data
            3. Back to Main Menu
            ''')

            pilih = int(input("Please Select Library Book Data Sub Menu [1-3]: "))

            if(pilih == 1):
                tampilkanData()

            elif(pilih == 2):
                tampilkanDataPilihan()
            
            elif(pilih == 3):
                break

            else:
                print("*****Please Input the Right Menu Number*****")

#Create
    elif(pilih == 2): 
        while(True):
            print ('''
            +++++++Return Book Data+++++++

            List Menu :
            1. Give Book
            2. Back to Main Menu
            ''')

            pilih = int(input("Please Select Return Book Data Sub Menu [1-2]: "))

            if(pilih == 1):
                createData()

            elif(pilih == 2):
                break

            else:
                print("*****Please Input the Right Menu Number*****")

#Update            
    elif(pilih == 3):
        while(True):
            print ('''
            +++++++Update Book Data+++++++

            List Menu :
            1. Update Book Information
            2. Back to Main Menu
            ''')

            pilih = int(input("Please Select Update Book Data Sub Menu [1-2]: "))

            if(pilih == 1):
                updateData()

            elif(pilih == 2):
                break
            else:
                print("*****Please Input the Right Menu Number*****")

#Delete
    elif(pilih == 4):
        while(True):
            print ('''
            +++++++Borrow Book Data+++++++

            List Menu :
            1. Take a Book
            2. Back to Main Menu
            ''')

            pilih = int(input("Please Select Borrow Book Data Sub Menu [1-2]: "))

            if(pilih == 1):
                deleteData()

            elif(pilih == 2):
                break

            else:
                print("*****Please Input the Right Menu Number*****")

#Exit
    elif(pilih == 5):
        print("Thank you and Good Bye!")
        program=False
    
    else :
        print("*****Please Input the Right Menu Number*****")

 







