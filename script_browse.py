import argparse
from profile import Profile
import time


#### ----- script ----- ####
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_profiles', type=int, default=5)
    parser.add_argument('--save_history', type=str2bool, default='t') #TODO

    args = parser.parse_args()
    num_profiles = args.num_profiles
    save_history = args.save_history
    start = time.time()
    # run this each day for a week
    for i in range(num_profiles):
        profile_num = i+1
        print('PROFILE ' + str(profile_num) + '\n $$$$$$$$$$$$$$$$')
        current_profile = Profile(profile_num)
        current_profile.visit_sites()
        time.sleep(10)
    end = time.time()
    print(end - start) # including time.sleep()'s, one run took about 600s (10 min)


def str2bool(v):
    if v.lower() in ('yes', 'true', 'True', 'TRUE', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'False', 'FALSE', 'f', 'h', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Not expected boolean type')


if __name__ == '__main__':
    main()


