import csv


class LocalDatabase:

    def __init__(self, file_path):
        self.file_path = file_path

    def is_exist(self, data_str):
        data_str = "{0}\n".format(data_str)
        with open(self.file_path, 'r') as f:
            file_data = f.readlines()
        if data_str in file_data:
            return True
        else:
            return False

    def write(self,data_str):
        if not self.is_exist(data_str):
            with open(self.file_path, 'a') as f:
                f.write('{0}\n'.format(data_str))
            return True
        else:
            return False

    def read(self, fav_type):
        out_data = []
        with open(self.file_path, 'rt')as f:
            data = csv.reader(f)
            for row in data:
                if fav_type == row[0]:
                    out_data.append({'name': row[1], 'url': row[2]})
                elif fav_type == "all":
                    out_data.append({'name': row[1], 'url': row[2]})

        return out_data, len(out_data)

    def clean(self):
        try:
            with open(self.file_path, 'w') as f:
                f.truncate(0)
            return True
        except Exception as e:
            return False
