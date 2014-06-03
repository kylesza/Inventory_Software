##
print("There are 2 steps before doing this \
First, open the .xls and sort alphabetically \
Remember to change the inventory to .csv, and then to a .txt\
Remember to add .csv at the end of the new file \n")
new_file = 0
while new_file != "quit":
        
    new_file = input("Enter name of new file : ")
    print("\n")
    open_file = input("Enter name of file to open : ")
    open_file = open(open_file,'r')
    new_file = open(new_file,'w')


    def create_file(open_file):
        for line in open_file:
            s = line.rstrip()
            s = line.strip('"')
            s = line.split(",",3)   
            if "AMP-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "TE Connectivity/AMP"   
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                print(s)
                new_file.write(s)
            elif "3M-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "3M Interconnect Solutions"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
                print(s)
            elif "AIM-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Aim Electronics"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
                print(s)
            elif "ALP-" in s[0] or "ALPHA WIRE" in s[0]:
                if "-"  in s[0]:
                    v = s[0]
                    v = v.split("-",1)[1]
                    s[2] = "Alpha Wire"
                    s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                    new_file.write(s)
                    print(s)
                else:
                    v = s[0]
                    s[2] = "Alpha Wire"
                    s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                    new_file.write(s)
                    print(s)
            elif "APH-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Amphenol"
                s = v + "," + s[1] + "," + s[2] + "," + s[3]+ "\n"
                new_file.write(s)
                print(s)
            elif "APL-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Appleton Electric"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
                print(s)
            elif "BEL-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Belden"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
                print(s)
            elif "BH-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Brad Harrison/Woodhead Connectivity"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
                print(s)
            elif "BIN-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Binder"
                s = v + "," + s[1] + "," + s[2] + "," + s[3]+ "\n"
                new_file.write(s)
                print(s)
            elif "BR-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Brand Rex"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
                print(s)
            elif "BUR-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Burndy Electronics Div."
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
                print(s)
            elif "BUS-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Cooper Bussman"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
                print(s)
            elif "CAR-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "General Cable/Carol"
                s = v + "," + s[1] + "," + s[2] + "," + s[3]  + "\n"
                new_file.write(s)
                print(s)
            elif "COM-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "CommScope"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
                print(s)
            elif "CON-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Lapp USA"
                s = v + "," + s[1] + "," + s[2] + "," + s[3]+ "\n"
                new_file.write(s)
                print(s)
            elif "DDK-" in s[0]:
                if "-"  in s[0]:
                    v = s[0]
                    v = v.split("-",1)[1]
                    s[2] = "DDK/Fujikura"
                    s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                    new_file.write(s)
                    print(s)
                else:
                    v = s[0]
                    s[2] = "DDK/Fujikura"
                    s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                    new_file.write(s)
                    print(s)
            elif "DEU-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Deutsch Industrial"
                s = v + "," + s[1] + "," + s[2] + "," + s[3]+ "\n"
                new_file.write(s)
                print(s)
            elif "FRA-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Mersen USA"
                s = v + "," + s[1] + "," + s[2] + "," + s[3]  + "\n"
                new_file.write(s)
                print(s)
            elif "HOF-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Hoffman Products"
                s = v + "," + s[1] + "," + s[2] + "," + s[3]+ "\n"
                new_file.write(s)
                print(s)
            elif "HON-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Honda Connectors"
                s = v + "," + s[1] + "," + s[2] + "," + s[3]+ "\n"
                new_file.write(s)
                print(s)
            elif "HT-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Harting North America"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
                print(s)
            elif "HUB-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Hubbell Industrial Controls"
                s = v + "," + s[1] + "," + s[2] + "," + s[3]+ "\n"
                new_file.write(s)
            elif "HYC-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Heyco Products"
                s = v + "," + s[1] + "," + s[2] + "," + s[3]+ "\n"
                new_file.write(s)
            elif "IDC-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Idec/Control Components"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "IGUS-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Igus"
                s = v + "," + s[1] + "," + s[2] + "," + s[3]+ "\n"
                new_file.write(s)
            elif "JAE-" in s[0]:
                if "-"  in s[0]:
                    v = s[0]
                    v = v.split("-",1)[1]
                    s[2] = "JAE Electronics"
                    s = v + "," + s[1] + "," + s[2] + "," + s[3]+ "\n"
                    new_file.write(s)
                else:
                    pass
            elif "JST-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "J.S.T."
                s = v + "," + s[1] + "," + s[2] + "," + s[3]+ "\n"
                new_file.write(s)
            elif "LMO-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "LEMO USA"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "LTZ-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Lutze"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "LUM-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Lumberg"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "MC-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                MC = v.split("-",1)[0]
                if MC == "MC":
                    s[2] = "Multi-Contract USA"
                    s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                    new_file.write(s)
            elif "MEN-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Mencom"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "MLX-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Molex"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "MS-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = ""
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "NCH-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Nichifu America"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "NIE-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Niedax Inc."
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "NTR-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "N-Tron"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "OLF-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Lapp USA"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "OMR-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Omron Electronic Components"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "PAR" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Parker Automation-CTC"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "PDT-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Panduit"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "PF-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Pepperl & Fuchs"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "PHX-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Phoenix Contact"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "PIO-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Delphi Connection Systems"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "PMA-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "PMA"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "R-" in s[0]:
                v = s[0]
                s[2] = "Remke Industries"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "RDE-" in s[0]:
                if "-"  in s[0]:
                    v = s[0]
                    v = v.split("-",1)[1]
                    s[2] = "RDE"
                    s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                    new_file.write(s)
                else:
                    pass
            elif "REE-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Rees"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "REI-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Reiku"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "REM-" in s[0] or "RPG-" in s[0] or "RSM-" in s[0] or "RSR-" in s[0]:
                v = s[0]
                s[2] = "Remke Industries"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "SAB-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "SAB North America"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "SLC-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Hummel/Sealcon"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "SOR-" in s[0]:
                v = s[0]
                s[2] = "Remke Industries"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "SOU-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Souriau USA"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "SRB-" in s[0]:
                v = s[0]
                s[2] = "Remke Industries"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "STI-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Omron STI"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "TB-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Thomas & Betts"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "TRK-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Turck"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "TS-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = ""
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "WAG-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "WAGO"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "WCH-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Winchester Electronics"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "WEI-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Weidmuller"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            elif "WLD-" in s[0]:
                v = s[0]
                v = v.split("-",1)[1]
                s[2] = "Wieland Electric"
                s = v + "," + s[1] + "," + s[2] + "," + s[3] + "\n"
                new_file.write(s)
            else:
                pass

                
    create_file(open_file)

