from simba.read_config_unit_tests import (read_config_entry,
                                          read_config_file)
import os, glob
from collections import Counter, defaultdict
from simba.misc_tools import get_video_meta_data

class FrameMergerer(object):
    def __init__(self,
                 config_path: str,
                 frame_types: list,
                 frame_setting: bool,
                 video_setting: bool):

        self.config = read_config_file(config_path)
        self.frame_types = frame_types
        self.frame_setting, self.video_setting = frame_setting, video_setting
        self.project_path = read_config_entry(self.config, 'General settings', 'project_path', data_type='str')
        self.clf_path = os.path.join(self.project_path, 'frames', 'output', 'sklearn_results')
        self.gantt_path = os.path.join(self.project_path, 'frames', 'output', 'gantt_plots')
        self.path_path = os.path.join(self.project_path, 'frames', 'output', 'path_plots')
        self.data_path = os.path.join(self.project_path, 'frames', 'output', 'live_data_table')
        self.distance_path = os.path.join(self.project_path, 'frames', 'output', 'line_plot')
        self.probability_path = os.path.join(self.project_path, 'frames', 'output', 'probability_plots')
        self.heatmaps_path = os.path.join(self.project_path, 'frames', 'output', 'heatmaps_location')
        self.find_videos_in_each_dir()
        self.plot_cnt = len(frame_types)
        self.check_which_videos_exist_in_all_categories()
        self.check_frm_lenth_of_each_video()
        self.find_viable_video_names()
        self.create_videos()


    def find_videos_in_each_dir(self):
        self.video_in_each_dir = {}
        if 'Classifications' in self.frame_types:
            self.video_in_each_dir['Classifications'] = glob.glob(self.clf_path + '/*.mp4')
        if 'Gantt' in self.frame_types:
            self.video_in_each_dir['Gantt'] = glob.glob(self.gantt_path + '/*.mp4')
        if 'Path' in self.frame_types:
            self.video_in_each_dir['Path'] = glob.glob(self.path_path + '/*.mp4')
        if 'Data table' in self.frame_types:
            self.video_in_each_dir['Data table'] = glob.glob(self.data_path + '/*.mp4')
        if 'Distance' in self.frame_types:
            self.video_in_each_dir['Distance'] = glob.glob(self.distance_path + '/*.mp4')
        if 'Probability' in self.frame_types:
            self.video_in_each_dir['Probability'] = glob.glob(self.probability_path + '/*.mp4')
        if 'Heatmaps' in self.frame_types:
            self.video_in_each_dir['Heatmaps'] = glob.glob(self.heatmaps_path + '/*.mp4')

    def check_which_videos_exist_in_all_categories(self):
        self.videos = []
        videos_cnt = Counter()
        for frame_type in self.frame_types:
            entries = [os.path.basename(x) for x in self.video_in_each_dir[frame_type]]
            for entry in entries:
                videos_cnt[entry] += 1
        for video_name in videos_cnt:
            if videos_cnt[video_name] != self.plot_cnt:
                print('SIMBA WARNING: Not all user-specified video types selected have been created for video {}. Video {} is therefore '
                      'omitted from merged video creation.'.format(video_name, video_name))
            else:
                self.videos.append(video_name)
        if len(self.videos) == 0:
            print('SIMBA ERROR: None of your videos have pre-generated visualizations for ALL the user-specified video types.')
            raise ValueError('SIMBA ERROR: None of your videos have pre-generated visualizations for ALL the user-specified video types.')
        else:
            for k, v in self.video_in_each_dir.items():
                for entry in v:
                    if not os.path.basename(entry) in self.videos:
                        self.video_in_each_dir[k].remove(entry)

    def check_frm_lenth_of_each_video(self):
        frame_counts = {}
        videos = []
        for video_name in self.videos:
            frame_counts[video_name] = {}
            for video_type, video_path_lst in self.video_in_each_dir.items():
                video_path = [x for x in video_path_lst if os.path.basename(x) == video_name][0]
                frame_counts[video_name][video_type] = get_video_meta_data(video_path)['frame_count']
            results_dict = defaultdict(list)
            for video_name, video_frm_cnts in frame_counts.items():
                for entry, value in video_frm_cnts.items():
                    results_dict[value].append(entry)
            if len(results_dict.keys()) > 1:
                print('SIMBA WARNING: Not all user-specified video types has the same number of frames for video {}. Video {} is therefore '
                    'omitted from merged video creation:'.format(video_name, video_name))
                for k, values in results_dict.items():
                    print('{} frames found in {} plots for video {}'.format(str(k), values, video_name))
            else:
                videos.append(video_name)
        if len(videos) == 0:
            print('SIMBA ERROR: None of your videos have pre-generated visualizations with the same number of frames for all the user-specified video types.')
            raise ValueError('SIMBA ERROR: None of your videos have pre-generated visualizations with the same number of frames for all the user-specified video types.')
        else:
            for k, v in self.video_in_each_dir.items():
                for entry in v:
                    if not os.path.basename(entry) in self.videos:
                        self.video_in_each_dir[k].remove(entry)


    def find_viable_video_names(self):
        self.out_video_names = set()
        for k, v in self.video_in_each_dir.items():
            for entry in v:
                self.out_video_names.add(os.path.basename(entry))
        self.out_video_names = list(set(self.out_video_names))



    def create_videos(self):
        print('Creating {} merged video(s)...'.format(str(len(self.out_video_names))))
        for video_name in self.out_video_names:

































test = FrameMergerer(config_path=r'/Users/simon/Desktop/troubleshooting/train_model_project/project_folder/project_config.ini',
                     frame_types=['Classifications', 'Data table'],
                     frame_setting=False,
                     video_setting=True)







