import glob
import os
import application.Library.Constant.GeneralConstant as GeneralConstant


def changeNameOfFileBaseOnFolder(path):
    last_processed_date = '0'
    if os.path.isfile(GeneralConstant.LAST_PROCESSED_DATE_PATH()):
        f = open(GeneralConstant.LAST_PROCESSED_DATE_PATH(), "r+", encoding='UTF-8')
        last_processed_date = f.readlines()[-1]
        f.close()

    def changeNameOfFileBaseOnFolderRecursive(file_path, name, curr_id):
        if os.path.isdir(file_path):  # is folder
            if os.path.basename(file_path) == 'CongNghe':
                name += '_CN'
            elif os.path.basename(file_path) == 'GiaoDuc':
                name += '_GD'
            elif os.path.basename(file_path) == 'KhoaHoc':
                name += '_KH'
            elif os.path.basename(file_path) == 'PhapLuat':
                name += '_PL'
            elif os.path.basename(file_path) == 'TheGioi':
                name += '_TG'
            elif os.path.basename(file_path) == 'ThoiSu':
                name += '_TS'
            elif os.path.basename(file_path) <= last_processed_date:
                return
            elif (os.path.basename(file_path) != 'ProcessedData') & (os.path.basename(file_path) != 'OriginalData'):
                name += os.path.basename(file_path)

            # Reset id
            if curr_id != 0:
                curr_id = 0

            print('Processing folder {0}: '.format(os.path.basename(file_path)))

            # Go Deeper inside folder
            for child_path in glob.glob(file_path + '/*'):
                changeNameOfFileBaseOnFolderRecursive(child_path, name, curr_id)
                curr_id += 1

        else:  # is file
            print('\t' + name + '_' + str(curr_id) + '.txt')
            os.rename(file_path, os.path.dirname(file_path) + '\\{0}_{1}.txt'.format(name, str(curr_id)))

    changeNameOfFileBaseOnFolderRecursive(path.pop(), '', 0)


def run_changing_folder_name_process():
    print('Changing folder name process')

    processed_data_path = GeneralConstant.PROCESSED_DATA_PATH()
    changeNameOfFileBaseOnFolder(glob.glob(processed_data_path))

    original_data_path = GeneralConstant.ORIGINAL_DATA_PATH()
    changeNameOfFileBaseOnFolder(glob.glob(original_data_path))

    print('Changing folder name process successfully')
