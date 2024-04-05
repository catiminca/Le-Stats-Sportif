import unittest
from app.data_ingestor import DataIngestor
from app.task_runner import TaskRunner
from sys import float_info
class TestMethods(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.data_ingestor = DataIngestor("./unittests/test.csv")
        self.count = 0
        self.jobs = []
    
    def test_states_mean(self):
        res = {'New Mexico':28.8, 'West Virginia':29.45, 'Ohio':30.05, 'Maryland':35.35,'Kansas':42.8 ,'Nebraska':45.8}
        for k, v in res.items():
            for key, value in TaskRunner.states_mean({"question": "Percent of adults aged 18 years and older who have obesity"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)

        res = {'West Virginia':21.7, 'Ohio':26.4, 'Kansas':32.75, 'New Mexico':35, 'Nebraska':35.65,'Maryland':43.5}
        for k, v in res.items():
            for key, value in TaskRunner.states_mean({"question": "Percent of adults who engage in no leisure-time physical activity"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        
    def test_state_mean(self):    
        
        res = {'Ohio':30.05}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "Ohio"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        
        res = {'Ohio':26.4}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "Ohio"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'New Mexico':28.8}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "New Mexico"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'New Mexico':35}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "New Mexico"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)

        res = {'Maryland':35.35}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "Maryland"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Maryland':43.5}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "Maryland"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        
        res = {'Kansas':42.8}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "Kansas"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Kansas':32.75}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "Kansas"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Nebraska':45.8}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "Nebraska"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Nebraska':35.65}
        for k, v in res.items():
            for k, v in TaskRunner.state_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "Nebraska"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        
        res = {'West Virginia':29.45}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "West Virginia"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'West Virginia':21.7}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "West Virginia"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)

    def test_best5(self):
        res = {'New Mexico':28.8, 'West Virginia':29.45, 'Ohio':30.05, 'Maryland':35.35,'Kansas':42.8}
        for k, v in res.items():
            for key, value in TaskRunner.best5({"question": "Percent of adults aged 18 years and older who have obesity"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'West Virginia':21.7, 'Ohio':26.4, 'Kansas':32.75, 'New Mexico':35, 'Nebraska':35.65}
        for k, v in res.items():
            for key, value in TaskRunner.best5({"question": "Percent of adults who engage in no leisure-time physical activity"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
    
    def test_worst5(self):
        res = {'Nebraska':45.8, 'Kansas':42.8, 'Maryland':35.35, 'Ohio':30.05,'West Virginia':29.45}
        for k, v in res.items():
            for key, value in TaskRunner.worst5({"question": "Percent of adults aged 18 years and older who have obesity"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Maryland':43.5, 'Nebraska':35.65, 'New Mexico':35, 'Kansas':32.75, 'Ohio':26.4}
        for k, v in res.items():
            for key, value in TaskRunner.worst5({"question": "Percent of adults who engage in no leisure-time physical activity"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
    
    def test_global_mean(self):
        res = {'global_mean': 35.375}
        for k, v in res.items():
            for key, value in TaskRunner.global_mean({"question": "Percent of adults aged 18 years and older who have obesity"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'global_mean': 32.5}
        for k, v in res.items():
            for key, value in TaskRunner.global_mean({"question": "Percent of adults who engage in no leisure-time physical activity"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)

    def test_diff_from_mean(self):
        res = {'New Mexico': 6.575, 'West Virginia': 6.075, 'Ohio': 5.425, 'Maryland': -0.025, 'Kansas': -7.3, 'Nebraska': -10.425}
        for k, v in res.items():
            for key, value in TaskRunner.diff_from_mean({"question": "Percent of adults aged 18 years and older who have obesity"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'West Virginia': 7.8, 'Ohio': 6.1, 'Kansas': 0.75, 'New Mexico': -2.5, 'Nebraska': -3.15, 'Maryland': -8.15}
        for k, v in res.items():
            for key, value in TaskRunner.diff_from_mean({"question": "Percent of adults who engage in no leisure-time physical activity"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
    
    def test_state_dif_from_mean(self):
        res = {'Ohio': 5.425}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "Ohio"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Ohio': 6.1}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "Ohio"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'New Mexico': 6.575}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "New Mexico"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'New Mexico': -2.5}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "New Mexico"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Maryland': -0.025}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "Maryland"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Maryland': -8.15}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "Maryland"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Kansas': -7.3}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "Kansas"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Kansas': 0.75}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "Kansas"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Nebraska': -10.425}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "Nebraska"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'Nebraska': -3.15}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "Nebraska"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'West Virginia': 6.075}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults aged 18 years and older who have obesity","state": "West Virginia"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {'West Virginia': 7.8}
        for k, v in res.items():
            for key, value in TaskRunner.state_dif_from_mean({"question": "Percent of adults who engage in no leisure-time physical activity","state": "West Virginia"},
                                                self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
    
    def test_mean_by_category(self):
        res = {"('Ohio', 'Income', '$75,000 or greater')":30.05, "('New Mexico', 'Income', '$25,000 - $34,999')": 28.8, 
               "('Nebraska', 'Income', 'Less than $15,000')": 45.8, "('Maryland', 'Education', 'High school graduate')": 32.2,
               "('Kansas', 'Income', '$50,000 - $74,999')": 42.8, "('Maryland', 'Income', '$75,000 or greater')": 40.0,
               "('West Virginia', 'Education', 'High school graduate')": 29.45}
        for k, v in res.items():
            for key, value in TaskRunner.mean_by_category({"question": "Percent of adults aged 18 years and older who have obesity"},
                                                     self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
        res = {"('Kansas', 'Age (years)', '45 - 54')": 32.75, "('New Mexico', 'Age (years)', '55 - 64')": 35.0,
               "('Ohio', 'Race/Ethnicity', '2 or more races')": 26.4, "('Maryland', 'Income', '$15,000 - $24,999')": 43.5,
               "('Nebraska', 'Income', '$15,000 - $24,999')": 35.65,
               "('West Virginia', 'Education', 'High school graduate')": 21.7}
        for k, v in res.items():
            for key, value in TaskRunner.mean_by_category({"question": "Percent of adults who engage in no leisure-time physical activity"},
                                                     self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    if (abs(v - value) < float_info.epsilon):
                        self.assertTrue(True)
    
    def test_state_mean_by_category(self):
        
        res = {'Ohio': {"('Income', '$75,000 or greater')": 30.05}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults aged 18 years and older who have obesity",
                                               "state": "Ohio"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)
                    
        
        res = {'Ohio': {"('Race/Ethnicity', '2 or more races')": 26.4}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults who engage in no leisure-time physical activity",
                                               "state": "Ohio"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)

        res = {'New Mexico': {"('Income', '$25,000 - $34,999')": 28.8}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults aged 18 years and older who have obesity",
                                               "state": "New Mexico"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)
        res = {'New Mexico': {"('Age (years)', '55 - 64')": 35.0}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults who engage in no leisure-time physical activity",
                                               "state": "New Mexico"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)
        
        res = {'Kansas': {"('Income', '$50,000 - $74,999')": 42.8}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults aged 18 years and older who have obesity",
                                               "state": "Kansas"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)
        res = {'Kansas': {"('Age (years)', '45 - 54')": 32.75}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults who engage in no leisure-time physical activity",
                                               "state": "Kansas"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)
        
        res = {'Nebraska': {"('Income', 'Less than $15,000')": 45.8}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults aged 18 years and older who have obesity",
                                               "state": "Nebraska"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)

        res = {'Nebraska': {"('Income', '$15,000 - $24,999')": 35.65}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults who engage in no leisure-time physical activity",
                                               "state": "Nebraska"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)

        
        res = {'Maryland': {"('Education', 'High school graduate')": 32.2, "('Income', '$75,000 or greater')": 40.0}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults aged 18 years and older who have obesity",
                                               "state": "Maryland"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)
        res = {'Maryland': {"('Income', '$15,000 - $24,999')": 43.5}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults who engage in no leisure-time physical activity",
                                               "state": "Maryland"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)
    
        res = {'West Virginia': {"('Education', 'High school graduate')": 29.45}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults aged 18 years and older who have obesity",
                                               "state": "West Virginia"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)
        
        res = {'West Virginia': {"('Education', 'High school graduate')": 21.7}}
        for k, v in res.items():
            for key, value in TaskRunner.state_mean_by_category({"question": "Percent of adults who engage in no leisure-time physical activity",
                                               "state": "West Virginia"}, self.data_ingestor, self.count, self.jobs).items():
                if key == k:
                    for k_dict, v_dict in v.items():
                        if k_dict in value:
                            if abs(v_dict - value[k_dict]) < float_info.epsilon:
                                self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()