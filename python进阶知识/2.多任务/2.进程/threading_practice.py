"""
文件夹 copy 器（多进程版）
进程池中任务出现问题不会产生异常信息
"""
import os
import multiprocessing


def copy_file(q, file_name, old_folder_name, new_folder_name):
    old_f = open(old_folder_name + os.sep + file_name, "rb")
    content = old_f.read()
    old_f.close()
    new_f = open(new_folder_name + os.sep + file_name, "wb")
    new_f.write(content)
    new_f.close()
    q.put(file_name)


def main():
    old_folder_name = input("请输入要复制的文件夹的名字：")
    try:
        new_folder_name = old_folder_name + "[复制]"
        os.mkdir(new_folder_name)
    except:
        pass
    file_names = os.listdir(old_folder_name)
    print(file_names)
    po = multiprocessing.Pool(5)
    q = multiprocessing.Manager().Queue()  # 针对进程池
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))
    po.close()
    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        file_name = q.get()
        print(f"已完成 copy {file_name}")
        copy_ok_num += 1
        if copy_ok_num >= all_file_num:
            break


if __name__ == "__main__":
    main()