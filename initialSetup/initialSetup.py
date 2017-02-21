import additionalHardening
import fileSystemConfiguration
import fileSystemIntegrity
import mandatoryAccessControl
import secureBootSettings
import softwareUpdates
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

#### ----------------------- FILE SYSTEM ---------------------------#####

def file_system_check():

# ---------1.1.1.1 file system comfiguration------#
   fileSystemConfiguration.check_mount_cramfs_disabled()
   fileSystemConfiguration.check_mount_freevxfs_disabled()
   fileSystemConfiguration.check_mount_jffs2_disabled()
   fileSystemConfiguration.check_mount_hfs_disabled()
   fileSystemConfiguration.check_mount_hfsplus_disabled()
   fileSystemConfiguration.check_mount_squashfs_disabled()
   fileSystemConfiguration.check_mount_udf_disabled()
   fileSystemConfiguration.check_mount_fat_disabled()

# ---------1.1.1-------#

   fileSystemConfiguration.check_partition_tmp_created()
   fileSystemConfiguration.check_partition_tmp_nodev()
   fileSystemConfiguration.check_partition_nosuid()
   fileSystemConfiguration.check_partition_noexec()

   fileSystemConfiguration.check_var_partition_exits()
   fileSystemConfiguration.check_varTmp_partition_exits()
   fileSystemConfiguration.check_varTmp_partition_nodev()
   fileSystemConfiguration.check_varTmp_partition_nosuid()
   fileSystemConfiguration.check_varTmp_partition_noexec()

   fileSystemConfiguration.check_varLog_partition_exits()
   fileSystemConfiguration.check_varLogAudit_partition_exits()
   fileSystemConfiguration.check_home_partition_exists()
   fileSystemConfiguration.check_home_partition_nodev()
   fileSystemConfiguration.check_devShm_partition_nodev()
   fileSystemConfiguration.check_devShm_partition_nosuid()
   fileSystemConfiguration.check_devShm_partition_noexec()

   fileSystemConfiguration.check_sticky_bit_worldRw_directories()
   fileSystemConfiguration.check_automounting_disabled()

def software_updates_check():

# --------1.2 software updates---------#
    softwareUpdates.gpg_globally_activated()
    softwareUpdates.check_rhnsd_daemon_disabled()

def file_system_integrity_check():
# --------1.3 file system integrity---------#
    fileSystemIntegrity.check_aide_installed()

def secure_boot_settings_check():
# -------1.4 Secure booting settings--------#
    secureBootSettings.check_singleUserMode_authentication()

def additional_hardening_check():
# ------1.5 Additional Hardening ----------------#
     additionalHardening.check_core_dumps_restricted()
     additionalHardening.check_NX_XD_support_enabled()
     additionalHardening.check_ASLR()
     additionalHardening.check_prelink_disabled()

def mandatory_access_control_check():
# ------1.6 Mandatory Access Control -------------#
    mandatoryAccessControl.check_SElinux_notDisabled_in_bootloader()
    mandatoryAccessControl.check_SELinux_state_enforcing()
    mandatoryAccessControl.check_SELinux_policy_configured()
    mandatoryAccessControl.check_setTroubleShoot_notInstalled()
    mandatoryAccessControl.check_mcstrans_notInstalled()
    mandatoryAccessControl.check_noConfined_deamons_exist()
    mandatoryAccessControl.check_SElinux_installed()

def warning_banners_check():
# ------1.7 Warning banners ----------------------#
    warningBanners.check_message_of_the_day_configured()
    warningBanners.check_localLogin_warningBanner_configured()
    warningBanners.check_remotelogin_warningBanner_configured()
    warningBanners.check_permissions_on_etc_motd()
    warningBanners.check_permissions_on_etc_issue()
    warningBanners.check_permissions_on_etc_issue_net()
    warningBanners.check_gdm_login_banner_configured()
    warningBanners.check_updates_patches_installed()
# ----------------------------------------------------------------------#

def run():

    welcome_message()
    promting_user()

    file_system_check()
    software_updates_check()
    file_system_integrity_check()
    secure_boot_settings_check()
    additional_hardening_check()
    mandatory_access_control_check()
    warning_banners_check()


run()
