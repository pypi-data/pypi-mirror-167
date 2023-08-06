import unittest

from deptools.register import packages_from_files, Package


class TestRegister(unittest.TestCase):
    def test_packages_from_file(self):
        packages = packages_from_files(
            ['path/to/installer/ats-sdk-rpm_v7.5.0.zip', '/path/to/installer/ATS-SDK-ReleaseNotes.html'])
        self.assertEqual(packages, [
            Package(os='Linux (.rpm)',
                    product_id='1018',
                    installer='ats-sdk-rpm_v7.5.0.zip',
                    readme='ATS-SDK-ReleaseNotes.html',
                    name='ATS-SDK',
                    arch='x86_64')
        ])
        packages = packages_from_files(
            ['/path/to/installer/drivers-ats9352-dkms_7.3.1_arm64.deb', '/path/to/installer/ATS9352_Driver_V7.3.1_Readme.html'])
        self.assertEqual(packages, [
            Package(os='Linux (.deb)',
                    product_id='1036',
                    installer='drivers-ats9352-dkms_7.3.1_arm64.deb',
                    readme='ATS9352_Driver_V7.3.1_Readme.html',
                    name='ATS9352 Linux driver',
                    arch='arm64')
        ])


if __name__ == "__main__":
    unittest.main()
