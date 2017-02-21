import fileSystemConfiguration
import softwareUpdates
import fileSystemIntegrity
import secureBootSettings
import additionalHardening
import mandatoryAccessControl
import warningBanners
######----- Code starts here -----######


def welcome_message():
    print('Welcome to CIS Red Hat Enterprise Linux 7 Benchmark assessment tool')
    print ('v2.1.0 - 06-02-2016')
    print ('---------------------------------------------------')

def promting_user():

    user_input = str(raw_input('would you like to start assessing your system (Y/N): '))

    if (user_input.lower() == "n"):
        print('exiting ....')
        exit()
    elif(user_input.lower() == "y"):
        print('starting ....')
        print('-----------------------------------------------------')
    else:
        print ('please enter either "y" or "n"')
        promting_user()

def run():

    welcome_message()
    promting_user()

#### ----------------------- FILE SYSTEM ---------------------------#####

#---------1.1.1.1 file system comfiguration------#
#    fileSystem.check_mount_cramfs_disabled()
#    fileSystem.check_mount_freevxfs_disabled()
#    fileSystem.check_mount_jffs2_disabled()
#    fileSystem.check_mount_hfs_disabled()
#    fileSystem.check_mount_hfsplus_disabled()
#    fileSystem.check_mount_squashfs_disabled()
#    fileSystem.check_mount_udf_disabled()
#    fileSystem.check_mount_fat_disabled()

# ---------1.1.1-------#

#    fileSystem.check_partition_tmp_created()
#    fileSystem.check_partition_tmp_nodev()
#    fileSystem.check_partition_nosuid()
#    fileSystem.check_partition_noexec()

#    fileSystem.check_var_partition_exits()
#    fileSystem.check_varTmp_partition_exits()
#    fileSystem.check_varTmp_partition_nodev()
#    fileSystem.check_varTmp_partition_nosuid()
#    fileSystem.check_varTmp_partition_noexec()

#    fileSystem.check_varLog_partition_exits()
#    fileSystem.check_varLogAudit_partition_exits()
#    fileSystem.check_home_partition_exists()
#    fileSystem.check_home_partition_nodev()
#    fileSystem.check_devShm_partition_nodev()
#    fileSystem.check_devShm_partition_nosuid()
#    fileSystem.check_devShm_partition_noexec()

#    fileSystem.check_sticky_bit_worldRw_directories()
#    fileSystem.check_automounting_disabled()


####-------------------------- SOFTWARE UPDATES------------------------#######

#--------1.2.1 software updates---------#
#    softwareUpdates.gpg_globally_activated()
#    softwareUpdates.check_rhnsd_daemon_disabled()

#--------1.3.1 file system integrity---------#
#    fileSystemIntegrity.check_aide_installed()


#-------1.4 Secure booting settings--------#
#    secureBootSettings.check_singleUserMode_authentication()

#------1.5 Additional Hardening ----------------#
    #additionalHardening.check_core_dumps_restricted()
    #additionalHardening.check_NX_XD_support_enabled()
    #additionalHardening.check_ASLR()
    #additionalHardening.check_prelink_disabled()

#------1.6 Mandatory Access Control -------------#

#    mandatoryAccessControl.check_SElinux_notDisabled_in_bootloader()
#    mandatoryAccessControl.check_SELinux_state_enforcing()
#    mandatoryAccessControl.check_SELinux_policy_configured()
#    mandatoryAccessControl.check_setTroubleShoot_notInstalled()
#    mandatoryAccessControl.check_mcstrans_notInstalled()
#    mandatoryAccessControl.check_noConfined_deamons_exist()
#    mandatoryAccessControl.check_SElinux_installed()

#------1.7 Warning banners ----------------------#
    warningBanners.check_message_of_the_day_configured()
    warningBanners.check_localLogin_warningBanner_configured()
    warningBanners.check_remotelogin_warningBanner_configured()
    warningBanners.check_permissions_on_etc_motd()
    warningBanners.check_permissions_on_etc_issue()

#----------------------------------------------------------------------#
run()
