class Path(object):
    @staticmethod
    def db_dir(database):
        if database == 'ucf101':
            # folder that contains class labels
            root_dir = 'D:/project/3DCNN/UCF101/UCF-101'

            # Save preprocess data into output_dir
            output_dir = 'D:/project/3DCNN/UCF101/ucf101_results'

            return root_dir, output_dir
        elif database == 'hmdb51':
            # folder that contains class labels
            root_dir = 'D:/project/3DCNN//hmdb-51'

            output_dir = 'D:/project/3DCNN//hmdb51'

            return root_dir, output_dir
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def model_dir():
        return 'D:/project/3DCNN/c3d-pretrained.pth'
