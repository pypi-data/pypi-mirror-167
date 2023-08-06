import os


def upload_dir(local_dir, remote_dir, callback=None):
    '''
    上传本地文件夹到远程目录
    :param local_dir:
    :param remote_dir:
    :param callback:
    :return:
    '''
    local_dir = local_dir.replace('\\', '/').strip()
    if local_dir[-1] == '/':
        local_dir = local_dir[0:-1]
    dir_name = local_dir[local_dir.rindex('/') + 1:].replace('/', '')
    for parent, dirnames, filenames in os.walk(local_dir):
        parent = parent.replace('\\', '/')
        absolute_dir = remote_dir + '/' + parent[parent.rindex(dir_name):]
        for filename in filenames:
            parent = parent.replace('\\', '/')
            local_file = os.path.join(parent, filename).replace('\\', '/')

            remote_file = local_file.replace(local_dir,remote_dir+'/'+dir_name)

            print(dir_name,'================')
            # remote_file = remote_dir + '/' + local_file[local_file.rindex(dir_name):]
            # remote_file = remote_dir + '/' + dir_name + '/' + filename
            print(local_file, remote_file)
            print(f'upload file from {local_file} to {remote_file}')
            if callback is not None:
                callback(f'upload file from {local_file} to {remote_file}')


if __name__ == '__main__':
    import ssh_utils
    ssh = ssh_utils.SSH('192.168.9.244',22,'gradmin','gradmin@)')
    ssh.connect()
    ssh.upload_dir('D:/RHH_D10_1.0.1','/home/gradmin/ttt')
    ssh.close()
