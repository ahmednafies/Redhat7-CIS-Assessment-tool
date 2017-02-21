
import source

# -------- 1.1.1.1 Ensure mounting of cramfs filesystems is disabled (Scored) -----#

def check_mount_cramfs_disabled():

    conf =  "1.1.1.1 Ensure mounting of cramfs filesystems is disabled (Scored)"
    cmd = "lsmod | grep cramfs"
    source.magic_function_one(conf, cmd)

# ---------- 1.1.1.2 Ensure mounting of freevxfs filesystems is disabled (Scored) ----#

def check_mount_freevxfs_disabled():

    conf =  "1.1.1.2 Ensure mounting of freevxfs filesystems is disabled (Scored)"
    cmd = "lsmod | grep freevxfs"
    source.magic_function_one(conf, cmd)

# ---------1.1.1.3 Ensure mounting of jffs2 filesystems is disabled (Scored)-----#

def check_mount_jffs2_disabled():

    conf =  "1.1.1.3 Ensure mounting of jffs2 filesystems is disabled (Scored)"
    cmd = "lsmod | grep jffs2"
    source.magic_function_one(conf, cmd)

#------- 1.1.1.4 Ensure mounting of hfs filesystems is disabled (Scored) -------#

def check_mount_hfs_disabled():

    conf =  "1.1.1.4 Ensure mounting of hfs filesystems is disabled (Scored)"
    cmd = "lsmod | grep hfs"
    source.magic_function_one(conf, cmd)


# ------ 1.1.1.5 Ensure mounting of hfsplus filesystems is disabled (Scored)-----#

def check_mount_hfsplus_disabled():

    conf =  "1.1.1.5 Ensure mounting of hfsplus filesystems is disabled (Scored)"
    cmd = "lsmod | grep hfsplus"
    source.magic_function_one(conf, cmd)


# ---------1.1.1.6 Ensure mounting of squashfs filesystems is disabled (Scored)-----#
def check_mount_squashfs_disabled():

    conf =  "1.1.1.6 Ensure mounting of squashfs filesystems is disabled (Scored)"
    cmd = "lsmod | grep squashfs"
    source.magic_function_one(conf, cmd)

# --------1.1.1.7 Ensure mounting of udf filesystems is disabled (Scored)-----------#

def check_mount_udf_disabled():

    conf =  "1.1.1.7 Ensure mounting of udf filesystems is disabled (Scored)"
    cmd = "lsmod | grep udf"
    source.magic_function_one(conf, cmd)


#-------- 1.1.1.8 Ensure mounting of FAT filesystems is disabled (Scored)-----#
def check_mount_fat_disabled():

    conf =  "1.1.1.7 Ensure mounting of udf filesystems is disabled (Scored)"
    cmd = "lsmod | grep vfat"
    source.magic_function_one(conf, cmd)



#------------------------ 1.1.1 - 1.8 --------------------------#



# ------- 1.1.1 check if Separate Partition for /tmp is created -------#

def check_partition_tmp_created():

    conf =  "1.1.2 check if Separate Partition for /tmp is created"
    cmd = 'grep "[[:space:]]/tmp[[:space:]]" /etc/fstab'
    source.magic_function_one(conf, cmd)


#------- 1.1.2 Set nodev option for /tmp Partition ----------#

def check_partition_tmp_nodev():

    conf = "1.1.3 Set nodev option for /tmp Partition "
    grep_output = 'grep "[[:space:]]/tmp[[:space:]]" /etc/fstab | grep nodev'
    mount_output = 'mount | grep "[[:space:]]/tmp[[:space:]]" | grep nodev'
    source.magic_function_two(conf, grep_output, mount_output)

#------- 1.1.3 Set nosuid option for /tmp Partition (Scored)-----#

def check_partition_nosuid():

    conf = "1.1.4 Set nosuid option for /tmp Partition (Scored) "
    grep_output = 'grep "[[:space:]]/tmp[[:space:]]" /etc/fstab | grep nosuid'
    mount_output = 'mount | grep "[[:space:]]/tmp[[:space:]]" | grep nosuid'
    source.magic_function_two(conf, grep_output, mount_output)

#------ 1.1.4 Set noexec option for /tmp Partition (Scored)--------#

def check_partition_noexec():

    conf = "1.1.5 Set noexec option for /tmp Partition (Scored)"
    grep_output = 'grep "[[:space:]]/tmp[[:space:]]" /etc/fstab | grep noexec'
    mount_output = 'mount | grep "[[:space:]]/tmp[[:space:]]" | grep noexec'
    source.magic_function_two(conf, grep_output, mount_output)

#------- 1.1.6 Ensure separate partition exists for /var (Scored)----#

