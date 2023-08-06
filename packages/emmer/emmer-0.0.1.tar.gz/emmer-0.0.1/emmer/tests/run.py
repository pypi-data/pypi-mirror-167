import unittest
import os
def download_test_data_from_url(download_folder):
    import wget
    print("\nDownloading test data \n")
    url_test_data = "https://surfdrive.surf.nl/files/index.php/s/I36mEBPiu40nXa5/download"  ## SURFdrive URL    
    wget.download(url_test_data, download_folder, )

def download_verify_data_from_url(download_folder):
    import wget
    print("\nDownloading verification data \n")
    url_verify_data = "https://surfdrive.surf.nl/files/index.php/s/bbacbB4dTL64l0W/download"  ## SURFdrive URL
    wget.download(url_verify_data, download_folder)

def extract_tar_files_in_folder(tar_folder, use_same_folder=True):
    import tarfile
    import os
    if use_same_folder == 0:
        target_folder = tar_folder
    else:
        target_folder = os.path.dirname(tar_folder)

    for file in os.listdir(tar_folder):
        if file.endswith(".tar.gz"):
            print("Extracting: {}".format(file))
            tar = tarfile.open(os.path.join(tar_folder,file))
            tar.extractall(target_folder)
            tar.close()

def run_tests():
    import emmer
    import os
    ## Make sure the test data is downloaded
    emmer_path = os.path.dirname(os.path.abspath(emmer.__file__))
    test_data_folder = os.path.join(emmer_path, "tests", "ndimage_unittest","data")
    test_verify_data_folder = os.path.join(emmer_path, "tests", "ndimage_unittest","verify")

    unittest_folder = os.path.join(emmer_path, "tests")
    
    if not os.path.exists(test_data_folder):
        os.makedirs(test_data_folder, exist_ok=True)
        download_test_data_from_url(test_data_folder)
    if not os.path.exists(test_verify_data_folder):
        os.makedirs(test_verify_data_folder, exist_ok=True)
        download_verify_data_from_url(test_verify_data_folder)
    
    ## Extract the tar files
    extract_tar_files_in_folder(test_data_folder, use_same_folder=True)
    extract_tar_files_in_folder(test_verify_data_folder, use_same_folder=True)

    ## Create the test suite
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(unittest_folder, pattern="test_*.py")
    
    ## Run the test suite
    test_runner = unittest.TextTestRunner(verbosity=0)
    test_result = test_runner.run(test_suite)
    print("test_result: {}".format(test_result))
    if test_result.wasSuccessful():
        print("All tests passed")
    else:
        print("Some tests failed")
        print(test_result.printErrors())
    
    print("="*80)
    print("Done")
    print("="*80)





