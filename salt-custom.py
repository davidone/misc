def get_block_device():
    '''
    Retrieve a list of disk devices
    '''
    cmd = '/bin/lsblk -n -io KNAME -d -e 1,7,11 -l'
    dev = __salt__['cmd.run'](cmd).splitlines()
    for i in dev:
        if i not in os.listdir('/dev'):
            raise CommandExecutionError(
                'Invalid device found'
            )
    return out
