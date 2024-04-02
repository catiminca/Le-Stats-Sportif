import os
import json
import csv

class DataIngestor:
    def __init__(self, csv_path: str):
        # TODO: Read csv from csv_path
        self.allData = {}
        self.questions_best_is_min = [
            'Percent of adults aged 18 years and older who have an overweight classification',
            'Percent of adults aged 18 years and older who have obesity',
            'Percent of adults who engage in no leisure-time physical activity',
            'Percent of adults who report consuming fruit less than one time daily',
            'Percent of adults who report consuming vegetables less than one time daily'
        ]

        self.questions_best_is_max = [
            'Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)',
            'Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic physical activity and engage in muscle-strengthening activities on 2 or more days a week',
            'Percent of adults who achieve at least 300 minutes a week of moderate-intensity aerobic physical activity or 150 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)',
            'Percent of adults who engage in muscle-strengthening activities on 2 or more days a week',
        ]
        with open(csv_path, 'r') as csv_file:
            heading = next(csv_file) 
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                if row[8] in self.allData:
                    self.allData[row[8]].append(row)
                else:
                    self.allData[row[8]] = [row]
            #print(self.allData["Percent of adults aged 18 years and older who have an overweight classification"])
            
            
            
# if __name__=='__main__':
#     cv = DataIngestor("../nutrition_activity_obesity_usa_subset.csv")
#    # print(cv.allData, len(cv.allData))

