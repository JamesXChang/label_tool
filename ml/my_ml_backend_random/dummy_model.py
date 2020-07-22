import random
import sys
sys.path.append("../")

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
                    'from_name': 'label',
                    'id': 'e-qKw65KZA',
                    'original_height': 629,
                    'original_width': 1225,
                    'source': '$image',
                    'to_name': 'image',
                    'type': 'rectanglelabels',
                    'value': {
                        'height': 4.675324675324675,
                        'rectanglelabels': ['DATE_O'],
                        'rotation': 0,
                        'width': 14.811375848404387,
                        'x': 72.66210876437343,
                        'y': 21.2987012987013
                    }
                },
                {
                    'from_name': 'answer',
                    'id': 'e-qKw65KZA',
                    'original_height': 629,
                    'original_width': 1225,
                    'source': '$image',
                    'to_name': 'image',
                    'type': 'textarea',
                    'value': {
                        'height': 4.675324675324675,
                        'rotation': 0,
                        'text': ['106年12月15日'],
                        'width': 14.811375848404387,
                        'x': 72.66210876437343,
                        'y': 21.2987012987013
                    }
                },
                {
                    'from_name': 'label',
                    'id': 'h_76oHEUHM',
                    'original_height': 629,
                    'original_width': 1225,
                    'source': '$image',
                    'to_name': 'image',
                    'type': 'rectanglelabels',
                    'value': {'height': 7.333842627960275,
                        'rectanglelabels': ['AMOUNT_O'],
                        'rotation': 0,
                        'width': 18.933333333333334,
                        'x': 31.866666666666667,
                        'y': 38.411000763941935}},
                {
                    'from_name': 'answer',
                    'id': 'h_76oHEUHM',
                    'original_height': 629,
                    'original_width': 1225,
                    'source': '$image',
                    'to_name': 'image',
                    'type': 'textarea',
                    'value': {'height': 7.333842627960275,
                        'rotation': 0,
                        'text': ['捌萬元整'],
                        'width': 18.933333333333334,
                        'x': 31.866666666666667,
                        'y': 38.411000763941935
                    }
                },
                {
                    'from_name': 'label',
                    'id': '7FTAdY3cxH',
                    'original_height': 629,
                    'original_width': 1225,
                    'source': '$image',
                    'to_name': 'image',
                    'type': 'rectanglelabels',
                    'value': {'height': 4.675324675324675,
                        'rectanglelabels': ['S_AMOUNT_O'],
                        'rotation': 0,
                        'width': 9.21081081081081,
                        'x': 77.19459459459459,
                        'y': 31.168831168831172
                    }
                },
                {
                    'from_name': 'answer',
                    'id': '7FTAdY3cxH',
                    'original_height': 629,
                    'original_width': 1225,
                    'source': '$image',
                    'to_name': 'image',
                    'type': 'textarea',
                    'value': {'height': 4.675324675324675,
                        'rotation': 0,
                        'text': ['80,000'],
                        'width': 9.21081081081081,
                        'x': 77.19459459459459,
                        'y': 31.168831168831172
                    }
                },
                {
                    'from_name': 'label',
                    'id': 'R9_AAk5pbz',
                    'original_height': 629,
                    'original_width': 1225,
                    'source': '$image',
                    'to_name': 'image',
                    'type': 'rectanglelabels',
                    'value': {'height': 22.337662337662337,
                        'rectanglelabels': ['NONNEGOT_I'],
                        'rotation': 0,
                        'width': 3.3333333333333335,
                        'x': 57.60000000000001,
                        'y': 51.168831168831176
                    }
                },
                {
                    'from_name': 'label',
                    'id': 'DuqJ8NM95C',
                    'original_height': 629,
                    'original_width': 1225,
                    'source': '$image',
                    'to_name': 'image',
                    'type': 'rectanglelabels',
                    'value': {'height': 9.35064935064935,
                        'rectanglelabels': ['SEAL_S'],
                        'rotation': 0,
                        'width': 28.933333333333334,
                        'x': 62.53333333333333,
                        'y': 58.18181818181818
                    }
                },
                {
                    'from_name': 'label',
                    'id': 'GKukVS0yNC',
                    'original_height': 629,
                    'original_width': 1225,
                    'source': '$image',
                    'to_name': 'image',
                    'type': 'rectanglelabels',
                    'value': {'height': 6.493506493506493,
                        'rectanglelabels': ['PAY_TO_O'],
                        'rotation': 0,
                        'width': 37.340689655172405,
                        'x': 32.262988505747124,
                        'y': 29.09090909090909
                    }
                },
                {
                    'from_name': 'answer',
                    'id': 'GKukVS0yNC',
                    'original_height': 629,
                    'original_width': 1225,
                    'source': '$image',
                    'to_name': 'image',
                    'type': 'textarea',
                    'value': {'height': 6.493506493506493,
                        'rotation': 0,
                        'text': ['新竹縣五峰鄉桃山國民小學'],
                        'width': 37.340689655172405,
                        'x': 32.262988505747124,
                        'y': 29.09090909090909
                    }
                }],
            })
        return results

    def fit(self, completions, workdir=None, **kwargs):
        return {'random': random.randint(1, 10)}
