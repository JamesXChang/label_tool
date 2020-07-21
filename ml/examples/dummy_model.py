import random

from ml import LabelStudioMLBase


class DummyModel(LabelStudioMLBase):

    def __init__(self, **kwargs):
        super(DummyModel, self).__init__(**kwargs)

        from_name, schema = list(self.parsed_label_config.items())[0]
        self.from_name = from_name
        self.to_name = schema['to_name'][0]
        self.labels = schema['labels']

    def predict(self, tasks, **kwargs):
        results = []
        for task in tasks:
            results.append({
                'result': [
                {
                    'from_name': self.from_name,
                    'to_name': self.to_name,
                    "original_height": 629,
                    "original_width": 1225,
                    "source": "$image",
                    "to_name": "image",
                    'type': 'rectanglelabels',
                    'value': {
                        "rectanglelabels": [
                            "DATE"
                        ],
                        "rotation": 0,
                        "height": 4.675324675324675,
                        "width": 15.066666666666666,
                        "x": 72.26666666666667,
                        "y": 21.558441558441558
                    }
                },
                {
                    "from_name": "answer",
                    "id": self.to_name,
                    "original_height": 629,
                    "original_width": 1225,
                    "source": "$image",
                    "to_name": "image",
                    "type": "textarea",
                    "value": {
                        "text": [
                            "106年12月15日"
                        ],
                        "rotation": 0,
                        "height": 4.675324675324675,
                        "width": 15.066666666666666,
                        "x": 72.26666666666667,
                        "y": 21.558441558441558
                    }
                },
                {
                    "from_name": self.from_name,
                    "id": self.to_name,
                    "original_height": 629,
                    "original_width": 1225,
                    "source": "$image",
                    "to_name": "image",
                    "type": "rectanglelabels",
                    "value": {
                        "rectanglelabels": [
                            "AMOUNT"
                        ],
                        "rotation": 0,
                        "height": 6.818181818181817,
                        "width": 19.203603603603604,
                        "x": 31.864864864864867,
                        "y": 38.66883116883117
                    }
                },
                {
                    "from_name": "answer",
                    "id": self.to_name,
                    "original_height": 629,
                    "original_width": 1225,
                    "source": "$image",
                    "to_name": "image",
                    "type": "textarea",
                    "value": {
                        "text": [
                            "捌萬元整"
                        ],
                        "rotation": 0,
                        "height": 6.818181818181817,
                        "width": 19.203603603603604,
                        "x": 31.864864864864867,
                        "y": 38.66883116883117
                    }
                },
                {
                    "from_name": self.from_name,
                    "id": self.to_name,
                    "original_height": 629,
                    "original_width": 1225,
                    "source": "$image",
                    "to_name": "image",
                    "type": "rectanglelabels",
                    "value": {
                        "rectanglelabels": [
                            "S_AMOUNT"
                        ],
                        "rotation": 0,
                        "height": 3.896103896103896,
                        "width": 9.066666666666666,
                        "x": 76.93333333333334,
                        "y": 31.68831168831169
                    }
                },
                {
                    "from_name": "answer",
                    "id": self.to_name,
                    "original_height": 629,
                    "original_width": 1225,
                    "source": "$image",
                    "to_name": "image",
                    "type": "textarea",
                    "value": {
                        "text": [
                            "80,000"
                        ],
                        "rotation": 0,
                        "height": 3.896103896103896,
                        "width": 9.066666666666666,
                        "x": 76.93333333333334,
                        "y": 31.68831168831169
                    }
                },
                {
                    "from_name": self.from_name,
                    "id": self.to_name,
                    "original_height": 629,
                    "original_width": 1225,
                    "source": "$image",
                    "to_name": "image",
                    "type": "rectanglelabels",
                    "value": {
                        
                        "rectanglelabels": [
                            "NONNEGOT"
                        ],
                        "rotation": 0,
                        "height": 23.376623376623378,
                        "width": 3.3333333333333335,
                        "x": 57.733333333333334,
                        "y": 50.64935064935064
                    }
                },
                {
                    "from_name": self.from_name,
                    "id": self.to_name,
                    "original_height": 629,
                    "original_width": 1225,
                    "source": "$image",
                    "to_name": "image",
                    "type": "rectanglelabels",
                    "value": {
                        "rectanglelabels": [
                            "SEAL"
                        ],
                        "rotation": 0,
                        "height": 8.571428571428571,
                        "width": 29.86666666666667,
                        "x": 62.133333333333326,
                        "y": 58.44155844155844
                    }
                },
                {
                    "from_name": self.from_name,
                    "id": self.to_name,
                    "original_height": 629,
                    "original_width": 1225,
                    "source": "$image",
                    "to_name": "image",
                    "type": "rectanglelabels",
                    "value": {
                        "rectanglelabels": [
                            "PAY_TO"
                        ],
                        "rotation": 0,
                        "height": 6.233766233766234,
                        "width": 37.06474820143884,
                        "x": 32.13429256594724,
                        "y": 29.350649350649352
                    }
                },
                {
                    "from_name": "answer",
                    "id": self.to_name,
                    "original_height": 629,
                    "original_width": 1225,
                    "source": "$image",
                    "to_name": "image",
                    "type": "textarea",
                    "value": {
                        "text": [
                            "新竹縣五峰鄉桃山國民小學"
                        ],
                        "rotation": 0,
                        "height": 6.233766233766234,
                        "width": 37.06474820143884,
                        "x": 32.13429256594724,
                        "y": 29.350649350649352
                    }
                }
                ],
            })
        return results

    def fit(self, completions, workdir=None, **kwargs):
        return {'random': random.randint(1, 10)}
