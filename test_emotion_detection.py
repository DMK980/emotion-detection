from EmotionDetection.emotion_detection import emotion_detector
import unittest

class EmotionDetector(unittest.TestCase):
    """
        This is a unit test to see if the 
        emotion detector throws an error

    """

    def test_emotion_detector(self):
        """
            Method to run the test cases

        """

        # joy testcase
        testCase1 = emotion_detector("I am glad this happened")
        self.assertEqual(testCase1["dominant_emotion"],"joy")

        # joy testcase
        testCase2 = emotion_detector("I am really mad about this")
        self.assertEqual(testCase2["dominant_emotion"],"anger")

        # joy testcase
        testCase3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(testCase3["dominant_emotion"],"disgust")

        # joy testcase
        testCase4 = emotion_detector("I am so sad about this")
        self.assertEqual(testCase4["dominant_emotion"],"sadness")

        # joy testcase
        testCase1 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(testCase1["dominant_emotion"],"fear")

unittest.main()


