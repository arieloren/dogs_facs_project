import cv2
import os
import shutil
import math


def get_the_file_name_and_type(path):
    import re
    path_list = re.split(r'[ \\]+', path)
    file_full_name = path_list[-1].split(".")
    file_name = file_full_name[0]
    file_type = file_full_name[1]
    return file_name, file_type


def split_number_by_decimal_point(num, digit_after_dec_point=1):
    num_str=str(round(num,digit_after_dec_point))
    int_part = num_str[:-1-digit_after_dec_point]
    frac_part = num_str[-1:]
    return int_part, frac_part

def single_video_to_frames(origin_path, destination_path, interval):
    count = 0
    step_for_saving_image = int(60 * interval)
    time_from_beginning = 0.0
    file_name, file_type = get_the_file_name_and_type(origin_path)
    cap = cv2.VideoCapture(origin_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(destination_path + os.sep + "garbage" + file_name + "." + file_type, fourcc, 20.0,
                          (640, 480))
    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret == True:
            if count % step_for_saving_image == 0:
                int_part, frac_part = split_number_by_decimal_point(time_from_beginning, 1)

                cv2.imwrite(destination_path + os.sep + file_name + "-frame_" + str(int_part) + "_" + str(frac_part) + ".jpg", frame)  # save frame as JPEG file

                time_from_beginning += interval

            count += 1
            frame = cv2.flip(frame, 0)

            # write the flipped frame
            out.write(frame)

            # cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def videos_to_frames(origin_folder_path, destination_folder_path, interval):
    for subdir, dirs, files in os.walk(origin_folder_path):
        for filename in files:
            filepath = subdir + os.sep + filename
            #image_origin_path = os.path.dirname(filepath)
            single_video_to_frames(filepath, destination_folder_path, interval)


if __name__ == '__main__':
    interval = 0.2
    # destination_path= 'D:\\Amir\\Machine_Learning_Course_Primrose\\Video_reading\\trial'
    # origin_path = 'D:\\Amir\\Machine_Learning_Course_Primrose\\Final_Project\\Daart3_F_2.avi'
    # single_video_to_frames(origin_path, destination_path, interval)

    origin_folder_path = 'D:\\Amir\\Machine_Learning_Course_Primrose\\Final_Project\\dog_videos_examples'
    destination_folder_path = 'D:\\Amir\\Machine_Learning_Course_Primrose\\Final_Project\\dog_videos_frames_examples'
    videos_to_frames(origin_folder_path, destination_folder_path, interval)
