import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from argparse import ArgumentParser
from easytorch import launch_training

def parse_args():
    parser = ArgumentParser(description='Run time series forecasting model in BasicTS framework based on EasyTorch!')
    # parser.add_argument('-c', '--cfg', required=True, help='training config')
    
    # parser.add_argument('-c', '--cfg', default='basicts/options/STID/STID_PEMS-BAY.py', help='training config')
    parser.add_argument('-c', '--cfg', default='basicts/options/STID/STID_PEMS04.py', help='training config')
    # parser.add_argument('-c', '--cfg', default='basicts/options/STID/STID_PEMS07.py', help='training config')
    # parser.add_argument('-c', '--cfg', default='basicts/options/STID/STID_PEMS08.py', help='training config')
    # parser.add_argument('-c', '--cfg', default='basicts/options/STID/STID_Electricity336.py', help='training config')

    parser.add_argument('--gpus', default='0', help='visible gpus')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    launch_training(args.cfg, args.gpus)
