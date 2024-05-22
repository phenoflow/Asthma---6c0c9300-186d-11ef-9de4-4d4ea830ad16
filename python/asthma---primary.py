# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"c665.00","system":"readv2"},{"code":"c1C4.00","system":"readv2"},{"code":"c11b.00","system":"readv2"},{"code":"9OJA.11","system":"readv2"},{"code":"c14j.00","system":"readv2"},{"code":"c31x.00","system":"readv2"},{"code":"H47y000","system":"readv2"},{"code":"c13o.00","system":"readv2"},{"code":"66YK.00","system":"readv2"},{"code":"c192.00","system":"readv2"},{"code":"c61u.00","system":"readv2"},{"code":"c61x.00","system":"readv2"},{"code":"173c.00","system":"readv2"},{"code":"663j.00","system":"readv2"},{"code":"H33zz00","system":"readv2"},{"code":"c31G.00","system":"readv2"},{"code":"c109.00","system":"readv2"},{"code":"H35y700","system":"readv2"},{"code":"H33..00","system":"readv2"},{"code":"c31u.00","system":"readv2"},{"code":"66YC.00","system":"readv2"},{"code":"c648.00","system":"readv2"},{"code":"c14w.00","system":"readv2"},{"code":"c1Du.00","system":"readv2"},{"code":"c13L.00","system":"readv2"},{"code":"c1Dw.00","system":"readv2"},{"code":"c672.00","system":"readv2"},{"code":"H332.00","system":"readv2"},{"code":"c191.00","system":"readv2"},{"code":"H33z000","system":"readv2"},{"code":"c135.00","system":"readv2"},{"code":"1O2..00","system":"readv2"},{"code":"c65f.00","system":"readv2"},{"code":"c1D6.00","system":"readv2"},{"code":"c66a.00","system":"readv2"},{"code":"c61v.00","system":"readv2"},{"code":"c61i.00","system":"readv2"},{"code":"c31t.00","system":"readv2"},{"code":"c61F.00","system":"readv2"},{"code":"c13T.00","system":"readv2"},{"code":"c13G.00","system":"readv2"},{"code":"178..00","system":"readv2"},{"code":"c13U.00","system":"readv2"},{"code":"H334.00","system":"readv2"},{"code":"8791.00","system":"readv2"},{"code":"663V100","system":"readv2"},{"code":"663h.00","system":"readv2"},{"code":"c61O.00","system":"readv2"},{"code":"cA11.00","system":"readv2"},{"code":"H33z.00","system":"readv2"},{"code":"c1E1.00","system":"readv2"},{"code":"c66B.00","system":"readv2"},{"code":"H33z.11","system":"readv2"},{"code":"173d.00","system":"readv2"},{"code":"c1E7.00","system":"readv2"},{"code":"cA15.00","system":"readv2"},{"code":"3052AT","system":"readv2"},{"code":"691 TM","system":"readv2"},{"code":"Y060 LE","system":"readv2"},{"code":"493 AE","system":"readv2"},{"code":"493 AH","system":"readv2"},{"code":"493 EP","system":"readv2"},{"code":"493 C","system":"readv2"},{"code":"493 F","system":"readv2"},{"code":"493","system":"readv2"},{"code":"Y100 AR","system":"readv2"},{"code":"493 NA","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('asthma-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["asthma---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["asthma---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["asthma---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
