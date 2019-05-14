import json


class LocalDatabase():

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self,data_str):
        data = dict()
        data['people'] = []
        data['people'].append({
            'name': 'Scott',
            'website': 'stackabuse.com',
            'from': 'Nebraska'
        })
        data['people'].append({
            'name': 'Larry',
            'website': 'google.com',
            'from': 'Michigan'
        })
        data['people'].append({
            'name': 'Tim',
            'website': 'apple.com',
            'from': 'Alabama'
        })

        with open(self.file_path, 'a') as f:
            # json.dump(data, f)
            f.write('{0}\n'.format(data_str))
        return 0
