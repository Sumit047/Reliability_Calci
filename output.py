import csv
import os
class write_in:
    def writrintofile(data,header,path):
        
        assert os.path.isfile(path)
        with open(path,'w',newline='') as f:
            writer = csv.writer(f)
              # write the heading
            writer.writerow(header)
        # write data into multiple rows
            writer.writerows(data)
