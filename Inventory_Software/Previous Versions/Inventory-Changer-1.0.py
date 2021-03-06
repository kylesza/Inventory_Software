#####################################
##  Empire Wire and Cable          ##
##    Inventory Changer            ##
##                                 ##
## Future Improvements:            ##
## Fix "mis-finds"                 ##
## Delete customer specific parts  ##
#####################################


print("STEPS TO DO BEFORE RUNNING\n\n")
print("1. Delete all columns except for Item#, Description, \
Product Group, \n and Quantity. Also delete the top row \n")
print("2. Sort Item# column by alphabetical order\n")
print("3. Click on Quantity Column, change the format to Number  \n in the Number \
tab on the top bar of excel. \n Then move the Decimal over 2 to the right 2 spots\n \
You also need to click on the Desciption column, ctrl-f, \n and replace all ',' with \
'-' \n")
print("4. Save file as .csv and place it in the folder this program is in\n")
print("5. Type 'q' for file name you want to open to end the program\n")

open_file=0

while open_file != "q" :
   try:    
        open_file = input("Enter name of file to open (remeber extension) : ")
        print("\n")
        new_file = input("Enter name of new file : ")
        new_file = open(new_file,'w')
        import csv


        def create_file(open_file):
            
            with open(open_file) as f:
                reader = csv.reader(f)
                for row in reader:

                    if "WCH-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Winchester Electronics"
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        print(s)
                        new_file.write(s)
                        
                    if "WEI-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Weidmuller"
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        print(s)
                        new_file.write(s)
                        
                    if "WLD-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Wieland Electric"
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        print(s)
                        new_file.write(s)

                    if "WAG-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "WAGO"
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"  
                        print(s)
                        new_file.write(s)
                    
                    elif "AMP-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "TE Connectivity/AMP"   
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)     
                        
                    elif "3M-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "3M Interconnect Solutions"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "AIM-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Aim Electronics"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)            
                    elif "ALP-" in row[0] or "ALPHA WIRE" in row[0]:
                        if "-"  in row[0]:
                            v = row[0]
                            v = v.split("-",1)[1]
                            row[2] = "Alpha Wire"
                            if "EA" in row[3]:
                                row[3] = row[3].split(",")[-1]
                            s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                            new_file.write(s)
                        else:
                            v = row[0]
                            row[2] = "Alpha Wire"
                            if "EA" in row[3]:
                                row[3] = row[3].split(",")[-1]
                            s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                            new_file.write(s)
                    elif "APH-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Amphenol"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "APL-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Appleton Electric"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "BEL-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Belden"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "BH-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Brad Harrison/Woodhead Connectivity"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "BIN-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Binder"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "BR-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Brand Rex"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "BBC-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Black Box"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "BUR-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Burndy Electronics Div."
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "BUS-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Cooper Bussman"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "CAR-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "General Cable/Carol"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "COM-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "CommScope"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "CON-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Lapp USA"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "DDK-" in row[0]:
                        if "-"  in row[0]:
                            v = row[0]
                            v = v.split("-",1)[1]
                            row[2] = "DDK/Fujikura"
                            if "EA" in row[3]:
                                row[3] = row[3].split(",")[-1]
                            s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                            new_file.write(s)
                        else:
                            v = row[0]
                            row[2] = "DDK/Fujikura"
                            if "EA" in row[3]:
                                row[3] = row[3].split(",")[-1]
                            s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                            new_file.write(s)
                    elif "DEU-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Deutsch Industrial"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "FD-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = ""
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "FRA-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Mersen USA"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "HOF-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Hoffman Products"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "HON-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Honda Connectors"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "HT-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Harting North America"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "HUB-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Hubbell Industrial Controls"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "HYC-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Heyco Products"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "IDC-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Idec/Control Components"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "ILME-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "ILME"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "IGUS-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Igus"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "JAE-" in row[0]:
                        if "-"  in row[0]:
                            v = row[0]
                            v = v.split("-",1)[1]
                            row[2] = "JAE Electronics"
                            if "EA" in row[3]:
                                row[3] = row[3].split(",")[-1]
                            s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                            new_file.write(s)
                        else:
                            pass
                    elif "JST-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "J.S.T."
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "LMO-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "LEMO USA"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "LTZ-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Lutze"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "LUM-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Lumberg"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "MC-" in row[0]:
                        v = row[0]
                        z = row[0]
                        v = v.split("-",1)[1]
                        z = z.split("-",1)[0]
                        if z == "MC" or z == "MCC": 
                           row[2] = "Multi-Contract USA"
                           if "EA" in row[3]:
                               row[3] = row[3].split(",")[-1]
                           s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                           new_file.write(s)
                    elif "MEN-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Mencom"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "MLX-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Molex"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "MS-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = ""
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "NCH-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Nichifu America"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "NIE-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Niedax Inc."
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "NTR-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "N-Tron"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "OLF-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Lapp USA"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "OMR-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Omron Electronic Components"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "PAR-" in row[0] or "PARK-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Parker Automation-CTC"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "PDT-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Panduit"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "PF-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Pepperl & Fuchs"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "PHX-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Phoenix Contact"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "PIO-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Delphi Connection Systems"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "PMA-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "PMA"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "RDE-" in row[0]:
                        if "-"  in row[0]:
                            v = row[0]
                            v = v.split("-",1)[1]
                            row[2] = "RDE"
                            if "EA" in row[3]:
                                row[3] = row[3].split(",")[-1]
                            s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                            new_file.write(s)
                        else:
                            pass
                    elif "REE-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Rees"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                        # TRK is here just to stop mis-finds
                    elif "TRK-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Turck"
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                        #
                    elif "REI-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Reiku"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "REM-" in row[0] or "RPG-" in row[0] or "RSM-" in row[0] or "RSR-" in row[0]:
                        v = row[0]
                        row[2] = "Remke Industries"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "SAB-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "SAB North America"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "SLC-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Hummel/Sealcon"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "SOR-" in row[0]:
                        v = row[0]
                        row[2] = "Remke Industries"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "SOU-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Souriau USA"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "SRB-" in row[0]:
                        v = row[0]
                        row[2] = "Remke Industries"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "STI-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Omron STI"
                        if "EA" in row[3]:
                            row[3] = row[3].split(",")[-1]
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "TB-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = "Thomas & Betts"

                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "TS" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[1]
                        row[2] = ""
                        s = v + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                        new_file.write(s)
                    elif "R-" in row[0]:
                        v = row[0]
                        v = v.split("-",1)[0]
                        print(v)
                        if v == "R":
                           print("yay!")
                           row[2] = "Remke Industries"
                           if "EA" in row[3]:
                               row[3] = row[3].split(",")[-1]
                           s = row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "\n"
                           new_file.write(s)


         
   except:
      print("\nFile Error, please try again111\n")
                
   try:           
      create_file(open_file)
   except:
      print("File Error, please try again22\n")
   new_file.close()
   print("Review the new .csv. If a product name looks out of place, it is. Delete those.\n")
