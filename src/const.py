from os.path import dirname,abspath

data_dir_path = dirname(abspath(__file__))
dependency = ['tensorflow','pandas','matplotlib','seaborn','scikit-learn','ipykernel']

KB = 1024
MB = 1024 * 1024
GB = 1024 * 1024 * 1024