import unittest
import tempfile
import shutil
import os
import time
import threading
from cellmapping.utils import detect_changes


class TestDetectionChanges(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def test_detect_changes(self):
        detect_changes_thread = threading.Thread(
            target=detect_changes, args=(self.test_dir,))
        detect_changes_thread.start()

        time.sleep(1)
        test_file = os.path.join(self.test_dir, "test_file.txt")
        open(test_file, "w").close()

        time.sleep(1)
        self.assertTrue(os.path.isfile(test_file))

        os.remove(test_file)
        time.sleep(1)
        self.assertFalse(os.path.isfile(test_file))

    def tearDown(self):
        shutil.rmtree(self.test_dir)


if __name__ == '__main__':
    unittest.main()
