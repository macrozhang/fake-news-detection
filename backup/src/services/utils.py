import os
from glob import glob

# if __name__ == '__main__':
#     for pipeline_file in glob(os.path.join('.', 'pipeline/code/pipelines', 'pd_*.yaml')):
#         with open(pipeline_file, 'r') as f:
#             pipeline = yaml.load(f, Loader=yaml.FullLoader)
#             run_pipeline(pipeline['processors'])