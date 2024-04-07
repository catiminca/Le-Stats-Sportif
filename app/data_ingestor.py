""""Module for geting data from csv file"""

import csv

class DataIngestor:
    """Class for getting the data"""
    def __init__(self, csv_path: str):
        # Read csv from csv_path
        self.all_data = {}
        self.questions_best_is_min = [
            'Percent of adults aged 18 years and older who have an overweight classification',
            'Percent of adults aged 18 years and older who have obesity',
            'Percent of adults who engage in no leisure-time physical activity',
            'Percent of adults who report consuming fruit less than one time daily',
            'Percent of adults who report consuming vegetables less than one time daily'
        ]
        q1_max = ''.join(['Percent of adults who achieve at least 150 minutes a week of',
                        ' moderate-intensity aerobic physical activity or 75 minutes a week of',
                        ' vigorous-intensity aerobic activity (or an equivalent combination)'])
        q2_max = ''.join(['Percent of adults who achieve at least 150 minutes a week of',
                        ' moderate-intensity aerobic physical activity or 75 minutes a week of',
                        ' vigorous-intensity aerobic physical activity and engage in',
                        ' muscle-strengthening activities on 2 or more days a week'])
        q3_max = ''.join(['Percent of adults who achieve at least 300 minutes a week of',
                        ' moderate-intensity aerobic physical activity or 150 minutes a week of',
                        ' vigorous-intensity aerobic activity (or an equivalent combination)'])
        q4_max = ''.join(['Percent of adults who engage in muscle-strengthening activities on 2',
                        ' or more days a week'])
        self.questions_best_is_max = [q1_max, q2_max, q3_max, q4_max]
        with open(csv_path, 'r') as csv_file:
            next(csv_file)
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[8] in self.all_data:
                    self.all_data[row[8]].append(row)
                else:
                    self.all_data[row[8]] = [row]
            