def check_var_partition_exits():

    conf =  "1.1.6 check if Separate Partition for /var is created"
    cmd = 'mount | grep " /var " | wc -l'
    output = '1'
    source.check_separate_partition_exits(conf, cmd, output)

#------ 1.1.7 check if Separate Partition for /var/tmp is created ------#

def check_varTmp_partition_exits():

    conf =  "1.1.7 check if Separate Partition for /var/tmp is created"
    cmd = 'mount | grep " /var/tmp " | wc -l'
    output = '1'
    source.check_separate_partition_exits(conf, cmd, output)

#----- 1.1.8 Ensure nodev option set on /var/tmp partition (Scored) ------#

def check_varTmp_partition_nodev():

    conf =  '1.1.8 Ensure nodev option set on /var/tmp partition (Scored)'
    cmd = 'mount | grep /var/tmp'
    output = 'nodev'

    source.check_options_function(conf, cmd, output)

#----- 1.1.9 Ensure nosuid option set on /var/tmp partition (Scored) -----#

# -- test = "echo 'tmpfs on /var/tmp type tmpfs (rw,nosuid,nodev,noexec,relatime)'"

def check_varTmp_partition_nosuid():

    conf = '1.1.9 Ensure nosuid option set on /var/tmp partition (Scored)'
    cmd = 'mount | grep /var/tmp'
    output = 'nosuid'

    source.check_options_function(conf, cmd, output)

# ----- 1.1.10 Ensure noexec option set on /var/tmp partition (Scored) -----#

def check_varTmp_partition_noexec():

    conf = '1.1.10 Ensure noexec option set on /var/tmp partition (Scored)'
    cmd = 'mount | grep /var/tmp'
    output = 'noexec'

    source.check_options_function(conf, cmd, output)

#----- 1.1.11 Ensure separate partition exists for /var/log (Scored) ------#

def check_varLog_partition_exits():

    conf =  '1.1.11 Ensure separate partition exists for /var/log (Scored)'
    cmd = 'mount | grep " /var/log " | wc -l'
    output = '1'

    source.check_separate_partition_exits(conf, cmd, output)

# ----- 1.1.12 Ensure separate partition exists for /var/log/audit (Scored)--#

def check_varLogAudit_partition_exits():

    conf =  '1.1.12 Ensure separate partition exists for /var/log/audit (Scored)'
    cmd = 'mount | grep " /var/log/audit " | wc -l'
    output = '1'

    source.check_separate_partition_exits(conf, cmd, output)

# ---- 1.1.13 Ensure separate partition exists for /home (Scored) ----#

def check_home_partition_exists():

    conf =  '1.1.13 Ensure separate partition exists for /home (Scored)'
    cmd = 'mount | grep " /home " | wc -l'
    output = '1'

    source.check_separate_partition_exits(conf, cmd, output)

# ---- 1.1.14 Ensure nodev option set on /home partition (Scored) ---- #

def check_home_partition_nodev():

    conf = '1.1.14 Ensure nodev option set on /home partition (Scored)'
    cmd = 'mount | grep /home'
    output = 'nodev'

    source.check_options_function(conf, cmd, output)

# ---- 1.1.15 Ensure nodev option set on /dev/shm partition (Scored) ---#

def check_devShm_partition_nodev():

    conf =  '1.1.15 Ensure nodev option set on /dev/shm partition (Scored)'
    cmd = 'mount | grep /dev/shm'
    output = 'nodev'

    source.check_options_function(conf, cmd, output)

# ---- 1.1.16 Ensure nosuid option set on /dev/shm partition (Scored) ---#

def check_devShm_partition_nosuid():

    conf =  '1.1.16 Ensure nosuid option set on /dev/shm partition (Scored)'
    cmd = 'mount | grep /dev/shm'
    output = 'nosuid'

    source.check_options_function(conf, cmd, output)

# ---- 1.1.17 Ensure noexec option set on /dev/shm partition (Scored) ---#

def check_devShm_partition_noexec():

    conf =  '1.1.17 Ensure noexec option set on /dev/shm partition (Scored)'
    cmd = 'mount | grep /dev/shm'
    output = 'noexec'

    source.check_options_function(conf, cmd, output)

# ----- 1.1.21 Ensure sticky bit is set on all world-writable directories (Scored) --#

def check_sticky_bit_worldRw_directories():

    conf =  '1.1.21 Ensure sticky bit is set on all world-writable directories (Scored)'
    cmd = "sudo df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d"
    output = ''

    source.output_isEqualTo_terminal_output(conf, cmd, output)

# ----- 1.1.22 Disable Automounting (Scored) ------- #

def check_automounting_disabled():

    conf =  '1.1.22 Disable Automounting (Scored)'
    cmd = 'systemctl is-enabled autofs'
    output = 'disabled'

    source.output_isIn_terminal_output(conf, cmd, output)
