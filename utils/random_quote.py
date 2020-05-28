import random
import json


def get_translations():
    with open('wotd.json', 'r') as f:
        translation_dict = json.load(f)
        
        no_of_lines = len(translation_dict) - 1
        res1 = translation_dict[0]
        res2 = translation_dict[1]
        res3 = translation_dict[2]
        res4 = translation_dict[3]
        res_img = translation_dict[-1]

        return res1, res2, res3, res4, res_img, no_of_lines
